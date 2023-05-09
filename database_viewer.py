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

def view_table():
    # Get the selected table from the Listbox
    selected_table = listbox.get(listbox.curselection())

    # Create a new tab for the selected table
    table_tab = ttk.Frame(notebook)
    table_treeview = create_treeview(table_tab, selected_table)
    notebook.add(table_tab, text=selected_table)

    # Switch to the new tab
    notebook.select(table_tab)

# Create the main window and notebook

# Create the main window
window = tk.Tk()
window.columnconfigure(0, weight=1)
window.rowconfigure(0, weight=1)
window.title("Aronium Database Viewer")

# Connect to the Aronium backup database
conn = sqlite3.connect('database.db')

# Make the window full screen
window.attributes('-fullscreen', True)

# Create a notebook (tabbed interface)
notebook = ttk.Notebook(window)
notebook.grid(column=0, row=0, columnspan=10, rowspan=10, sticky='nsew')
# Create the "Home" tab
home_tab = ttk.Frame(notebook)
home_tab.columnconfigure(0, weight=1)
home_tab.columnconfigure(1, weight=1)
home_tab.columnconfigure(2, weight=1)
home_tab.columnconfigure(3, weight=1)
home_tab.columnconfigure(4, weight=1)
home_tab.columnconfigure(5, weight=1)
home_tab.columnconfigure(6, weight=1)
home_tab.columnconfigure(7, weight=1)
home_tab.columnconfigure(8, weight=1)
home_tab.columnconfigure(9, weight=1)
home_tab.rowconfigure(0, weight=1)
home_tab.rowconfigure(1, weight=1)
home_tab.rowconfigure(2, weight=1)
home_tab.rowconfigure(3, weight=1)
home_tab.rowconfigure(4, weight=1)
home_tab.rowconfigure(5, weight=1)
home_tab.rowconfigure(6, weight=1)
home_tab.rowconfigure(7, weight=1)
home_tab.rowconfigure(8, weight=1)
home_tab.rowconfigure(9, weight=1)
notebook.add(home_tab, text='Home')

# Create a Listbox in the "Home" tab
listbox = tk.Listbox(home_tab)
listbox.grid(column=0, row=5, columnspan=5, rowspan=5, sticky='nsew')

# Create a "View Table" button in the "Home" tab
view_button = tk.Button(home_tab, text="View Table")
view_button.grid(column=6, row=0)

# Get the table names from the database
cursor = conn.cursor()
cursor.execute("SELECT name FROM sqlite_master WHERE type='table'")
tables = cursor.fetchall()

# Insert table names into the Listbox
for table in tables:
    
    table_name = table[0]
    print("name: " + str(table_name))
    listbox.insert('end', table_name)
    
# Start the main event loop
window.mainloop()

