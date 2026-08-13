import tkinter as tk
from tkinter import ttk

def on_enter(event):
    print("ENTER")

def on_leave(event):
    print("LEAVE")

root = tk.Tk()
root.geometry("800x600")
frame = tk.Frame(root, bg="#240f52")
frame.pack(fill="both", expand=True)

label = tk.Label(frame, text="Raven", bg="#240f52", font=("Courier", 12, "bold"))
label.pack(pady=20)

btn1 = tk.Button(frame, text="Start Attack")
btn1.place(relx=0.5, rely=0.4, anchor="n")
btn1.lift()
btn1.bind("<Enter>", on_enter)
btn1.bind("<Leave>", on_leave)

btn2 = tk.Button(frame, text="Results History")
btn2.place(relx=0.5, rely=0.5, anchor="n")
btn2.lift()
btn2.bind("<Enter>", on_enter)
btn2.bind("<Leave>", on_leave)

btn3 = tk.Button(frame, text="Settings")
btn3.place(relx=0.5, rely=0.6, anchor="n")
btn3.lift()
btn3.bind("<Enter>", on_enter)
btn3.bind("<Leave>", on_leave)

root.mainloop()