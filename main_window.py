from data_viewer_frame import DatabaseViewerApp
from find_password_frame import FindPassword
from delete_frame import DeleteCredential
from insert_frame import InsertFrame
from ttkbootstrap import Style
import tkinter as tk
import os

class MainWindow(tk.Tk):
    def __init__(self):
        #it creates the main window with the title "Login bank" and the size 700x500
        #it is the window that is going to be shown when the app starts
        super().__init__()
        self.title("Login bank")
        self.geometry("700x550")
        
        #here we create the main frame when the app starts
        self.create_main_frame()
        
    def create_main_frame(self):
        #it creates the main frame
        self.main_frame = tk.Frame(self)
        self.main_frame.pack(fill=tk.BOTH, expand=True)
        
        #here we create the button to go to the insert frame
        button_insert = tk.Button(self.main_frame, text="Insert", command=self.open_insert_frame)
        button_insert.pack(pady=20)
        
        button_view = tk.Button(self.main_frame, text="View Database", command=self.open_database_viewer)
        button_view.pack(pady=20)
        
        button_find_password = tk.Button(self.main_frame, text="Find Password", command=self.open_find_password)
        button_find_password.pack(pady=20)
        
        button_delete = tk.Button(self.main_frame, text="Delete Login", command=self.open_delete_credential)
        button_delete.pack(pady=20)
        
    def open_insert_frame(self):
        #it hides the main frame
        self.main_frame.pack_forget()
        
        #here we create the insert frame
        self.insert_frame = InsertFrame(self, self.back_to_main_frame)
        self.insert_frame.pack(fill=tk.BOTH, expand=True)
        
    def open_database_viewer(self):
        #
        db_path = os.path.join(os.path.dirname(__file__), "database.db")
        self.database_viewer = DatabaseViewerApp(db_path)
        self.database_viewer.mainloop()
        
    def open_find_password(self):
        self.find_password_window = FindPassword(self)
        self.find_password_window.grab_set()
        
    def open_delete_credential(self):
        self.delete_credential_window = DeleteCredential(self)
        self.delete_credential_window.grab_set()
    
    def back_to_main_frame(self):
        #now it hides the insert frame, it will be destroyed after the user goes back to the main frame
        #it will happen because when the user click on the 'back' button
        self.insert_frame.pack_forget()
        
        #and it shows the main frame
        self.main_frame.pack(fill=tk.BOTH, expand=True)

if __name__ == "__main__":
    app = MainWindow()
    app.mainloop()
