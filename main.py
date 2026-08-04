import tkinter as tk

from gui.homeSC import HomeScreen
from gui.crackSC import CrackScreen

root = tk.Tk()
root.geometry("800x600") #Set Window Resolution
root.title("Raven") #Set Title
root.configure(bg='#240f52') #Set BG color

def show_crack_screen():
    home_page.destroy()
    crack_page = CrackScreen(root)
    crack_page.pack(fill="both", expand=True)


home_page = HomeScreen(root, show_crack_screen)
home_page.configure(bg='#240f52')
home_page.pack(side="bottom",fill="both", expand=True)






root.mainloop()