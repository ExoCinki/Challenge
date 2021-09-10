# Import library HTTP
import requests
from src import checkOsUser


def infoUser(url):
    # check if .env endpoint ot empty
    if url and "http" in url:
        # Request get on Endpoint and check url response
        try:
            reponse = requests.get(url)
        except requests.ConnectionError:
            print(f"La Connection a échouer changer de Endpoint ou Réessayer")
            exit()

        # Check response status
        if reponse.status_code == 200:

            # Storage response at request
            contenu = reponse.json()
            # Split information in variables and verification
            try:
                email, username, useragent = contenu["email"], contenu["username"], contenu["user_agent"]
            except:
                print(f"Une erreur est survenue ! Réessayez !")
                # Information User
            print(
                f"L'adresse email de l'utilisateur {username} est {email}. Iel utilise le système d'exploitation {checkOsUser.checkOs(useragent)}.")
        else:
            # Display error with status
            print(f"Une erreur {reponse.status_code} est survenue!")
    else:
        print(f"Votre URL est vide ! Vérifier votre .env")
