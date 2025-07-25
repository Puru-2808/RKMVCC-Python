import numpy as np

xi=0
xf=1
yi=0
yf=0
n=10001
h=(xf-xi)/(n-1)

Ei=0
Ef=20
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
    if abs(yy[i])<=0.001:
        EE1.append(EE[i])

print(EE1)