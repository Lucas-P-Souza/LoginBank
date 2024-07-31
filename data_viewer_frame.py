from ttkbootstrap import Style
from tkinter import ttk
import data_base as db
import tkinter as tk

class DatabaseViewerApp(tk.Tk):
    def __init__(self, db_file):
        super().__init__()
        self.title("Database Viewer")
        self.geometry("800x600")

        self.db_file = db_file

        #create a connection with the database
        self.connection = db.create_connection()
        
        #create the widgets
        self.create_widgets()

        #load the data from the database
        self.load_data()

    def create_widgets(self):
        #create a frame to display the data
        self.data_frame = ttk.Frame(self)
        self.data_frame.pack(padx=20, pady=20, fill=tk.BOTH, expand=True)

        #create a treeview to display the data
        self.treeview = ttk.Treeview(self.data_frame, columns=("ID", "Site/App", "User", "Senha Criptografada"), show="headings")
        self.treeview.heading("ID", text="ID")
        self.treeview.heading("Site/App", text="Site/App")
        self.treeview.heading("User", text="User")
        self.treeview.heading("Senha Criptografada", text="Senha Criptografada")
        self.treeview.pack(fill=tk.BOTH, expand=True)

        #botton to refresh the data
        self.refresh_button = ttk.Button(self, text="Refresh", command=self.load_data)
        self.refresh_button.pack(pady=10)
        
        #create a frame to search for data
        self.search_frame = tk.Frame(self)
        self.search_frame.pack(pady=10)

    def load_data(self):
        #clear the treeview
        for item in self.treeview.get_children():
            self.treeview.delete(item)

        #query to select all data from the users table
        query = "SELECT id, site_app, username, password FROM users"
        try:
            cursor = self.connection.cursor()
            cursor.execute(query)
            rows = cursor.fetchall()
            
            #insert the data into the treeview
            for row in rows:
                self.treeview.insert("", tk.END, values=row)

        except db.sqlite3.Error as e:
            print(f"Erro ao acessar o banco de dados: {e}")
    
    def __del__(self):
        #close the connection when the object is deleted
        if self.connection:
            self.connection.close()
