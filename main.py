import tkinter as tk
from tkinter import ttk

from gui.homeSC import HomeScreen
from gui.crackSC import CrackScreen

crack_page = None
home_page = None
root = tk.Tk()
root.geometry("800x600") #Set Window Resolution
root.title("Raven") #Set Title
root.configure(bg='#240f52') #Set BG color

def show_home_screen():
    global crack_page, home_page
    crack_page.destroy()
    home_page = HomeScreen(root, show_crack_screen)
    home_page.pack(fill="both", expand=True)

def show_crack_screen():
    global crack_page,home_page
    home_page.destroy()
    crack_page = CrackScreen(root, show_home_screen)
    crack_page.pack(fill="both", expand=True)






home_page = HomeScreen(root, show_crack_screen)
home_page.configure(bg='#240f52')
home_page.pack(side="bottom",fill="both", expand=True)






root.mainloop()
