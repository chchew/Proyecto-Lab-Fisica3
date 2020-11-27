import tkinter as tk
from tkinter import ttk
from tkinter import *
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
#Crear Particula
    campo2 = tk.Frame(ventanaDatos, bg = "LightGreen")
    label2 = tk.Label(campo2, text="Crear partícula:", font=("Courier", 17), bg="LightGreen", fg="black")
    label2.pack(side=tk.TOP)
    
    label2 = tk.Label(campo2, text="Protones:", font=("Courier", 13), bg="LightGreen", fg="black")
    label2.pack(side=tk.LEFT, ipady = 7)
    
    entry5 = tk.Text(campo2, width=12, height=1)
    entry5.pack(side = tk.LEFT)
    
    label3 = tk.Label(campo2, text="    Neutrones:", font=("Courier", 13), bg="LightGreen", fg="black")
    label3.pack(side=tk.LEFT, ipady = 7)
    
    entry6 = tk.Text(campo2, width=12, height=1)
    entry6.pack(side = tk.LEFT)

    label2 = tk.Label(campo2, text="    Electrones:", font=("Courier", 13), bg="LightGreen", fg="black")
    label2.pack(side=tk.LEFT, ipady = 7)
    
    entry7 = tk.Text(campo2, width=12, height=1)
    entry7.pack(side = tk.LEFT)

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
    
    entry8 = tk.Text(campo2, width=12, height=1)
    entry8.pack(side = tk.LEFT)

    campo2.pack(side=tk.TOP)
#

    trash = tk.Label(ventanaDatos, text="", font=("Courier", 17), bg="LightGreen", fg="black")
    trash.pack(side=tk.TOP)
    campo3 = tk.Frame(ventanaDatos, bg = "LightGreen")

    label4 = tk.Label(campo3, text="Seleccione las particula:", font=("Courier", 17), bg="LightGreen", fg="black")
    label4.pack(side=tk.TOP)
    
    #particulas
    CheckVar1 = IntVar()
    CheckVar2 = IntVar()
    CheckVar3 = IntVar()
    CheckVar4 = IntVar()
    CheckVar5 = IntVar()
    
    C1 = Checkbutton(campo3, text = "Proton", variable = CheckVar1, \
                 onvalue = 1, offvalue = 0, height=5, \
                 width = 20, bg="LightGreen")
    C1.pack(side=tk.LEFT, ipady = 7)

    C2 = Checkbutton(campo3, text = "Positron", variable = CheckVar2, \
                 onvalue = 1, offvalue = 0, \
                 width = 20, bg="LightGreen")
    
    C2.pack(side=tk.LEFT, ipady = 7)
    
    C3 = Checkbutton(campo3, text = "Antiproton", variable = CheckVar3, \
                 onvalue = 1, offvalue = 0,\
                 width = 20, bg="LightGreen")
    C3.pack(side=tk.LEFT, ipady = 7)
    
    C4 = Checkbutton(campo3, text = "Nucleo de deuterio", variable = CheckVar4, \
                 onvalue = 1, offvalue = 0,\
                 width = 20, bg="LightGreen")
    C4.pack(side=tk.LEFT, ipady = 7)
    
    C5 = Checkbutton(campo3, text = "Nucleo de litio", variable = CheckVar5, \
                 onvalue = 1, offvalue = 0,\
                 width = 20, bg="LightGreen")
    C5.pack(side=tk.LEFT, ipady = 7)
    
    campo3.pack(side=tk.TOP)

    button1 = tk.Button(ventanaDatos, text = "Simulacion", font=("Courier", 15))
    button1.pack(pady=10, ipadx=5)

    def registrarUsuario():
        protones = entry5.get()
        neutrones = entry6.get()
        electrones = entry7.get()
        voltaje = entry8.get()

    def valueCheckBox():
        ch1 = C1.get()
        ch2 = C2.get()
        ch3 = C3.get()
        ch4 = C4.get()
        ch5 = C5.get()
ventanaDatos()
