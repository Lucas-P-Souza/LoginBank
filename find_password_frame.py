from data_viewer_frame import DatabaseViewerApp
from insert_frame import InsertFrame  
from tkinter import ttk
import login_bank as lb
import data_base as db
import tkinter as tk
import os

#this class is responsible for the find password frame
class FindPassword(tk.Toplevel):            
    
    #this method is responsible for the initialization of the find password frame
    def __init__(self, parent):
        
        #here we initialize the find password frame with the name "Find Password" and the size 800x800
        super().__init__(parent)
        self.title("Find Password")
        self.geometry("800x800")
        self.parent = parent
        
        #here we load save were the database is located
        self.db_file = os.path.join(os.path.dirname(__file__), "database.db")
        
        #now we create a connection with the database
        self.connection = db.create_connection()
        
        #the create_widgets method is responsible for creating the widgets of the find password frame
        self.create_widgets()
        
        #the load_data method is responsible for loading the data from the database
        self.load_data()
        
    #the create_widgets method is responsible for creating the widgets of the find password frame
    def create_widgets(self):
        
        self.label_site = ttk.Label(self, text="Site/App:")
        self.label_site.pack(pady=10)
        
        self.entry_site = ttk.Entry(self, width=30)
        self.entry_site.pack()
        
        #here we create a button to search for logins 
        self.button_search = ttk.Button(self, text="Search logins", command=self.search_logins)
        self.button_search.pack(pady=10)
        
        #here we create a frame to display the data from the database
        self.data_frame = ttk.Frame(self)
        self.data_frame.pack(padx=20, pady=20, fill=tk.BOTH, expand=True)

        #create a treeview to display the data
        #the treeview is a widget that allows you to display data in a table format
        self.treeview = ttk.Treeview(self.data_frame, columns=("ID", "Site/App", "User", "Senha Criptografada"), show="headings")
        self.treeview.heading("ID", text="ID")
        self.treeview.heading("Site/App", text="Site/App")
        self.treeview.heading("User", text="User")
        self.treeview.heading("Senha Criptografada", text="Senha Criptografada")
        self.treeview.pack(fill=tk.BOTH, expand=True)

        #create a button that allows the user to refresh the data
        self.refresh_button = ttk.Button(self, text="Refresh", command=self.load_data)
        self.refresh_button.pack(pady=10)
        
        self.search_frame = tk.Frame(self)
        self.search_frame.pack(pady=10)
        
        #create a button that allows the user to insert a new login
        self.label_password = ttk.Label(self, text="Senha:")
        self.label_password.pack(pady=10)
        
        self.entry_password = ttk.Entry(self, show="*")  # Campo de senha
        self.entry_password.pack()
        
        #create a button that allows the user to decrypt the password
        self.button_decrypt = ttk.Button(self, text="Decrypt password", command=self.decrypt_password)
        self.button_decrypt.pack(pady=10)
        
        #create the place where the decrypted password will be displayed
        self.label_decrypted_password = ttk.Label(self, text="")
        self.label_decrypted_password.pack(pady=10)
        
        #create a button that allows the user to go back to the main window
        self.button_back = ttk.Button(self, text="Back", command=self.destroy)
        self.button_back.pack(pady=10)
    
    #the load_data method is responsible for loading the data from the database
    def load_data(self):
        
        #clear the data from the treeview
        for item in self.treeview.get_children():
            self.treeview.delete(item)

        #here we create a query to select all the data from the database
        #the query is a string that contains the sql command to be executed
        query = "SELECT id, site_app, username, password FROM users"
        try:
            cursor = self.connection.cursor()
            cursor.execute(query)
            rows = cursor.fetchall()
            
            #here we insert the data from the database into the treeview
            for row in rows:
                self.treeview.insert("", tk.END, values=row)

        except db.sqlite3.Error as e:
            print(f"Erro ao acessar o banco de dados: {e}")
    
    #the search_logins method is responsible for searching the logins in the database
    def search_logins(self):
        
        #clear the data from the treeview
        for item in self.treeview.get_children():
            self.treeview.delete(item)
        
        #save the site entered by the user
        site = self.entry_site.get()
        
        #search for the logins in the database using the site entered by the user
        results = db.find_credential(site)
        
        #if the results are not empty, insert the data into the treeview
        if results:

            #here we insert the data from the database into the treeview for each result found
            for result in results:
                values_with_site = (result[0], site, result[1], result[2])
                self.treeview.insert("", tk.END, values=values_with_site)
        #if the results are empty, display a message to the user
        else:
            print(f"Logins para o site '{site}' não encontrados.")
    
    #the decrypt_password method is responsible for decrypting the password of the selected login
    #the password is decrypted using the entered password by the user and the encryption method used to encrypt the password
    def decrypt_password(self):
        try:
            #capturing the selected item from the treeview and the login id, user and encrypted password
            selected_item = self.treeview.selection()[0]
            login_id = self.treeview.item(selected_item, "values")[0]
            login_user = self.treeview.item(selected_item, "values")[2]
            encrypted_password = self.treeview.item(selected_item, "values")[3]
            
            #this is the password entered by the user to decrypt the password
            entered_password = self.entry_password.get()
            
            #here we check if the password entered by the user is correct
            if lb.is_password_correct(entered_password):
                
                #here you can choose which encryption method you want to use
                #you can choose between cezar cipher and vinegere cipher to decrypt the password
                #to use the cezar cipher, uncomment the line 93 and comment the line 95
                #to use the vinegere cipher, uncomment the line 95 and comment the line 93
                
                #here we decrypt the password using the cezar cipher
                #decrypted_password = lb.decripter_cezar(encrypted_password)
                #here we decrypt the password using the vinegere cipher
                decrypted_password = lb.decrypted_vinegere(encrypted_password, login_user)
                
            #if the password entered by the user is incorrect, display a message to the user
            else:
                decrypted_password = "Senha incorreta"
            
            #display the decrypted password to the user
            self.label_decrypted_password.config(text=f"Senha descriptografada: {decrypted_password}")
            
            #clear the password entered by the user
            self.entry_password.delete(0, tk.END)
        except IndexError:
            print("Por favor, selecione um login.")
