import sqlite3

try:
    sql_connection = sqlite3.connect('sqlite_python.db')

    query = '''
    CREATE TABLE SqliteDB_developers (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    email TEXT NOT NULL UNIQUE,
    joining_date DATETIME,
    salary REAL NOT NULL);'''

    with open('tables.sql', 'r') as file:
        sql_script = file.read()

    cursor = sql_connection.cursor()
    print("Baza danych została podłączona")

    # cursor.execute(query)
    # sql_connection.commit()

    cursor.executescript(sql_script)

except sqlite3.Error as e:
    print("Bład podczas podłaczania bazy danych", e)
finally:
    if sql_connection:
        sql_connection.close()
        print("Baza została zamknięta")

# Bład podczas podłaczania bazy danych table SqliteDB_developers already exists
