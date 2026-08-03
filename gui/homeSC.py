import tkinter as tk


banner = r"""
    ____                       
   / __ \____ __   _____  ____ 
  / /_/ / __ `/ | / / _ \/ __ \
 / _, _/ /_/ /| |/ /  __/ / / /
/_/ |_|\__,_/ |___/\___/_/ /_/ 

"""


class HomeScreen(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent, bg="#240f52")
        self.parent = parent
        self.create_widget()

    def create_widget(self):
        self.title_label = tk.Label(
            self,
            text=banner.strip('\n'),
            justify="left",
            bg = "#240f52",
            font=("Courier", 12, "bold")

        )
        self.title_label.pack(pady=20)
        self.Start_button = tk.Button(self, text="Start Attack", command=self.destroy)  # Attack Button
        self.Start_button.place(relx=0.5, rely=0.4, anchor="n")
        self.Start_button.lift()

        self.Results_button = tk.Button(self, text="Results History", command=self.destroy)  # Attack Button
        self.Results_button.place(relx=0.5, rely=0.5, anchor="n")
        self.Results_button.lift()

        self.Settings_button = tk.Button(self, text="Settings", command=self.destroy)  # Attack Button
        self.Settings_button.place(relx=0.5, rely=0.6, anchor="n")
        self.Settings_button.lift()

        self.Start_button.bind("<Enter>", self.on_enter)
        self.Start_button.bind("<Leave>", self.on_leave)

        self.Results_button.bind("<Enter>", self.on_enter)
        self.Results_button.bind("<Leave>", self.on_leave)

        self.Settings_button.bind("<Enter>", self.on_enter)
        self.Settings_button.bind("<Leave>", self.on_leave)

    def on_enter(self,event):
        event.widget.config(background="#2ecc71", foreground="white")




    def on_leave(self, event):
        # Restores original background color when mouse leaves
        event.widget.config(background='#3498db', foreground='white')


