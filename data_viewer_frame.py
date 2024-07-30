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

        # Cria uma conexão com o banco de dados
        self.connection = db.create_connection()
        
        # Cria widgets para exibição dos dados
        self.create_widgets()

        # Carrega e exibe dados iniciais
        self.load_data()

    def create_widgets(self):
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
    
    def __del__(self):
        # Fecha a conexão com o banco de dados ao destruir a janela
        if self.connection:
            self.connection.close()
