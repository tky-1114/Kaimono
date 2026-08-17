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

    print("追加しました")

if __name__ == "__main__":
    pass