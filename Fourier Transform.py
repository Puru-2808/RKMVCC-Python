import matplotlib.pyplot as plt
import numpy as np
from scipy import integrate

# previous function
xi = -20
xf = 20
n = 1001
h = (xf-xi)/(n-1)

xx=[]
yy=[]
XX1=[]
yy1=[]

for i in range (n):
    x=xi+i*h
    xx.append(x)
    y = np.sin(3*x) + 0.6*np.sin(7*x) + 0.3*np.sin(12*x)
    yy.append(y)

# transformed fuction
ti=-20
tf=20
h1=(tf-ti)/(n-1)
tt=[]
aa=[]


for i in range(n):
    t=ti+i*h1
    tt.append(t)
    

# transformation
for i in range (len(tt)):
    ff=[]
    for k in range(n):
        f = np.exp(-1j*tt[i]*xx[k])*yy[k]
        ff.append(f)
    a=(integrate.simpson(ff,x=xx))/((2*np.pi)**0.5)
    aa.append(a)

plt.figure(figsize=(10,4))

plt.subplot(1,2,1)
plt.plot(xx, yy, 'k')
plt.title("Time-domain signal")

plt.subplot(1,2,2)
plt.plot(tt, np.abs(aa), 'r')
plt.title("Frequency spectrum")

plt.tight_layout()
plt.show()