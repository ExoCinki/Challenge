import os
from dotenv import load_dotenv
import checkInfoUser


load_dotenv()
# Url Endpoint
URL = os.getenv('URL_ENDPOINT')
# Call function infoUser
checkInfoUser.infoUser(URL)