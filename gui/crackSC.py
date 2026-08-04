import tkinter as tk
from tkinter import filedialog

class CrackScreen(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent, bg="#240f52")
        self.parent = parent
        self.create_widget()

    def create_widget(self):
        self.Browse_button = tk.Button(self, text="Browse Hash/File", command=self.browse_file)
        self.Browse_button.place(relx=0.5,rely=0.4, anchor="n")
        self.Browse_button.lift()


    def browse_file(self):
        file_path = filedialog.askopenfilename(title="Choose attack mode:", filetypes=(("Text Files", "*.txt"),))
        if file_path:
            print(f"Selected file: {file_path}")
        else:
            print("No file selected")




