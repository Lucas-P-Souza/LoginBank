from data_viewer_frame import DatabaseViewerApp
from insert_frame import InsertFrame  
from tkinter import ttk
import login_bank as lb
import data_base as db
import tkinter as tk
import os

class FindPassword(tk.Toplevel):            
            
    def __init__(self, parent):
        super().__init__(parent)
        self.title("Find Password")
        self.geometry("800x500")
        self.parent = parent
        
        self.db_file = os.path.join(os.path.dirname(__file__), "database.db")
        
        self.connection = db.create_connection()
        
        self.create_widgets()
        
        self.load_data()
        
    def create_widgets(self):
        
        # Label e Entry para inserir o nome do site
        self.label_site = ttk.Label(self, text="Site/App:")
        self.label_site.pack(pady=10)
        
        self.entry_site = ttk.Entry(self, width=30)
        self.entry_site.pack()
        
        # Botão para buscar logins do site especificado
        self.button_search = ttk.Button(self, text="Buscar Logins", command=self.search_logins)
        self.button_search.pack(pady=10)
        
        # Frame para exibir os dados
        self.data_frame = ttk.Frame(self)
        self.data_frame.pack(padx=20, pady=20, fill=tk.BOTH, expand=True)

        # Cria uma Treeview para exibir os dados
        self.treeview = ttk.Treeview(self.data_frame, columns=("ID", "Site/App", "User", "Senha Criptografada"), show="headings")
        self.treeview.heading("ID", text="ID")
        self.treeview.heading("Site/App", text="Site/App")
        self.treeview.heading("User", text="User")
        self.treeview.heading("Senha Criptografada", text="Senha Criptografada")
        self.treeview.pack(fill=tk.BOTH, expand=True)

        # Botão para atualizar os dados
        self.refresh_button = ttk.Button(self, text="Refresh", command=self.load_data)
        self.refresh_button.pack(pady=10)
        
        self.search_frame = tk.Frame(self)
        self.search_frame.pack(pady=10)
        
        # Label e Entry para digitar a senha
        self.label_password = ttk.Label(self, text="Senha:")
        self.label_password.pack(pady=10)
        
        self.entry_password = ttk.Entry(self, show="*")  # Campo de senha
        self.entry_password.pack()
        
        # Botão para descriptografar a senha
        self.button_decrypt = ttk.Button(self, text="Descriptografar Senha", command=self.decrypt_password)
        self.button_decrypt.pack(pady=10)
        
        # Label para exibir a senha descriptografada
        self.label_decrypted_password = ttk.Label(self, text="")
        self.label_decrypted_password.pack(pady=10)
        
        # Botão para voltar para a janela principal
        self.button_back = ttk.Button(self, text="Back", command=self.destroy)
        self.button_back.pack(pady=10)
    
    def load_data(self):
        # Limpa os dados existentes na Treeview
        for item in self.treeview.get_children():
            self.treeview.delete(item)

        # Consulta SQL para selecionar todos os registros da tabela
        query = "SELECT id, site_app, username, password FROM users"
        try:
            cursor = self.connection.cursor()
            cursor.execute(query)
            rows = cursor.fetchall()
            
            # Insere os dados na Treeview
            for row in rows:
                self.treeview.insert("", tk.END, values=row)

        except db.sqlite3.Error as e:
            print(f"Erro ao acessar o banco de dados: {e}")
        
    def search_logins(self):
        
        # Limpa os dados existentes na Treeview de logins
        for item in self.treeview.get_children():
            self.treeview.delete(item)
        
        # Obtém o nome do site inserido pelo usuário
        site = self.entry_site.get()
        
        # Busca os logins associados ao site no banco de dados
        results = db.find_credential(site)
        
        if results:
            # Insere os logins encontrados na Treeview
            for result in results:
                values_with_site = (result[0], site, result[1], result[2])
                self.treeview.insert("", tk.END, values=values_with_site)
        else:
            print(f"Logins para o site '{site}' não encontrados.")
    
    def decrypt_password(self):
        try:
            # Obtém o ID do item selecionado na Treeview de logins
            selected_item = self.treeview.selection()[0]
            login_id = self.treeview.item(selected_item, "values")[0]
            login_user = self.treeview.item(selected_item, "values")[1]
            encrypted_password = self.treeview.item(selected_item, "values")[2]
            
            # Obtém a senha digitada pelo usuário
            entered_password = self.entry_password.get()
            
            # Descriptografa a senha
            if lb.is_password_correct(entered_password):
                
                #here you can choose which encryption method you want to use
                #you can choose between cezar cipher and vinegere cipher to decrypt the password
                #to use the cezar cipher, uncomment the line 93 and comment the line 95
                #to use the vinegere cipher, uncomment the line 95 and comment the line 93
                
                #here we decrypt the password using the cezar cipher
                #decrypted_password = lb.decripter_cezar(encrypted_password)
                #here we decrypt the password using the vinegere cipher
                decrypted_password = lb.decrypted_vinegere(encrypted_password, login_user)
                
            else:
                decrypted_password = "Senha incorreta"
            
            # Exibe a senha descriptografada
            self.label_decrypted_password.config(text=f"Senha descriptografada: {decrypted_password}")
            
            # Limpa o campo de senha após descriptografar
            self.entry_password.delete(0, tk.END)
        except IndexError:
            print("Por favor, selecione um login.")
