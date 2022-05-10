import sqlite3

try:
    sqliteConnection = sqlite3.connect('scrape_data.db')
    sqlite_query = '''CREATE TABLE DATA (
    id INTEGER PRIMARY  KEY,
    product_name TEXT NOT NULL,
    location TEXT NOT NULL,
    quality TEXT NOT NULL,
    price REAL NOT NULL 
    );'''
    cursor = sqliteConnection.cursor()
    cursor.execute(sqlite_query)
    sqliteConnection.commit()
    cursor.close()
except sqlite3.Error as error:
    print(error)
finally:
    if sqliteConnection:
        sqliteConnection.close()
        print('Closed')