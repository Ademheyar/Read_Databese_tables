import tkinter as tk
from tkinter import ttk
import sqlite3

def create_treeview(tab, table_name):
    cursor = conn.cursor()
    cursor.execute(f"SELECT * FROM {table_name}")
    table_data = cursor.fetchall()

    tree = ttk.Treeview(tab)
    tree['columns'] = tuple([description[0] for description in cursor.description])
    tree.heading('#0', text='ID')

    for column in tree['columns']:
        tree.column(column, width=100)
        tree.heading(column, text=column)

    for index, data in enumerate(table_data):
        tree.insert('', 'end', text=str(index), values=data)

    # Add vertical scrollbar
    tree_scrollbar_y = ttk.Scrollbar(tab, orient='vertical', command=tree.yview)
    tree.configure(yscrollcommand=tree_scrollbar_y.set)
    tree_scrollbar_y.pack(side='right', fill='y')

    # Add horizontal scrollbar
    tree_scrollbar_x = ttk.Scrollbar(tab, orient='horizontal', command=tree.xview)
    tree.configure(xscrollcommand=tree_scrollbar_x.set)
    tree_scrollbar_x.pack(side='bottom', fill='x')

    tree.pack(expand=True, fill='both')
    return tree

# Connect to the backup database
conn = sqlite3.connect('database.db')

# Create the main window
window = tk.Tk()
window.title("Database Viewer")

# Make the window full screen
window.attributes('-fullscreen', True)

# Create a notebook (tabbed interface)
notebook = ttk.Notebook(window)

# Get the table names from the database
cursor = conn.cursor()
cursor.execute("SELECT name FROM sqlite_master WHERE type='table'")
tables = cursor.fetchall()

# Create tabs and Treeview widgets for each table
for table in tables:
    table_name = table[0]
    table_tab = ttk.Frame(notebook)
    table_treeview = create_treeview(table_tab, table_name)
    notebook.add(table_tab, text=table_name)

# Pack the notebook widget
notebook.pack(expand=True, fill='both')

# Start the main event loop
window.mainloop()

# Close the database connection
conn.close()
