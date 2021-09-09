# Import library HTTP
import requests
# Url Endpoint
url = "https://random-data-api.com/api/internet_stuff/random_internet_stuff"
# Request get on Endpoint
reponse = requests.get(url)
# Storage reponse at resquest
contenu = reponse.json()
# Split information in variables
email = contenu["email"]
username = contenu["username"]
useragent = contenu["user_agent"]

# Search tag on user_agent and redefine user_agent in emoji
if ('Windows' in useragent):
    useragent = "\U0001fa9f"
elif ('Android' in useragent and 'Linux' in useragent):
    useragent = "\U0001f916"
elif ('Linux' in useragent):
    useragent = "\U0001f427"
elif ('Macintosh' in useragent or 'Mac OS X' in useragent):
    useragent = "\U0001f34e"

print("L'adresse email de l'utilisateur",username,"est",email,". Iel utilise le système d'exploitation ",useragent,".")