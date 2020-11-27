import tkinter as tk
from tkinter import messagebox
from random import randint
from tkinter import Entry
import psycopg2
from psycopg2 import Error
from datos import *
#########################
### Ventana principal ###
#########################
gui = tk.Tk()
gui.title("Proyecto 2 Fisica 3")
gui.geometry("800x600")
gui.configure(background = "LightGreen")

label1= tk.Label(gui, text="Proyecto laboratorio Fisica 3", font=("Century", 30), pady=100, bg="LightGreen", fg="black")
label11= tk.Label(gui, text="Simulación de un espectrómetro de masas", font=("Century", 15), pady=10, bg="LightGreen", fg="black")
label1.pack()
label11.pack()


button1 = tk.Button(gui, text = "Empezar", font=("Courier", 15), command =ventanaDatos)
button1.pack(pady=10, ipadx=5)

gui.mainloop()
