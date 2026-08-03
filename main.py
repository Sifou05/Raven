from tkinter import *
import tkinter as tk

from gui.homeSC import HomeScreen


root = tk.Tk()
root.geometry("800x600") #Set Window Resolution
root.title("Raven") #Set Title
root.configure(bg='#240f52') #Set BG color

home_page = HomeScreen(root)
home_page.configure(bg='#240f52')
home_page.pack(side="bottom",fill="both", expand=True)






root.mainloop()