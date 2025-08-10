import matplotlib.pyplot as plt
import numpy as np
from scipy import integrate

# previous function
xi = -100
xf = 100
n = 1001
h = (xf-xi)/(n-1)

xx=[]
yy=[]

for i in range (n):
    x=xi+i*h
    xx.append(x)
    y= np.exp(-x**2)
    yy.append(y)

# transformed fuction
ti=xi
tf=xf

tt=[]
aa=[]


for i in range(n):
    t=ti+i*h
    tt.append(t)
    

# transformation
for i in range (len(tt)):
    ff=[]
    for k in range(n):
        f = np.exp(-1j*tt[i]*xx[k])*yy[k]
        ff.append(f)
    a=integrate.simpson(ff,x=xx)/((2**0.5)*np.pi)
    aa.append(a)

plt.plot(xx,yy,'-k')
plt.plot(tt,np.real(aa),'-r')
plt.show()