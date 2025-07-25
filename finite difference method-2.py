import numpy as np


xi,xf=-2,2
yi=np.e**(2)+np.e**(-2)
yf=np.e**(2)+np.e**(-2)
print(yi,yf)
N=700
n=N-2 #5
h=(xf-xi)/(n-1)
xx=[]
yy=[]
cc=[]
dd=[]
ee=[]
rr=[]



for i in range(1,n+1):
    x=xi+i*h
    p=np.e**x
    q=(np.e**(-x))-1
    r=np.e**(2*x)+np.e**(-2*x)
    c=1-((h/2)*p)
    d=((h**2)*q)-2
    e=1+((h/2)*p)
    xx.append(x)
    dd.append(d)
    cc.append(c)
    ee.append(e)
    rr.append(r)
print("rr2=",rr[1])
print("cc1=",cc[0])
print("rr5=",rr[4])
print("ee5=",ee[4])
print
a=[]
a=np.zeros([n,n])
for i in range(n):
    a[i][i]=dd[i]           #dd[0] is d1
for i in range(n-1):
    a[i][i+1]=ee[i]
for i in range(n-1):
    a[i+1][i]=cc[i+1]
print(a)

b=[]
b=np.zeros([n,1])
b[0][0]=((h**2)*rr[0])-(cc[0]*yi)
for i in range(1,n-1):
    b[i][0]=(h**2)*rr[i]
b[n-1][0]=((h**2)*rr[n-1])-(ee[n-1]*yf)

print(b)

c=[]
c=np.linalg.solve(a,b)
print(c)

xx1=[]
h1=(xf-xi)/(N-1)
for i in range(N):
    x1=xi+i*h1
    y=(np.e**x1)+(np.e**(-x1))
    xx1.append(x1)
    yy.append(y)

import matplotlib.pyplot as plt
plt.plot(xx,c,'-r')
plt.plot(xx1,yy,'-k')
plt.show()