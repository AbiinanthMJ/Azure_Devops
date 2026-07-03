from dotenv import load_dotenv
import os

load_dotenv()

SERVER = os.getenv("SERVER")
DATABASE = os.getenv("DATABASE")
USERNAME = os.getenv("DB_USERNAME")
PASSWORD = os.getenv("DB_PASSWORD")