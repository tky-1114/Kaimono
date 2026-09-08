import mysql.connector
import os
from dotenv import load_dotenv

load_dotenv()

DB_HOST = os.getenv("DB_HOST")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_NAME = os.getenv("DB_NAME")

conn = mysql.connector.connect(
    host = DB_HOST,
    user = DB_USER,
    password = DB_PASSWORD
)

cursor = conn.cursor()

cursor.execute(
    f"CREATE DATABASE IF NOT EXISTS `{DB_NAME}`"
)

cursor.close()
conn.close()

conn = mysql.connector.connect(
    host = DB_HOST,
    user = DB_USER,
    password = DB_PASSWORD,
    database  = DB_NAME
)

cursor = conn.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS items (
        id INT AUTO_INCREMENT PRIMARY KEY,
        name VARCHAR(100) NOT NULL,
        num INT NOT NULL,
        details TEXT,
        deadline DATE NOT NULL,
        status INT NOT NULL DEFAULT 0
    )
""")

conn.commit()
cursor.close()
conn.close()

print("database built")