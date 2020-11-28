import tkinter as tk
from tkinter import ttk
from tkinter import *
from random import randint
from tkinter import Entry
import psycopg2
from psycopg2 import Error
from proyecto2 import getGraph

nombres=["Proton","Partícula alfa","Nucleo de tritio","Nucleo de Carbono-12","Nucleo de Carbono-14","Nucleo de Uranio-238","Nucleo de Uranio-235"]
masas=[1.67e-27,6.68e-27,5.01e-27,2.004e-26,2.338e-26,3.9746e-25,3.9245e-25]
cargas=[1.6e-19,3.2e-19,1.6e-19,9.6e-19,9.6e-19,1.472e-17,1.472e-17]

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
    
    entry5 = tk.Entry(campo2, width=12)
    entry5.pack(side = tk.LEFT)
    
    label3 = tk.Label(campo2, text="    Neutrones:", font=("Courier", 13), bg="LightGreen", fg="black")
    label3.pack(side=tk.LEFT, ipady = 7)
    
    entry6 = tk.Entry(campo2, width=12)
    entry6.pack(side = tk.LEFT)

    label2 = tk.Label(campo2, text="    Electrones:", font=("Courier", 13), bg="LightGreen", fg="black")
    label2.pack(side=tk.LEFT, ipady = 7)
    
    entry7 = tk.Entry(campo2, width=12)
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
    
    entry8 = tk.Entry(campo2, width=12)
    entry8.pack(side = tk.LEFT)

    campo2.pack(side=tk.TOP)
#

    trash = tk.Label(ventanaDatos, text="", font=("Courier", 17), bg="LightGreen", fg="black")
    trash.pack(side=tk.TOP)
    campo3 = tk.Frame(ventanaDatos, bg = "LightGreen")

    label4 = tk.Label(campo3, text="Seleccione las particula:", font=("Courier", 17), bg="LightGreen", fg="black")
    label4.pack(side=tk.TOP)
    
    #particulas
    CheckVar1 = tk.IntVar(ventanaDatos)
    CheckVar2 = tk.IntVar(ventanaDatos)
    CheckVar3 = tk.IntVar(ventanaDatos)
    CheckVar4 = tk.IntVar(ventanaDatos)
    CheckVar5 = tk.IntVar(ventanaDatos)
    CheckVar6 = tk.IntVar(ventanaDatos)
    CheckVar7 = tk.IntVar(ventanaDatos)
    CheckVar8 = tk.IntVar(ventanaDatos)

    
    
    C1 = tk.Checkbutton(campo3, text = nombres[0], variable = CheckVar1, \
                 onvalue = 1, offvalue = 0, height=5, \
                 width = 20, bg="LightGreen")
    C1.pack(side=tk.LEFT, ipady = 7)

    C2 = Checkbutton(campo3, text = nombres[1], variable = CheckVar2, \
                 onvalue = 1, offvalue = 0, \
                 width = 20, bg="LightGreen")
    
    C2.pack(side=tk.LEFT, ipady = 7)
    
    C3 = Checkbutton(campo3, text = nombres[2], variable = CheckVar3, \
                 onvalue = 1, offvalue = 0,\
                 width = 20, bg="LightGreen")
    C3.pack(side=tk.LEFT, ipady = 7)
    
    C4 = Checkbutton(campo3, text = nombres[3], variable = CheckVar4, \
                 onvalue = 1, offvalue = 0,\
                 width = 20, bg="LightGreen")
    C4.pack(side=tk.LEFT, ipady = 7)
    
    C5 = Checkbutton(campo3, text = nombres[4], variable = CheckVar5, \
                 onvalue = 1, offvalue = 0,\
                 width = 20, bg="LightGreen")
    C5.pack(side=tk.LEFT, ipady = 7)

    C6 = Checkbutton(campo3, text = nombres[5], variable = CheckVar6, \
                 onvalue = 1, offvalue = 0,\
                 width = 20, bg="LightGreen")
    C6.pack(side=tk.LEFT, ipady = 7)

    C7 = Checkbutton(campo3, text = nombres[6], variable = CheckVar7, \
                 onvalue = 1, offvalue = 0,\
                 width = 20, bg="LightGreen")
    C7.pack(side=tk.LEFT, ipady = 7)

    C8 = Checkbutton(campo3, text = "Partícula costumizada", variable = CheckVar8, \
                 onvalue = 1, offvalue = 0,\
                 width = 20, bg="LightGreen")
    C8.pack(side=tk.LEFT, ipady = 7)
    
    campo3.pack(side=tk.TOP)

    def valueCheckBox():
        ch1 = CheckVar1.get()
        ch2 = CheckVar2.get()
        ch3 = CheckVar3.get()
        ch4 = CheckVar4.get()
        ch5 = CheckVar5.get()
        ch6 = CheckVar6.get()
        ch7 = CheckVar7.get()
        ch8 = CheckVar8.get()
        return [ch1,ch2,ch3,ch4,ch5,ch6,ch7],ch8
    def graficar():
        bools,iscustom=valueCheckBox()
        mas=[]
        car=[]
        nom=[]
        for i in range(7):
            if bools[i]:
                mas.append(masas[i])
                car.append(cargas[i])
                nom.append(nombres[i])
        if iscustom:
            p=int(entry5.get())
            n=int(entry6.get())
            e=int(entry7.get())
            masa=1.67e-27*(p+n)+9.11e-31*e
            carga=1.6e-19*(p-e)
            mas.append(masa)
            car.append(carga)
            nom.append("Partícula custom")
        voltaje=float(entry8.get())
        getGraph(mas,car,nom,voltaje)
    button1 = tk.Button(ventanaDatos, text = "Simulacion", font=("Courier", 15),command=graficar)
    button1.pack(pady=10, ipadx=5)