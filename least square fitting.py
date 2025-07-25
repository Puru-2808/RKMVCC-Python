import numpy as np
x=[]
for i in range(40,19,-1):
    x.append(i)
yy=[0.420,0.429,0.458,0.478,0.491,0.515,0.540,0.572,0.606,0.650,0.707,0.759,0.820,0.900,1.001,1.111,1.249,1.368,1.549,1.720,1.959]
y=[]
for i in range(len(yy)):
    y1=np.log(yy[i])
    y.append(y1)
k=0
n=len(x)
for i in range(n):
    k=k+y[i]
k1=0
for i in range(n):
    k1=k1+x[i]
k2=0
for i in range(n):
    k2=k2+x[i]**2
k3=0
for i in range(n):
    k3=k3+x[i]*y[i]

m=((n*k3)-k*k1)/((n*k2)-k1**2) #slope
c1=k
c2=m*k1
c3=len(x)
c=(c1-c2)/c3

y_f=[]
for i in range(n):
    y1=m*x[i]+c
    y_f.append(np.e**y1)
import matplotlib.pyplot as plt
plt.plot(x,y_f,'-r')
plt.plot(x,yy,'.k')
plt.show()