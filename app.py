import data_base as db
import subprocess
import sys
import os

def run_pyinstaller():
    try:
        # Obtém o diretório atual do script
        script_dir = os.path.dirname(os.path.abspath(__file__))
        # Monta o caminho completo para o script
        script_path = os.path.join(script_dir, "app.py")
        # Define o diretório de saída para a pasta atual
        dist_path = os.path.join(script_dir, "dist")
        
        os.makedirs(dist_path, exist_ok=True)
        
        # Chama o pyinstaller com o caminho correto
        subprocess.check_call(["pyinstaller", "--onefile", "--windowed", "--distpath", dist_path, script_path])
    except subprocess.CalledProcessError as e:
        print(f"Erro ao executar pyinstaller: {e}")
        sys.exit(1)

def main():
    run_pyinstaller()

    # Resto do seu código principal aqui
    from main_window import MainWindow
    import tkinter as tk

    db.create_connection()
    db.create_table()
    
    root = tk.Tk()
    root.withdraw()  # Esconder a janela principal do Tkinter

    app = MainWindow()
    app.mainloop()

if __name__ == "__main__":
    main()