import sqlite3
from Data.Utils import utils

def load_db_into_list():
    conn = sqlite3.connect(utils.DB_FILE)
    cur = conn.cursor()
    with conn:
        cur.execute("SELECT * FROM Printers")
        list_db = cur.fetchall()
    conn.commit()
    conn.close()
    return list_db

def get_tables_name():
    conn = sqlite3.connect(utils.DB_FILE)

    cursor = conn.execute("SELECT name FROM sqlite_master WHERE type='table';")
    name_list = [table[0] for table in cursor.fetchall()]
    conn.close()
    return name_list

def add_list_to_db(data):
    connection = sqlite3.connect(utils.DB_FILE)
    cursor = connection.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS Printers
                  (Name TEXT, Model TEXT, Address TEXT, Sup_Date TEXT, Start_Count INT, Last_Count INT,
                    Count INT, Total_Pages INT)''')
    cursor.execute('''INSERT INTO Printers(Name,Model,Address,Sup_Date,Start_Count,Last_Count,Count,Total_Pages)
                        VALUES(?,?,?,?,?,?,?,?)''', (data[0], data[1], data[2], data[3], data[4], data[5], data[6],
                                                     int(data[6]) - int(data[5])))
    connection.commit()
    connection.close()

if __name__ == '__main__':
    #add_list_to_db(['Dima', "MD12345", "10.1.1.210", "23.05.2023", "0", "40", "50000"])
    #load_db_into_list()
    get_tables_name()