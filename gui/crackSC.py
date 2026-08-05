import tkinter as tk
from tkinter import filedialog

class CrackScreen(tk.Frame):
    def __init__(self, parent, on_goBack):
        super().__init__(parent, bg="#240f52")
        self.parent = parent
        self.on_goBack = on_goBack
        self.create_widget()

    def create_widget(self):
        self.Browse_button = tk.Button(self, text="Browse Hash/File", command=self.browse_file)
        self.Browse_button.place(relx=0.5,rely=0.4, anchor="n")
        self.Browse_button.lift()

        self.back_icon = tk.PhotoImage(file=r"assets/back-to-home.png")
        self.Back_button = tk.Button(self, image=self.back_icon, command=self.on_goBack)
        self.Back_button.place(relx=0.03, rely=0.010, anchor="n")
        self.Back_button.lift()



    def browse_file(self):
        file_path = filedialog.askopenfilename(title="Choose attack mode:", filetypes=(("Text Files", "*.txt"),))
        if file_path:
            print(f"Selected file: {file_path}")
        else:
            print("No file selected")




