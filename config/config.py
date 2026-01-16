import psycopg2
import os
from dotenv import load_dotenv

load_dotenv()

database = os.getenv('DATABASE')
host = os.getenv('HOST')
user = os.getenv('USER')
password = os.getenv('PASSWORD')

def get_connection():
    connection = psycopg2.connect(dbname=database, host=host, user=user, password=password)
    return connection