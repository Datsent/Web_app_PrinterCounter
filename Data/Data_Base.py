import sqlite3, csv
import os.path
import time
from Data.Utils import utils
from datetime import datetime

def export_to_csv(table):
    now = datetime.now()
    formatted_date = now.strftime("%B_%Y")
    conn = sqlite3.connect(utils.DB_FILE)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Printers")
    column_names = [description[0] for description in cursor.description]
    data = cursor.fetchall()
    with open(f'C:\\Web_app_PrinterCounter\\Data\\db\\{formatted_date}.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(column_names)
        writer.writerows(data)
    conn.close()
    return f'C:\\Web_app_PrinterCounter\\Data\\db\\{formatted_date}.csv'

def get_time_modify():
    file_path = "Data/db/data.db"
    modification_time = os.path.getmtime(file_path)

    # Convert the modification time to a string
    modification_time_string = 'Last Update: ' + time.strftime("%d-%m-%Y %H:%M:%S", time.localtime(modification_time))
    return modification_time_string
def addresses_list():
    conn = sqlite3.connect(utils.DB_FILE)
    cursor = conn.cursor()
    query = "SELECT Model, Address FROM Printers"
    cursor.execute(query)
    results = cursor.fetchall()
    column_list = [(row[0], row[1]) for row in results]
    conn.close()
    return column_list

def edit_count(address, value):
    # Connect to the SQLite database
    conn = sqlite3.connect(utils.DB_FILE)
    cursor = conn.cursor()
    query = f"UPDATE Printers SET Count = '{value}' WHERE Address = '{address}'"
    cursor.execute(query)
    query = "UPDATE Printers SET Total_Pages = Count - Last_Count"
    cursor.execute(query)
    conn.commit()
    conn.close()

def status(address, status):
    conn = sqlite3.connect(utils.DB_FILE)
    cursor = conn.cursor()

    # Execute an SQL query to check if the column exists in the table
    query = "SELECT name FROM sqlite_master WHERE type='table' AND name='Printers' AND sql LIKE '%Status%'"
    cursor.execute(query)
    result = cursor.fetchone()
    query = f"UPDATE Printers SET Status = '{status}' WHERE Address = '{address}'"
    # Check if the column exists
    if result is not None:
        cursor.execute(query)
    else:
        cursor.execute('ALTER TABLE Printers ADD COLUMN Status TEXT')
        cursor.execute(query)
    conn.commit()
    conn.close()

def load_db_into_list(table):
    conn = sqlite3.connect(utils.DB_FILE)
    cur = conn.cursor()
    cur.execute('''CREATE TABLE IF NOT EXISTS Printers
                      (Name TEXT, Model TEXT, Address TEXT, Sup_Date TEXT, Start_Count INT, Last_Count INT,
                        Count INT, Total_Pages INT)''')
    query = f'SELECT * FROM {table}'
    with conn:
        cur.execute(query)
        list_db = cur.fetchall()
    conn.commit()
    conn.close()
    return list_db

def copy_table():
    now = datetime.now()
    formatted_date = now.strftime("%B_%Y")
    conn = sqlite3.connect(utils.DB_FILE)
    cursor = conn.cursor()
    cursor.execute('CREATE TABLE new_table AS SELECT * FROM Printers')
    query = f'ALTER TABLE new_table RENAME TO {formatted_date}'
    cursor.execute(query)
    conn.commit()
    conn.close()

def reset_counter():
    conn = sqlite3.connect(utils.DB_FILE)
    cursor = conn.cursor()
    query = "UPDATE Printers SET Last_Count = Count"
    cursor.execute(query)
    query = "UPDATE Printers SET Total_Pages = Count - Last_Count"
    cursor.execute(query)
    conn.commit()
    conn.close()

def set_offline_printer(address):
    conn = sqlite3.connect(utils.DB_FILE)
    cursor = conn.cursor()
    query = f"UPDATE Printers SET Count = Last_Count + 350 WHERE Address = '{address}'"
    cursor.execute(query)
    conn.commit()
    conn.close()
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
    #print(load_db_into_list('Printers'))
    #edit_row('123')
    #addresses_list()
    #get_tables_name()
    #copy_table()
    #export_to_csv('Printers')
    #reset_counter()
    status('10.1.1.180', 'V')
    print(get_time_modify())

