import numpy as np
import matplotlib.pyplot as plt

xi,xf=-0.5,4
yi=0
yf=9*(np.e**(-4))
n=22
h=(xf-xi)/(n-1)
xx=[]
yy=[]
cc=[]
dd=[]
ee=[]
rr=[]

for i in range(1,n-1):
    x=xi+i*h
    p=2
    q=1
    r=0
    c=1-((h/2)*p)
    d=((h**2)*q)-2
    e=1+((h/2)*p)
    xx.append(x)
    dd.append(d)
    cc.append(c)
    ee.append(e)
    rr.append(r)

a=[]
a=np.zeros([n-2,n-2])
for i in range(n-2):
    a[i][i]=dd[i]           #dd[0] is d1
for i in range(n-3):
    a[i][i+1]=ee[i]
for i in range(n-3):
    a[i+1][i]=cc[i+1]
print(a)

b=[]
b=np.zeros([n-2,1])
b[0][0]=((h**2)*rr[0])-(cc[0]*yi)
for i in range(1,n-3):
    b[i][0]=(h**2)*rr[i]
b[n-3][0]=((h**2)*rr[n-3])-(ee[n-3]*yf)
print(b)

c=np.linalg.solve(a,b)
print(c)


xx1=[]
for i in range(n):
    x1=xi+i*h
    y=((2*x1)+1)*(np.e**(-x1))
    xx1.append(x1)
    yy.append(y)
ss=[]
NN=[]
N=n-2
ee=[]
e=0
for i in range(N):
    e=e+(c[i]-yy[i+1])**2
    ee.append(e)
for i in range(N):
    f=((1/(i+1))*ee[i])**0.5
    ss.append(f)
    NN.append(i)
plt.plot(NN,ss,'-r')
plt.show()