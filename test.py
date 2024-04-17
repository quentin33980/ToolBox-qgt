import nmap
import re
import requests
import csv
import os
from datetime import datetime
from packaging import version

def scan_network(network):
    nm = nmap.PortScanner()
    nm.scan(hosts=network, arguments='-sn')
    hosts_list = [(x, nm[x]['status']['state']) for x in nm.all_hosts()]
    return hosts_list, nm

def scan_ports(host, nm):
    nm.scan(hosts=host, arguments='-sV')
    ports = {}
    for protocol in nm[host].all_protocols():
        ports[protocol] = list(nm[host][protocol].keys())
    return ports

def is_valid_network(network):
    pattern = r'^(?:\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}(?:/\d{1,2})?)$'
    return re.match(pattern, network) is not None

def is_vulnerable(version_detected, version_range):
    if version.parse(version_detected) <= version.parse(version_range):
        return True
    return False

def get_vulnerabilities(service_name, version_detected):
    vulnerabilities = []
    cve_ids = []
    try:
        response = requests.get(f"https://services.nvd.nist.gov/rest/json/cves/1.0?cpeMatchString=cpe:/a:{service_name}:{version_detected}")
        if response.status_code == 200:
            data = response.json()
            if 'result' in data and 'CVE_Items' in data['result']:
                for item in data['result']['CVE_Items']:
                    cve_id = item['cve']['CVE_data_meta']['ID']
                    severity = item['impact']['baseMetricV3']['cvssV3']['baseSeverity']
                    description = item['cve']['description']['description_data'][0]['value']
                    version_range = item.get('configurations', {}).get('nodes', [{}])[0].get('cpe_match', [{}])[0].get('versionEndIncluding', '0')
                    if is_vulnerable(version_detected, version_range):
                        vulnerabilities.append((severity, description, 'Critical' if severity == 'HIGH' else 'Non-Critical'))
                        cve_ids.append(cve_id)
    except Exception as e:
        print(f"Erreur lors de la récupération des vulnérabilités : {e}")
    return cve_ids, vulnerabilities

def save_to_csv(folder, filename, data):
    if not os.path.exists(folder):
        os.makedirs(folder)
    path = os.path.join(folder, filename)
    with open(path, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Host", "Port", "Service Name", "Version", "CVE ID", "Severity", "Description", "Criticity"])
        writer.writerows(data)

def main():
    while True:
        network = input("Veuillez entrer l'adresse du réseau à scanner (ex: 192.168.1.0/24 ou 192.168.1.1): ")
        if not is_valid_network(network):
            print("Format d'adresse incorrect. Veuillez entrer une adresse valide au format CIDR ou une adresse IP simple.")
        else:
            break

    print(f"Scanning network {network}...\n")
    hosts, nm = scan_network(network)
    if hosts:
        print("Adresses IP découvertes :")
        data_to_save = []
        for host, status in hosts:
            print(f"Host: {host} \t Status: {status}")
            ports = scan_ports(host, nm)
            if ports:
                for protocol, ports_list in ports.items():
                    for port in ports_list:
                        service = nm[host][protocol][port]
                        version_detected = service.get('version', "Version non disponible")
                        service_name = service.get('name', "Service inconnu")
                        cve_ids, vulnerabilities = get_vulnerabilities(service_name, version_detected)
                        if cve_ids:
                            for severity, description, criticity in vulnerabilities:
                                data_to_save.append([host, port, service_name, version_detected, ", ".join(cve_ids), severity, description, criticity])
                        else:
                            data_to_save.append([host, port, service_name, version_detected, "No CVE IDs found", "N/A", "No vulnerabilities found", "Non-Critical"])
            else:
                print(f"Aucun port TCP ouvert trouvé sur {host}")
        now = datetime.now().strftime("%d-%m-%Y-%H%M")
        save_to_csv("Resultats", f"scan_{now}.csv", data_to_save)
    else:
        print("Aucune adresse IP n'a été découverte.")

if __name__ == "__main__":
    main()
