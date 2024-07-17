import tkinter as tk
import login_bank as lb
import data_base as db
import os

class InsertFrame(tk.Frame):
    def __init__(self, parent, back_callback):
        super().__init__(parent)
        self.back_callback = back_callback
        
        #here we create the entry field for the site or app
        self.label_site = tk.Label(self, text="Insert new site or app")
        self.label_site.pack(pady=5)
        self.entry_site = tk.Entry(self)
        self.entry_site.pack(pady=2)

        #here we create the entry field for the login
        self.label_login = tk.Label(self, text="Insert new login")
        self.label_login.pack(pady=5)
        self.entry_login = tk.Entry(self)
        self.entry_login.pack(pady=2)

        #here we create the entry field for the password
        self.label_password = tk.Label(self, text="Insert new password")
        self.label_password.pack(pady=5)
        self.entry_password = tk.Entry(self)
        self.entry_password.pack(pady=2)

        #here we create the button to insert the credentials
        #when the button is clicked, the function insert_credentials is called to insert the credentials 
        # into the database
        self.button_insert = tk.Button(self, text="Insert", command=self.insert_credentials)
        self.button_insert.pack(pady=20)
        
        #botton to go back to the main window
        self.button_back = tk.Button(self, text="Back", command=self.back_callback)
        self.button_back.pack(pady=20)
    
    def insert_credentials(self):
        #it gets the site, login and password from the entry fields
        site = self.entry_site.get()
        login = self.entry_login.get()
        password = self.entry_password.get()
        
        #here is where you can choose which encryption method you want to use
        #you can choose between cezar cipher and vinegere cipher to encrypt the password
        #to use the cezar cipher, uncomment the line 51 and comment the line 53
        #to use the vinegere cipher, uncomment the line 53 and comment the line 51
        
        #here we encrypt the password using the cezar cipher
        #encrypted_password = lb.encrepter_cezar(password, login, site)
        #here we encrypt the password using the vinegere cipher
        encrypted_password = lb.encrypted_vinegere(password, login, site)
        
        #here we insert the credentials into the database
        db.insert_credential(site, login, encrypted_password)
        
        #here we clear the entry fields after inserting the credentials into the database
        self.entry_site.delete(0, tk.END)
        self.entry_login.delete(0, tk.END)
        self.entry_password.delete(0, tk.END)
