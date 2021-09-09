import requests
def infoUser(url):
    # check if .env endpoint ot empty
    if(url):
        # Request get on Endpoint and check url response
        try:
            reponse = requests.get(url)
        except requests.ConnectionError:
            print(f"La Connection a échouer changer de Endpoint ou Réessayer")
            exit()
            
        # Check response status
        if(reponse.status_code == 200):

            # Storage reponse at resquest
            contenu = reponse.json()
            # Split information in variables and verification
            try:
                email = contenu["email"]
                username = contenu["username"]
                useragent = contenu["user_agent"]
            except:
                print(f"Une erreur est survenue ! Réessayez !")
            # Search tag on user_agent and redefine user_agent in emoji
            if ('Windows' in useragent):
                useragent = "\U0001fa9f"
            elif ('Android' in useragent and 'Linux' in useragent):
                useragent = "\U0001f916"
            elif ('Linux' in useragent):
                useragent = "\U0001f427"
            elif ('Macintosh' in useragent or 'Mac OS X' in useragent):
                useragent = "\U0001f34e"
            else:
                useragent = "\U0001F910"

            # Information User
            print(f"L'adresse email de l'utilisateur {username} est {email}. Iel utilise le système d'exploitation {useragent}.")
        else:
            # Display error with status
            print(f"Une erreur {reponse.status_code} est survenue!")
    else:
        print(f"Votre URL est vide ! Vérifier votre .env")