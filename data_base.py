import sqlite3
import os

#cathes the path of the database file
db_file = os.path.join(os.path.dirname(__file__), "database.db")

#creates a connection with the database
def create_connection():
    global db_file
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except sqlite3.Error as e:
        print(f"Erro ao conectar ao banco de dados: {e}")
        return None

#creates the table 'users' in the database
def create_table():
    global db_file
    conn = create_connection()
    if conn is not None:
        try:
            c = conn.cursor()
            #here we create the table 'users' with the columns 'id', 'site_app', 'username' and 'password'
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

#inserts a new credential in the database
def insert_credential(site, login, encrypted_password):
    global db_file
    conn = create_connection()
    if conn is not None:
        try:
            #here we insert the new credential in the table 'users'
            c = conn.cursor()
            c.execute("INSERT INTO users (site_app, username, password) VALUES (?, ?, ?)", (site, login, encrypted_password))
            conn.commit()
            print(f"Credencial inserida com sucesso para o site {site}.")
        except sqlite3.Error as e:
            print(f"Erro ao inserir credencial: {e}")
        finally:
            conn.close()

#finds a credential in the database
def find_credential(site):
    conn = create_connection()
    cursor = conn.cursor()
    #here we select the credential with the site equal to the parameter 'site'
    cursor.execute("SELECT id, username, password FROM users WHERE site_app=?", (site,))
    result = cursor.fetchall()
    conn.close()
    return result

#finds all credentials in the database
def find_all_credentials():
    #here we select all credentials in the table 'users'
    """Retorna todas as credenciais armazenadas no banco de dados."""
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT id, username, password FROM users")
    result = cursor.fetchall()
    conn.close()
    return result

#finds a credential by its id
def get_encrypted_password(login_id):
    conn = create_connection()
    cursor = conn.cursor()
    #here we select the password of the credential with the id equal to the parameter 'login_id'
    cursor.execute("SELECT password FROM users WHERE id=?", (login_id,))
    result = cursor.fetchone()
    conn.close()
    return result[0]

#updates a credential in the database
def update_credential(site, new_login, new_password):
    global db_file
    conn = create_connection()
    if conn is not None:
        try:
            #here we update the credential with the site equal to the parameter 'site'
            c = conn.cursor()
            c.execute("UPDATE users SET username=?, password=? WHERE site_app=?", (new_login, new_password, site))
            conn.commit()
            print(f"Credencial atualizada com sucesso para o site {site}.")
        except sqlite3.Error as e:
            print(f"Erro ao atualizar credencial: {e}")
        finally:
            conn.close()

#deletes a credential from the database
def delete_credential(login_id):
    conn = create_connection()
    cursor = conn.cursor()
    #here we delete the credential with the id equal to the parameter 'login_id'
    cursor.execute("DELETE FROM users WHERE id=?", (login_id,))
    conn.commit()
    conn.close()
