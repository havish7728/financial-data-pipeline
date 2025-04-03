import mysql.connector
from config import DB_CONFIG

def create_connection():
    conn=mysql.connector.connect(**DB_CONFIG)
    return conn