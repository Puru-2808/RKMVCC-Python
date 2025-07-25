import matplotlib.pyplot as plt
import numpy as np
xi=1
yi=1
xf=3
zi=1
n=10001
mi=-2*yi+3*zi
h=(xf-xi)/(n-1)
xx=[]
yy=[]
xx1=[]
yy1=[]
xx.append(xi)
yy.append(yi)
for i in range(1,n):
    x=xi+i*h
    zf=zi+h*mi
    yf=yi+h*zi
    mf=-2*yf+3*zf
    zi=zf
    mi=mf
    yi=yf
    xx.append(x)
    yy.append(yf)
for j in range(n):
    x1=xi+j*h
    e=np.e
    y1=((1/e)*(e**x1))
    xx1.append(x1)
    yy1.append(y1)
plt.plot(xx,yy,'-o')
plt.plot(xx1,yy1,'.-k')
plt.show()