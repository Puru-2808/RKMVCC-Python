import matplotlib.pyplot as plt
import numpy as np
p= np.pi
a= 0
b= 2*p
n= 101
N=13
h= (b-a)/(n-1)
xx=[]
yy=[]

for j in range(n):
    x= a+j*h
    xx.append(x)
    s= xx[j]
    t=xx[j]
    for i in range(1,N):
        t= (-t)* ((xx[j]**2) /(2*i*(2*i +1)))
        s= s+t
    yy.append(s)
    
ss=np.sin(xx)
print(ss)
plt.grid()
plt.plot(xx,yy,".r",xx, ss,'k.')
plt.show()