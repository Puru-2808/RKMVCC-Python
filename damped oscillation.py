import matplotlib.pyplot as plt
import numpy as np
xi=0
xi1=0
xi2=0
yi=4
yi1=4
yi2=4
xf=20
zi=0
zi1=0
zi2=0
a=3# a=alpha
w=1 # w=omega
a1=3
w1=3
a2=0.1
w2=3
n=10001
mi=-(2*a)*zi-(w**2)*yi
mi1=-(2*a1)*zi1-(w1**2)*yi1
mi2=-(2*a2)*zi2-(w2**2)*yi2
h=(xf-xi)/(n-1)
h1=(xf-xi1)/(n-1)
h2=(xf-xi2)/(n-1)
xx=[]
yy=[]
xx1=[]
yy1=[]
xx2=[]
yy2=[]
for i in range(n):
    x=xi+i*h
    zf=zi+h*mi
    yf=yi+h*zi
    mf=-(2*a)*zf-(w**2)*yf
    zi=zf
    mi=mf
    yi=yf
    xx.append(x)
    yy.append(yf)
for j in range(n):
    x1=xi1+j*h1
    zf1=zi1+h1*mi1
    yf1=yi1+h1*zi1
    mf1=-(2*a1)*zf1-(w1**2)*yf1
    zi1=zf1
    mi1=mf1
    yi1=yf1
    xx1.append(x1)
    yy1.append(yf1)
for k in range(n):
    x2=xi2+k*h2
    zf2=zi2+h2*mi2
    yf2=yi2+h2*zi2
    mf2=-(2*a2)*zf2-(w2**2)*yf2
    zi2=zf2
    mi2=mf2
    yi2=yf2
    xx2.append(x2)
    yy2.append(yf2)
plt.plot(xx,yy,'-r')
plt.plot(xx1,yy1,'-b')
plt.plot(xx2,yy2,'-k')
plt.grid()
plt.show()