import os

import mysql.connector
from mysql.connector import errorcode

def get_database_connection():
    try:
        db_host = os.environ['DB_HOST']
        db_port = os.environ['DB_PORT']
        db_user = os.environ['DB_USER']
        db_password = os.environ['DB_PASSWORD']
        db_name = os.environ['DB_NAME']
        database_connection = mysql.connector.connect(
            host=db_host,
            port=db_port,
            user=db_user,
            #password='auvLecfk9X',
            password=db_password,
            database=db_name)
        return database_connection
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something is wrong with your user name or password")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist")
        else:
            print(err)
        raise err
