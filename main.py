import os
from dotenv import load_dotenv
import src.checkInfoUser


load_dotenv()
# Url Endpoint
URL = os.getenv('URL_ENDPOINT')
# Call function infoUser
src.checkInfoUser.infoUser(URL)
