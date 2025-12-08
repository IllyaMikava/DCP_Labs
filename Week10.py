import mysql.connector
from tkinter import *
from tkinter import ttk

# --- Database Connection Settings ---
HOST = "localhost"
USER = "root"
PASSWORD = ""   
DATABASE = "school"


# --- Connect to MySQL ---
def get_connection():
    return mysql.connector.connect(
        host=HOST,
        user=USER,
        password=PASSWORD,
        database=DATABASE
    )


# --- Load Data into Table ---
def load_data(search_text=""):
    conn = get_connection()
    cursor = conn.cursor()

    for row in tree.get_children():
        tree.delete(row)

    if search_text:
        cursor.execute("SELECT * FROM students WHERE name LIKE %s", ("%" + search_text + "%",))
    else:
        cursor.execute("SELECT * FROM students")

    for row in cursor.fetchall():
        tree.insert("", END, values=row)

    conn.close()


# --- When Search Button Pressed ---
def on_search():
    text = search_entry.get()
    load_data(text)


# --- Main GUI Function ---
def main():
    global root, tree, search_entry

    root = Tk()
    root.title("Student Database Viewer")
    root.geometry("600x400")

    Label(root, text="Search Student by Name:").pack(pady=5)
    search_entry = Entry(root)
    search_entry.pack(pady=5)
    Button(root, text="Search", command=on_search).pack(pady=5)

    columns = ("ID", "Name", "Email")
    tree = ttk.Treeview(root, columns=columns, show="headings")

    for col in columns:
        tree.heading(col, text=col)
        tree.column(col, width=180)

    tree.pack(pady=10, fill=BOTH, expand=True)

    load_data()

    root.mainloop()

if __name__ == "__main__":
    main()
