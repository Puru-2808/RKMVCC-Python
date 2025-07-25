import numpy as np
import matplotlib.pyplot as plt
from scipy import integrate

xi=-1
xf=1
yi=0
yf=0
n=10001
h=(xf-xi)/(n-1)

Ei=0
Ef=12
n1=1001
h1=(Ef-Ei)/(n1-1)

EE=[]
EE1=[]
xx=[]
yy=[]
mm=[]

for i in range(n1):
    zi=1
    yi=0
    E=Ei+i*h1
    EE.append(E)
    mi=-2*E*yi
    mm.append(mi)
    for j in range(n):
        x=xi+j*h
        z=zi+h*mm[i]
        y=yi+h*zi
        m=-2*EE[i]*y
        yi=y
        zi=z
        mm[i]=m
    xx.append(x)
    yy.append(y)

for i in range(n1-1):
    if yy[i]*yy[i+1]<0:
        EE1.append(EE[i])

for i in range(len(EE1)):
    yi = 0
    zi = 1
    mi = -2 * EE1[i] * yi

    xx = [xi]
    yy = [yi]

    for j in range(n):
        x = xi + j * h
        xx.append(x)

        yf = yi + h * zi
        yy.append(yf)

        zf = zi + h * mi
        mf = -2 * EE1[i] * yf
        
        yi=yf
        zi=zf
        mi=mf
    xx=np.array(xx)
    yy=np.array(yy)
    N=integrate.simpson(yy**2,xx)
    yy=yy/(N**0.5)

    plt.plot(xx, yy, label=f"E = {E:.3f}")

plt.xlabel("x")
plt.ylabel("y(x)")
plt.title("Solutions for Detected Energy Levels")
plt.legend()
plt.grid()
plt.show()