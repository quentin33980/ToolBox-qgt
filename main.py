import subprocess

def main():
    while True:
        print("Menu:")
        print("1. Option 1")
        print("2. Option 2")
        print("3. Scan et vulnérabilité")
        print("4. Quitter")
        choice = input("Choisissez une option : ")

        if choice == '1':
            print("Vous avez choisi l'option 1")
            # Ajoutez ici le code pour l'option 1

        elif choice == '2':
            print("Vous avez choisi l'option 2")
            # Ajoutez ici le code pour l'option 2

        elif choice == '3':
            print("Vous avez choisi de lancer le scan et la vérification des vulnérabilités.")
            subprocess.run(["python", "test.py"])  # Exécute le script test.py

        elif choice == '4':
            print("Au revoir !")
            break

        else:
            print("Choix invalide. Veuillez choisir une option valide.")

if __name__ == "__main__":
    main()
