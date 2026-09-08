import mysql.connector
import os
from dotenv import load_dotenv

load_dotenv()

def connect_mysql():
    conn = mysql.connector.connect(
        host = os.getenv("DB_HOST"),
        user = os.getenv("DB_USER"),
        password = os.getenv("DB_PASSWORD"),
        database = os.getenv("DB_NAME")
    )
    return conn

def add_item(name, num, details, deadline):

    conn = connect_mysql()
    cursor = conn.cursor()

    sql = """
        INSERT INTO items (name, num, details, deadline) 
        VALUES (%s, %s, %s, %s);
    """

    cursor.execute(sql, (name, num, details, deadline))

    conn.commit()

    cursor.close()
    conn.close()

    print("追加しました")

def get_items():

    conn = connect_mysql()
    cursor = conn.cursor()

    sql = "SELECT * FROM items;"
    cursor.execute(sql)

    items = cursor.fetchall()

    cursor.close()
    conn.close()

    return items

def delete_items(id):

    conn = connect_mysql()
    cursor = conn.cursor()

    sql = "DELETE FROM items WHERE id = %s;"
    cursor.execute(sql, (id, ))

    conn.commit()
    conn.close()
    cursor.close()

def update_status(item_id, status):
    conn = connect_mysql()
    cursor = conn.cursor()

    sql = """
        UPDATE items
        SET status = %s
        WHERE id = %s
    """

    cursor.execute(sql, (status, item_id))

    conn.commit()
    conn.close()
    cursor.close()