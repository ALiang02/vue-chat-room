import sqlite3
import os

database_path = os.path.dirname(__file__) + '/my.db'

def execute_sql(sql, choice):
    my_db = sqlite3.connect(database_path)
    my_cursor = my_db.cursor()
    my_cursor.execute(sql)
    results = []
    if choice == 'select':
        results = my_cursor.fetchall()
    else:
        my_db.commit()
    my_cursor.close()
    my_db.close()
    return results

if __name__ == '__main__':
    sql = "SELECT * FROM user WHERE user_name  = '%s'" % "jl"
    results = execute_sql(sql, 'select')
    print(results)