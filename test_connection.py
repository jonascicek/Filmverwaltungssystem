import mysql.connector
import os

SQLIP = str(os.environ["SQLIP"])
SQLUsername = str(os.environ['SQL_USERNAME'])
SQLPassword = str(os.environ['SQL_PASSWORD'])
SQLDatabase = str(os.environ['SQL_DATABASE'])


def create_connection():
    connection = mysql.connector.connect(
            host = SQLIP,
            user = SQLUsername,
            password = SQLPassword,
            database = SQLDatabase
    )
    return connection

try:
    conn = create_connection()
    print("Verbindung zur MySQL-Datenbank erfolgreich")
    conn.close()
except mysql.connector.Error as err:
    print(f"Fehler: {err}")

