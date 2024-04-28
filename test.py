import csv
import os
import nmap
import re
from datetime import datetime

def scan_network(network):
    """Scan the specified network using nmap and return hosts and their status along with nmap object."""
    nm = nmap.PortScanner()
    nm.scan(hosts=network, arguments='-sn')
    return [(x, nm[x]['status']['state']) for x in nm.all_hosts()], nm

def scan_ports(host, nm):
    """Scan ports for a given host using the nmap object provided and return services details."""
    nm.scan(hosts=host, arguments='-sV')
    ports = {}
    for protocol in nm[host].all_protocols():
        ports[protocol] = {}
        for port in nm[host][protocol].keys():
            service = nm[host][protocol][port]
            ports[protocol][port] = service
    return ports

def is_valid_network(network):
    """Validate the network address format using regex."""
    pattern = r'^(?:\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}(?:/\d{1,2})?)$'
    return re.match(pattern, network) is not None

def save_to_csv(folder, filename, data):
    """Save the collected data into a CSV file in the specified folder."""
    if not os.path.exists(folder):
        os.makedirs(folder)
    path = os.path.join(folder, filename)
    with open(path, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["IP_Host", "Port", "Service Name", "Version", "Produit"])
        writer.writerows(data)

def main():
    """Main function to orchestrate network scanning and port scanning process."""
    try:
        while True:
            network = input("Please enter the network address to scan (e.g., 192.168.1.0/24): ")
            if not is_valid_network(network):
                print("Incorrect address format. Please enter a valid CIDR or a simple IP address.")
            else:
                break

        print(f"Scanning network {network}...\n")
        hosts, nm = scan_network(network)
        if hosts:
            print("Discovered IP addresses:")
            data_to_save = []
            for host, status in hosts:
                print(f"Host: {host} \t Status: {status}")
                ports = scan_ports(host, nm)
                for protocol, port_info in ports.items():
                    for port, service_details in port_info.items():
                        service_name = service_details.get('name', "Unknown service")
                        version_detected = service_details.get('version', "Unknown version")
                        product = service_details.get('product', "Unknown product")
                        data_to_save.append([host, port, service_name, version_detected, product])
            now = datetime.now().strftime("%d-%m-%Y-%H")  # Changed time format to include ":" between hours and minutes
            save_to_csv("Resultats", f"scan_{now}.csv", data_to_save)
        else:
            print("No IP addresses were discovered.")
    except KeyboardInterrupt:
        print("Program stopped by user.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
