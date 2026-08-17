import mysql.connector

def connect_mysql():
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="practice"
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