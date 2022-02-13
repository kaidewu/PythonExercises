# Import everything from tkinter
from tkinter import *
import math
# Create a tkinter window
app = Tk()

# Winodow dimension
app.geometry('530x330')

# Title of tkinter window
app.wm_title('IMC Calculator')

# Defining a function that calculate the IMC
def calculate():
    result = float(weight.get()) / (float(height.get()) ** 2)
    imc.set(result)

height = StringVar()
weight = StringVar()
imc = StringVar()

# Create a label and entry for height
height_label = Label(app, text='Tell your height in meters (ej. 1.80):', font=('calibre', 10, 'bold'))
height_entry = Entry(app, textvariable=height, font=('calibre', 10, 'normal'))

# Create a label and entry for weight
weight_label = Label(app, text='Tell your weight in kg (ej. 80):', font=('calibre', 10, 'bold'))
weight_entry = Entry(app, textvariable=weight, font=('calibre', 10, 'normal'))

# Create a label and entry for the result
imc_label = Label(app, text='Result:', font=('calibre', 10, 'bold'))
imc_entry = Entry(app, textvariable=imc, font=('calibre', 10, 'normal'))

# Accept button
calculate_button = Button(app, text='calculate', command=calculate)

# Position using grid
height_label.grid(row=3, column=0)
height_entry.grid(row=3, column=1)
weight_label.grid(row=4, column=0)
weight_entry.grid(row=4, column=1)
imc_label.grid(row=5, column=0)
imc_entry.grid(row=5, column=1)
calculate_button.grid(row=6, column=1)

app.mainloop()