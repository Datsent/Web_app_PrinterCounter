import tkinter as tk
import sqlite3
from tkinter import ttk


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('Table with Inputs and SQLite')
        self.geometry('970x400')

        # Create delete labels and fields
        delete_frame = ttk.Frame(self, borderwidth=1, border=2, relief=tk.SUNKEN, name='delete')
        title_delete_grid = ttk.Label(delete_frame, text='Delete Printer', font=('Helvetica', 12, 'bold'))
        comment_delete = ttk.Label(delete_frame, text='Select row and input the IP address of Printer', font=('David', 10))
        ip_d_label = ttk.Label(delete_frame, text='IP:')
        ip_d_input = ttk.Entry(delete_frame)
        delete_button = ttk.Button(delete_frame, text='Delete', command=lambda: self.delete_printer(ip_d_input.get()))

        # Create input labels and fields
        input_layout = ttk.Frame(self, borderwidth=1, relief=tk.SUNKEN, name='play')
        title_input_grid = ttk.Label(input_layout, text='Input Printer', font=('Helvetica', 12, 'bold'))
        name_label = ttk.Label(input_layout, text='Name:')
        name_input = ttk.Entry(input_layout)
        Model_label = ttk.Label(input_layout, text='Model:')
        Model_input = ttk.Entry(input_layout)
        ip_adress_label = ttk.Label(input_layout, text='IP Adress:')
        ip_adress_input = ttk.Entry(input_layout)
        sup_date_label = ttk.Label(input_layout, text='Supply Date:')
        sup_date_input = ttk.Entry(input_layout)
        start_count_label = ttk.Label(input_layout, text='Start Count:')
        start_count_input = ttk.Entry(input_layout)
        last_count_label = ttk.Label(input_layout, text='Last Count:')
        last_count_input = ttk.Entry(input_layout)
        submit_button = ttk.Button(input_layout, text='Submit', command=lambda: (self.add_to_table(name_input.get(), Model_input.get(), ip_adress_input.get(),
                                                                                          sup_date_input.get(), start_count_input.get(),
                                                                                          int(last_count_input.get()), int(last_count_input.get()))))

        # Create layout for delete fields and button
        title_delete_grid.grid(row=0, column=0, padx=5, pady=0, columnspan=3)
        comment_delete.grid(row=1, column=0, padx=5, pady=0, columnspan=3)
        ip_d_label.grid(row=2, column=0, padx=5, pady=10)
        ip_d_input.grid(row=2, column=1, padx=5, pady=5)
        delete_button.grid(row=3, column=0, columnspan=2)

        # Create layout for input fields and button
        title_input_grid.grid(row=0, column=0, padx=5, pady=5, columnspan=6)
        name_label.grid(row=1, column=0, padx=5, pady=5)
        name_input.grid(row=1, column=1, padx=5, pady=5)
        Model_label.grid(row=2, column=0, padx=5, pady=5)
        Model_input.grid(row=2, column=1, padx=5, pady=5)
        ip_adress_label.grid(row=1, column=2, padx=5, pady=5)
        ip_adress_input.grid(row=1, column=3, padx=5, pady=5)
        sup_date_label.grid(row=2, column=2, padx=5, pady=5)
        sup_date_input.grid(row=2, column=3, padx=5, pady=5)
        start_count_label.grid(row=1, column=4, padx=5, pady=5)
        start_count_input.grid(row=1, column=5, padx=5, pady=5)
        last_count_label.grid(row=2, column=4, padx=5, pady=5)
        last_count_input.grid(row=2, column=5, padx=5, pady=5)
        submit_button.grid(row=3, column=0, padx=5, pady=5, columnspan=6)

        self.table = ttk.Treeview(self)
        self.table['columns'] = ('Name', 'Model', 'IP Adress', 'Supply Date', 'Start Count', 'Last Count', 'Count', 'Total Pages')
        self.table.heading('#0', text='ID')
        self.table.column('#0', width=50)
        self.table.heading('Name', text='Name')
        self.table.column('Name', width=200)
        self.table.heading('Model', text='Model')
        self.table.column('Model', width=100)
        self.table.heading('IP Adress', text='IP Adress')
        self.table.column('IP Adress', width=100)
        self.table.heading('Supply Date', text='Supply Date')
        self.table.column('Supply Date', width=100)
        self.table.heading('Start Count', text='Start Count')
        self.table.column('Start Count', width=100)
        self.table.heading('Last Count', text='Last Count')
        self.table.column('Last Count', width=100)
        self.table.heading('Count', text='Count')
        self.table.column('Count', width=50)
        self.table.heading('Total Pages', text='Total Pages')
        self.table.column('Total Pages', width=50)



        # Create layout for table and input fields/button
        main_layout = ttk.Frame(self)
        self.table.grid(row=0, column=0, padx=5, pady=5, columnspan=8)  #
        input_layout.grid(row=1, column=0, padx=5, pady=5, rowspan=5)
        delete_frame.grid(row=1, column=1, padx=5, pady=5)
        main_layout.grid(row=2, column=0, padx=5, pady=5)

        # Connect to database
        self.conn = sqlite3.connect('Data/db/example.db')
        self.cursor = self.conn.cursor()

        # Create table in database if it doesn't exist
        self.cursor.execute('CREATE TABLE IF NOT EXISTS page_count (id INTEGER PRIMARY KEY, name TEXT, model TEXT, adress TEXT, sup_date TEXT, start_count INTEGER, last_count INTEGER, count INTEGER, total_pages INTEGER)')

        # Populate table with data from database
        self.cursor.execute('SELECT * FROM page_count')
        rows = self.cursor.fetchall()
        for row in rows:
            self.table.insert('', 'end', text=row[0], values=(row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8]))

    def add_to_table(self, name, model, adress, sup_date, start_count, last_count, count):
        # Add data to database
        self.cursor.execute('INSERT INTO page_count (name, model, adress, sup_date, start_count, last_count, count, total_pages) VALUES (?, ?, ?, ?, ?, ?, ?, ?)',
                            (name, model, adress, sup_date, start_count, last_count, count, last_count))
        self.conn.commit()

        # Add data to table
        row_id = self.cursor.lastrowid
        self.table.insert('', 'end', text=row_id, values=(name, model, adress, sup_date, start_count, last_count, count, count - last_count))


    def delete_printer(self, ip):
        self.cursor.execute(f'DELETE from page_count where adress = "{ip}"')
        self.conn.commit()
        items = self.table.get_children()
        for item in items:
            data = self.table.item(item)['values'][2]
            if str(ip) == str(data):
                selected_item = self.table.selection()[0]
                self.table.delete(selected_item)
                break
            else:
                pass

if __name__ == '__main__':
    app = App()
    app.mainloop()
