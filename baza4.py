import sqlite3

try:
    sql_connection = sqlite3.connect('sqlite_python.db')
    select = '''
    SELECT * FROM software;
    '''

    update = '''
    UPDATE software SET price = 2000 WHERE id=1;
    '''

    delete = '''
    DELETE FROM software WHERE id=1;
    '''

    cursor = sql_connection.cursor()
    print("Baza danych została podłączona")

    # select
    for row in cursor.execute(select):
        print(row)  # (1, 'Python', 200.0)

    # update
    # cursor.execute(update)  # (1, 'Python', 2000.0)
    # sql_connection.commit()

    # delete
    cursor.execute(delete)
    sql_connection.commit()


except sqlite3.Error as e:
    print("Bład podczas podłaczania bazy danych", e)
finally:
    if sql_connection:
        sql_connection.close()
        print("Baza została zamknięta")
# CRUD - Create, Read, Update, Delete
# Insert, Select, Update, Delete
# Post, Get, Put, Delete
