import tkinter as tk
from tkinter import ttk
import login_bank as lb  # Supondo que `login_bank.py` contém a função de descriptografar senha
import data_base as db

class DeleteCredential(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.title("Delete Credential")
        self.geometry("700x500")
        self.parent = parent
        
        self.label_site = ttk.Label(self, text="Site/App:")
        self.label_site.pack(pady=10)
        
        self.entry_site = ttk.Entry(self, width=30)
        self.entry_site.pack()
        
        self.button_search = ttk.Button(self, text="Buscar Logins", command=self.search_logins)
        self.button_search.pack(pady=10)
        
        self.login_frame = ttk.Frame(self)
        self.login_frame.pack(pady=10, fill=tk.BOTH, expand=True)
        
        self.login_treeview = ttk.Treeview(self.login_frame, columns=("ID", "Login", "Senha Criptografada"), show="headings", selectmode="browse")
        self.login_treeview.heading("ID", text="ID")
        self.login_treeview.heading("Login", text="Login")
        self.login_treeview.heading("Senha Criptografada", text="Senha Criptografada")
        self.login_treeview.pack(fill=tk.BOTH, expand=True)
        
        self.label_password = ttk.Label(self, text="Senha:")
        self.label_password.pack(pady=10)
        
        self.entry_password = ttk.Entry(self, show="*")
        self.entry_password.pack()
        
        self.button_delete = ttk.Button(self, text="Deletar Login", command=self.delete_credential)
        self.button_delete.pack(pady=10)
        
        self.label_status = ttk.Label(self, text="")
        self.label_status.pack(pady=10)
        
        self.button_back = ttk.Button(self, text="Back", command=self.destroy)
        self.button_back.pack(pady=10)
        
    def search_logins(self):
        for item in self.login_treeview.get_children():
            self.login_treeview.delete(item)
        
        site = self.entry_site.get()
        results = db.find_credential(site)
        
        if results:
            for result in results:
                self.login_treeview.insert("", tk.END, values=result)
        else:
            print(f"Logins para o site '{site}' não encontrados.")
    
    def delete_credential(self):
        try:
            selected_item = self.login_treeview.selection()[0]
            login_id = self.login_treeview.item(selected_item, "values")[0]
            encrypted_password = self.login_treeview.item(selected_item, "values")[2]
            
            entered_password = self.entry_password.get()
            
            decrypted_password = lb.decripter_cezar(encrypted_password)
            
            if decrypted_password:
                db.delete_credential(login_id)
                self.label_status.config(text="Login deletado com sucesso.")
                self.search_logins()
            else:
                self.label_status.config(text="Senha incorreta. Não foi possível deletar o login.")
            
            self.entry_password.delete(0, tk.END)
        except IndexError:
            print("Por favor, selecione um login.")
