import tkinter as tk
from tkinter import messagebox
import numpy as np
from math import tan, cos,sin,pi
import matplotlib.pyplot as plt
import matplotlib.animation as matanimation
import matplotlib.lines as mlines
from celluloid import Camera
from pathlib import Path
import os.path


#====================================================================================
def getGraph():
    masas=[1.67e-27,9.11e-31,3.34e-27,1.17e-26,1.5e-26,9.11e-31,1.67e-27,2e-26,1.5e-26,1.84e-26]
    cargas=[1.6e-19,-1.6e-19,1.6e-19,4.8e-19,6.4e-19,1.6e-19,-1.6e-19,-9.6e-19,6.4e-19,8e-19]
    nombres =[
    "Proton",
    "Electron",
    "Nucleo de deuterio",
    "Nucleo de litio",
    "Nucleo de berilio",
    "Positron",
    "Antiproton",
    "Nucleo de carbono de antimateria",
    "Nucleo de berilio de antimateria",
    "Nucleo de boro de antimateria"]
    
    V = 120
    d=0.03
    B=5e-3
    particula1 = 0
    particula2 = 2
    particula3 = 3

    m1 = masas[particula1]
    q1 = cargas[particula1]
    m2 = masas[particula2]
    q2 = cargas[particula2]
    m3 = masas[particula3]
    q3 = cargas[particula3]
    nombre1=nombres[particula1]
    nombre2=nombres[particula2]
    nombre3=nombres[particula3]
    
    r1=V*m1/(q1*d*B**2)
    r2=V*m2/(q2*d*B**2)
    r3=V*m3/(q3*d*B**2)
    rmax=max(r1,r2,r3)

    w1=q1*B/m1
    w2=q2*B/m2
    w3=q3*B/m3


    T1=2*pi/w1
    T2=2*pi/w2
    T3=2*pi/w3
    Tmax=max(T1,T2,T3)

    Xo = -2.2*rmax
    Xf = 0.2*rmax
    Yo = -1.2*rmax
    Yf = 0.5*rmax

    fig=plt.figure()
    camera=Camera(fig)
    plt.grid(linestyle='-',linewidth=1)
    plt.xlim(Xo,Xf)
    plt.ylim(Yo,Yf)

    for i in np.linspace(0,1.1*Tmax/2,num=80):
        t=np.linspace(0,i)

        if t[len(t)-1]<=T1/2:
            th1=q1*B*t/m1
        if t[len(t)-1]<=T2/2:
            th2=q2*B*t/m2
        if t[len(t)-1]<=T3/2:
            th3=q3*B*t/m3

        x1=r1*(np.cos(th1)-1)
        x2=r2*(np.cos(th2)-1)
        x3=r3*(np.cos(th3)-1)

        y1=-r1*np.sin(th1)
        y2=-r2*np.sin(th2)
        y3=-r3*np.sin(th3)

        plt.vlines(0,Yo,Yf,colors='k',linewidth=2)
        plt.hlines(0,Xo,Xf,colors='k',linewidth=2)
        plt.xlabel("x(m)")
        plt.ylabel("y(m)")
        plt.plot(x1,y1,'g',x2,y2,'y',x3,y3,'b')
        plt.plot(x1[len(x1)-1],y1[len(y1)-1],'ro',x2[len(x2)-1],y2[len(y2)-1],'ro',x3[len(x3)-1],y3[len(y3)-1],'ro')
        leyenda1=mlines.Line2D([],[],color='g',label=nombre1)
        leyenda2=mlines.Line2D([],[],color='y',label=nombre2)
        leyenda3=mlines.Line2D([],[],color='b',label=nombre3)
        plt.legend(handles=[leyenda1,leyenda2,leyenda3],bbox_to_anchor=(0.4,1))
        camera.snap()
    p=os.path.join(Path(__file__).parent.absolute(),'animacion.gif')
    animacion=camera.animate()
    writergif=matanimation.PillowWriter(fps=30)
    animacion.save(p,writer=writergif)
#=====================================================================================
getGraph()
