import sqlite3
import os

db_file = os.path.join(os.path.dirname(__file__), "database.db")

def create_connection():
    global db_file
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except sqlite3.Error as e:
        print(f"Erro ao conectar ao banco de dados: {e}")
        return None

def create_table():
    global db_file
    conn = create_connection()
    if conn is not None:
        try:
            c = conn.cursor()
            # Ajuste na criação da tabela 'users' para incluir a coluna 'site_app'
            c.execute('''CREATE TABLE IF NOT EXISTS users
                         (id INTEGER PRIMARY KEY AUTOINCREMENT,
                          site_app TEXT NOT NULL,
                          username TEXT NOT NULL,
                          password TEXT NOT NULL)''')
            conn.commit()
            print("Tabela 'users' criada com sucesso.")
        except sqlite3.Error as e:
            print(f"Erro ao criar tabela: {e}")
        finally:
            conn.close()

def insert_credential(site, login, encrypted_password):
    global db_file
    conn = create_connection()
    if conn is not None:
        try:
            c = conn.cursor()
            c.execute("INSERT INTO users (site_app, username, password) VALUES (?, ?, ?)", (site, login, encrypted_password))
            conn.commit()
            print(f"Credencial inserida com sucesso para o site {site}.")
        except sqlite3.Error as e:
            print(f"Erro ao inserir credencial: {e}")
        finally:
            conn.close()

def find_credential(site):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT id, username, password FROM users WHERE site_app=?", (site,))
    result = cursor.fetchall()
    conn.close()
    return result

def find_all_credentials():
    """Retorna todas as credenciais armazenadas no banco de dados."""
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT id, username, password FROM users")
    result = cursor.fetchall()
    conn.close()
    return result

def get_encrypted_password(login_id):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT password FROM users WHERE id=?", (login_id,))
    result = cursor.fetchone()
    conn.close()
    return result[0]

def update_credential(site, new_login, new_password):
    global db_file
    conn = create_connection()
    if conn is not None:
        try:
            c = conn.cursor()
            c.execute("UPDATE users SET username=?, password=? WHERE site_app=?", (new_login, new_password, site))
            conn.commit()
            print(f"Credencial atualizada com sucesso para o site {site}.")
        except sqlite3.Error as e:
            print(f"Erro ao atualizar credencial: {e}")
        finally:
            conn.close()

def delete_credential(login_id):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM users WHERE id=?", (login_id,))
    conn.commit()
    conn.close()
