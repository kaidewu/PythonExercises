from _tkinter import *
from curses.textpad import Textbox
import tkinter as tk

app = tk.Tk()
body = tk.Label(app, width=430, height=330)
body.pack()
texto = tk.Label(app, text='Dime cuanto mides?: ')
altura = tk.Entry(app)
app.mainloop()