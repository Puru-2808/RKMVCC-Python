import numpy as np

xi=-5
xf=5
yi=0
yf=0
n=10001
h=(xf-xi)/(n-1)

Ei=0
Ef=2
n1=1001
h1=(Ef-Ei)/(n1-1)

EE=[]
EE1=[]
xx=[]
xx1=[]
yy=[]
yy1=[]
mm=[]
mm1=[]

for i in range(n1):
    xi=-5
    zi=1
    yi=0
    E=Ei+i*h1
    EE.append(E)
    mi=-2*(E-(0.5*xi**2))*yi
    mm.append(mi)
    for j in range(n):
        x=xi+j*h
        z=zi+h*mm[i]
        y=yi+h*zi
        m=-2*(EE[i]-(0.5*x**2))*y
        yi=y
        zi=z
        mm[i]=m
    xx.append(x)
    yy.append(y)

for i in range(n1-1):
    if yy[i]*yy[i+1]<0:
        EE1.append(EE[i])

# for ground state
mi0=-2*(EE1[0]-0.5*xi**2)*yi
zi1=1
for j in range(n):
        x1=xi+j*h
        z1=zi1+h*mi0
        y1=yi+h*zi1
        m1=-2*(EE1[0]-0.5*x1**2)*y1
        yi=y1
        mi0=m1
        zi1=z1
        xx1.append(x1)
        yy1.append(y1)

#for 1st excited state
mi1=-2*(EE1[1]-0.5*xi**2)*yi
zi2=1
for j in range(n):
        x2=xi+j*h
        z2=zi2+h*mi1
        y2=yi+h*zi2
        m2=-2*(EE1[1]-0.5*x2**2)*y2
        yi=y2
        mi1=m2
        zi2=z2
        xx2.append(x2)
        yy2.append(y2)    

plt.plot(xx1,yy1,'-r')
plt.plot(xx2,yy2,'-b')
plt.grid()
plt.show()