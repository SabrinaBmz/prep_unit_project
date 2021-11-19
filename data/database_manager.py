import sqlite3
from sqlite3 import Error


def create_connection(db_file, encoding =('UTF-8')):
    """ create a database connection to a SQLite database """
    conn = None
    try:
        conn = sqlite3.connect(db_file)  # add a connection for the database
    except Error as e:
        print(e)

    # return the connection 
    return conn 

def close_connection(conn):
    """ closes a connection to a database """
    conn.cursor.close()


def select_all(conn, encoding =('UTF-8')):
    """select all rows from our table using the conn we already created """
    cur = conn.cursor()
    query = "SELECT * FROM longley" # write the query to retrive all data from the longley table 

    cur.execute(query)

    rows = cur.fetchall()  # fetch all rows using the cursor cur

    return rows 


def print_rows(rows):
    """ Loop through the retrived rows of a table and print them"""
    # All of the function body is a todo task
    for row in rows:
        print(row)
