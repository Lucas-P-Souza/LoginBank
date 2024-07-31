import data_base as db
import subprocess
import sys
import os

#this function runs the pyinstaller to create the executable file
def run_pyinstaller():
    try:
        script_dir = os.path.dirname(os.path.abspath(__file__))
        script_path = os.path.join(script_dir, "app.py")
        dist_path = os.path.join(script_dir, "dist")
        os.makedirs(dist_path, exist_ok=True)
        
        #here we run the pyinstaller to create the executable file
        subprocess.check_call(["pyinstaller", "--onefile", "--windowed", "--distpath", dist_path, script_path])
        
    except subprocess.CalledProcessError as e:
        print(f"Erro ao executar pyinstaller: {e}")
        sys.exit(1)

def main():
    
    ##run_pyinstaller()
    
    from main_window import MainWindow
    import tkinter as tk

    db.create_connection()
    db.create_table()
    
    root = tk.Tk()
    root.withdraw()

    app = MainWindow()
    app.mainloop()

if __name__ == "__main__":
    main()