import numpy as np
import matplotlib.pyplot as plt

xi,xf=-2,2    # range
yi=np.e**(2)+np.e**(-2)
yf=np.e**(2)+np.e**(-2)
n=700         # number of points
h=(xf-xi)/(n-1)
xx=[]
yy=[]
cc=[]
dd=[]
ee=[]
rr=[]

for i in range(1,n-1):
    x=xi+i*h        #starting from 1 to n-1 because there is no d(xi) and d(xf)
    p=np.e**x               #p(x)
    q=(np.e**(-x))-1     #q(x)
    r=np.e**(2*x)+np.e**(-2*x)    #r(x)
    c=1-((h/2)*p)
    d=((h**2)*q)-2
    e=1+((h/2)*p)
    xx.append(x)
    dd.append(d)
    cc.append(c)
    ee.append(e)
    rr.append(r)

a=[]
a=np.zeros([n-2,n-2])    #null matrix
for i in range(n-2):
    a[i][i]=dd[i]                  #dd[0] is d1
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

c=[]
c=np.linalg.solve(a,b)   #solution
print(c)

xx1=[]
for i in range(n):
    x1=xi+i*h
    y=(np.e**x1)+(np.e**(-x1))
    xx1.append(x1)
    yy.append(y)


plt.plot(xx,c,'-r')      # graph using finite difference method
plt.plot(xx1,yy,'-.k')   # actual solution graph
plt.show()