# config.py
import os
from dotenv import load_dotenv

load_dotenv()  # Load variables from .env

MYSQL_HOST = os.environ.get("MYSQL_HOST")
MYSQL_USER = os.environ.get("MYSQL_USER")
MYSQL_PASSWORD = os.environ.get("MYSQL_PASSWORD")
MYSQL_DB = os.environ.get("MYSQL_DB")
PORT_DB = int(os.environ.get("PORT_DB", 3306))  # default port fallback
