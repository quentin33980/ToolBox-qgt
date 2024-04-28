import subprocess

def main():
    while True:
        print("Menu:")
        print("1. Scan et vulnérabilité")
        print("2. Enumération")
        print("3. Option 3")
        print("4. Quitter")
        choice = input("Choisissez une option : ")

        if choice == '1':
            print("Vous avez choisi de lancer le scan et la vérification des vulnérabilités.")
            subprocess.run(["python", "test.py"])  # Exécute le script test.py

        elif choice == '2':
            print("Vous avez choisi de lancer l'enumération des repertoires.")
            subprocess.run(["python", "repertoires.py"])  # Exécute le script repertoires.py

        elif choice == '3':
            print("VVous avez choisi l'option 3")
       

        elif choice == '4':
            print("Au revoir !")
            break

        else:
            print("Choix invalide. Veuillez choisir une option valide.")

if __name__ == "__main__":
    main()