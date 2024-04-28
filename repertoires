import requests
import os

def scan_directories(server_ip, server_port, wordlist_path):
    """Scan the specified server for directories using a given wordlist."""
    base_url = f"http://{server_ip}:{server_port}"
    existing_directories = []

    # Vérifier l'existence du fichier wordlist
    if not os.path.exists(wordlist_path):
        print("Le chemin de la wordlist est invalide.")
        return

    try:
        with open(wordlist_path, 'r') as file:
            for line in file:
                directory = line.strip()
                if directory:
                    url = f"{base_url}/{directory}"
                    try:
                        response = requests.get(url)
                        if response.status_code == 200:
                            print(f"Répertoire trouvé : {url}")
                            existing_directories.append(url)
                        else:
                            print(f"Répertoire non trouvé : {url}")
                    except requests.RequestException:
                        print(f"Erreur de connexion à {url}")
    except FileNotFoundError:
        print("Le fichier wordlist n'a pas pu être ouvert.")

    return existing_directories

def main():
    """Demande à l'utilisateur les informations nécessaires et lance le scan."""
    server_ip = input("Entrez l'IP du serveur à scanner : ")
    server_port = input("Entrez le port du serveur : ")
    wordlist_path = input("Entrez le chemin complet de la wordlist à utiliser : ")

    print("\nDémarrage du scan...")
    directories = scan_directories(server_ip, server_port, wordlist_path)
    if directories:
        print("\nRépertoires existants trouvés :")
        for directory in directories:
            print(directory)
    else:
        print("\nAucun répertoire existant trouvé.")

if __name__ == "__main__":
    main()
