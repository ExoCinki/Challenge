# Import library HTTP
import checkInfoUser
import os
from dotenv import load_dotenv

load_dotenv()
# Url Endpoint
URL = os.getenv('URL_ENDPOINT')
# Call function infoUser
checkInfoUser.infoUser(URL)