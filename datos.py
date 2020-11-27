import tkinter as tk
from tkinter import messagebox
from random import randint
from tkinter import Entry
import psycopg2
from psycopg2 import Error


#####################
### Menu de datos ###
#####################
def ventanaDatos():
    
    ventanaDatos = tk.Tk()
    ventanaDatos.title("Datos")
    ventanaDatos.geometry("800x600")
    ventanaDatos.configure(background = "LightGreen")

    label1= tk.Label(ventanaDatos, text="Datos para simulacion", font=("Century", 44), pady=40, bg="LightGreen", fg="black")
    label1.pack()
   

    trash = tk.Label(ventanaDatos, text="", font=("Courier", 17), bg="LightGreen", fg="black")
    trash.pack(side=tk.TOP)

    campo2 = tk.Frame(ventanaDatos, bg = "LightGreen")
    label2 = tk.Label(campo2, text="Particula creada:", font=("Courier", 17), bg="LightGreen", fg="black")
    label2.pack(side=tk.TOP)
    
    label2 = tk.Label(campo2, text="Protones:", font=("Courier", 13), bg="LightGreen", fg="black")
    label2.pack(side=tk.LEFT, ipady = 7)
    
    usuario = tk.Text(campo2, width=12, height=1)
    usuario.pack(side = tk.LEFT)
    
    label3 = tk.Label(campo2, text="    Iones:", font=("Courier", 13), bg="LightGreen", fg="black")
    label3.pack(side=tk.LEFT, ipady = 7)
    
    usuario = tk.Text(campo2, width=12, height=1)
    usuario.pack(side = tk.LEFT)

    label2 = tk.Label(campo2, text="    Electrones:", font=("Courier", 13), bg="LightGreen", fg="black")
    label2.pack(side=tk.LEFT, ipady = 7)
    
    usuario = tk.Text(campo2, width=12, height=1)
    usuario.pack(side = tk.LEFT)

    campo2.pack(side=tk.TOP)


    label4 = tk.Label(ventanaDatos, text="", font=("Courier", 17), bg="LightGreen", fg="black")
    label4.pack(side=tk.TOP)

#
    trash = tk.Label(ventanaDatos, text="", font=("Courier", 17), bg="LightGreen", fg="black")
    trash.pack(side=tk.TOP)

    campo2 = tk.Frame(ventanaDatos, bg = "LightGreen")
    label2 = tk.Label(campo2, text="Datos de escenario:", font=("Courier", 17), bg="LightGreen", fg="black")
    label2.pack(side=tk.TOP)
    
    label2 = tk.Label(campo2, text="Voltaje:", font=("Courier", 13), bg="LightGreen", fg="black")
    label2.pack(side=tk.LEFT, ipady = 7)
    
    usuario = tk.Text(campo2, width=12, height=1)
    usuario.pack(side = tk.LEFT)

    campo2.pack(side=tk.TOP)
#

    trash = tk.Label(ventanaDatos, text="", font=("Courier", 17), bg="LightGreen", fg="black")
    trash.pack(side=tk.TOP)
    campo3 = tk.Frame(ventanaDatos, bg = "LightGreen")

    label4 = tk.Label(campo3, text="Seleccione particulas:", font=("Courier", 17), bg="LightGreen", fg="black")
    label4.pack(side=tk.TOP)

    campo3.pack(side=tk.TOP)

    trash = tk.Label(ventanaDatos, text="", font=("Courier", 17), bg="LightGreen", fg="black")
    trash.pack(side=tk.TOP)

    button1 = tk.Button(ventanaDatos, text = "Simulacion", font=("Courier", 15))
    button1.pack(pady=10, ipadx=5)

