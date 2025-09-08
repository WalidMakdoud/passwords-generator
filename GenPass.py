import time
import random

while True:
    choix = input('Vous voulez créer un mot de passe ("y", "n", "exit") : ').strip().lower()

    if choix == "y":
        
        while True:
            try:
                length = int(input("Taper la longueur du mot de passe (Max = 14): "))
                if length <= 14:
                    break
                else:
                    print("Le maximum est 14. Essayez encore.\n")
            except ValueError:
                print("Entrée invalide. Tapez un nombre entier.\n")

        print("Création du mot de passe........")
        s = "QWERTYUIOPASDFGHJKLZXCVBNMqwertyuiopasdfghjklzxcvbnm1234567890!@#$%^&*()_+=<>?.,}{[]/-"
        p = "".join(random.choice(s) for _ in range(length))

        time.sleep(2)
        print("✅ Mot de passe généré :", p, "\n")

    elif choix == "n":
        print("Merci pour l'utilisation!\n")
    elif choix == "exit":
        print("Programme terminé.")
        break
    else:
        print('ERREUR: tapez un choix entre ("y", "n", "exit").\n')
