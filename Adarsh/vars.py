# (c) adarsh-goel
import os
from os import getenv, environ
from dotenv import load_dotenv



load_dotenv()

class Var(object):
    MULTI_CLIENT = False
    API_ID = int(getenv('API_ID' , '6437947811'))
    API_HASH = str(getenv('API_HASH', 'e53eecba602443041994af39d029f3f6"'))
    BOT_TOKEN = str(getenv('BOT_TOKEN', "6437947811:AAETguqBfMr-R0vN4QqFLsXp4j-q1D-x2uw"))
    name = str(getenv('SESSION_NAME', 'filetolinkbot'))
    SLEEP_THRESHOLD = int(getenv('SLEEP_THRESHOLD', '60'))
    WORKERS = int(getenv('WORKERS', '4'))
    BIN_CHANNEL = int(getenv('BIN_CHANNEL', "-1002465335505"))
    PORT = int(getenv('PORT', 8080))
    BIND_ADRESS = str(getenv('WEB_SERVER_BIND_ADDRESS', '127.0.0.1'))
    PING_INTERVAL = int(environ.get("PING_INTERVAL", "1200"))  # 20 minutes
    OWNER_ID = set(int(x) for x in os.environ.get("OWNER_ID", "6368992891").split())  
    NO_PORT = bool(getenv('NO_PORT', False))
    APP_NAME = None
    OWNER_USERNAME = str(getenv('OWNER_USERNAME', "agent11147"))
    if 'DYNO' in environ:
        ON_HEROKU = True
        APP_NAME = str(getenv('APP_NAME'))
    
    else:
        ON_HEROKU = False
    FQDN = str(getenv('FQDN', '127.0.0.1:8080')) if not ON_HEROKU or getenv('FQDN', '') else APP_NAME+'.herokuapp.com'
    HAS_SSL=bool(getenv('HAS_SSL',False))
    if HAS_SSL:
        URL = "https://{}/".format(FQDN)
    else:
        URL = "http://{}/".format(FQDN)
    DATABASE_URL = str(getenv('DATABASE_URL', 'mongodb+srv://<dpdev0>:<1234dp>@cluster0.gonun.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0'))
    UPDATES_CHANNEL = str(getenv('UPDATES_CHANNEL', '1002036383574'))
    BANNED_CHANNELS = list(set(int(x) for x in str(getenv("BANNED_CHANNELS", "-1001362659779")).split())) 
