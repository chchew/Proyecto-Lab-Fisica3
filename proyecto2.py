import numpy as np
from math import pi
import matplotlib.pyplot as plt
import matplotlib.animation as matanimation
import matplotlib.lines as mlines
from celluloid import Camera
from pathlib import Path
import os.path


#====================================================================================
def getGraph(masasParticulas,cargasParticulas,nombresParticulas,voltaje):
    if len(masasParticulas)>3 or len(masasParticulas)<1 or len(masasParticulas)!=len(cargasParticulas) or len(cargasParticulas)!=len(nombresParticulas) or voltaje<0:
        return
    n=len(masasParticulas)
    V = voltaje
    d=0.03
    B=5e-3

    m1 = masasParticulas[0]
    q1 = cargasParticulas[0]
    nombre1=nombresParticulas[0]
    r1=V*m1/(q1*d*B**2)
    w1=q1*B/m1
    T1=2*pi/w1
    
    if n>=2:
        m2 = masasParticulas[1]
        q2 = cargasParticulas[1]
        nombre2=nombresParticulas[1]
        r2=V*m2/(q2*d*B**2)
        w2=q2*B/m2
        T2=2*pi/w2
        if n==3:
            m3 = masasParticulas[2]
            q3 = cargasParticulas[2]
            nombre3=nombresParticulas[2]
            r3=V*m3/(q3*d*B**2)
            w3=q3*B/m3
            T3=2*pi/w3
            
    
    if n==1:
        rmax=r1
        Tmax=T1
    elif n==2:
        rmax=max(r1,r2)
        Tmax=max(T1,T2)
    else:
        rmax=max(r1,r2,r3)
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
        plt.vlines(0,Yo,Yf,colors='k',linewidth=2)
        plt.hlines(0,Xo,Xf,colors='k',linewidth=2)
        plt.xlabel("x(m)")
        plt.ylabel("y(m)")

        if t[len(t)-1]<=T1/2:
            th1=q1*B*t/m1
        x1=r1*(np.cos(th1)-1)
        y1=-r1*np.sin(th1)
        plt.plot(x1,y1,'g',x1[len(x1)-1],y1[len(y1)-1],'ro')
        leyenda1=mlines.Line2D([],[],color='g',label=nombre1)

        if n>=2:
            if t[len(t)-1]<=T2/2:
                th2=q2*B*t/m2
            x2=r2*(np.cos(th2)-1)
            y2=-r2*np.sin(th2)
            plt.plot(x2,y2,'y',x2[len(x2)-1],y2[len(y2)-1],'ro')
            leyenda2=mlines.Line2D([],[],color='y',label=nombre2)

            if n==3:
                if t[len(t)-1]<=T3/2:
                    th3=q3*B*t/m3
                x3=r3*(np.cos(th3)-1)
                y3=-r3*np.sin(th3)
                plt.plot(x3,y3,'b',x3[len(x3)-1],y3[len(y3)-1],'ro')
                leyenda3=mlines.Line2D([],[],color='b',label=nombre3)
        if n==1:
            plt.legend(handles=[leyenda1],bbox_to_anchor=(0.4,1))
        elif n==2:
            plt.legend(handles=[leyenda1,leyenda2],bbox_to_anchor=(0.4,1))
        else:
            plt.legend(handles=[leyenda1,leyenda2,leyenda3],bbox_to_anchor=(0.4,1))
        camera.snap()
    p=os.path.join(Path(__file__).parent.absolute(),'animacion.gif')
    animacion=camera.animate()
    writergif=matanimation.PillowWriter(fps=30)
    animacion.save(p,writer=writergif)
#=====================================================================================
