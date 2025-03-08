from tkinter import *
import time

tk = Tk()
tk.title("Notepad")
tk.geometry("500x400")
tk.configure(bg='#A8A7A7')

def save():
    a = open("text.txt", "w")
    a.write(f"{textbox.get("1.0", "end-1c")}")

textbox = Text(tk, height=400, width=300, bg="white")
savebut = Button(tk, text="Kaydet", height=1, width=7, command=lambda:save())

savebut.pack()
textbox.pack()

tk.mainloop()