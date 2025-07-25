import matplotlib.pyplot as plt
import numpy as np
e=np.e
xi=-0.9   # these are boundary conditions
yi=-1
xf=0.9
yf=1
n=101
h=(xf-xi)/(n-1)
zz=[]
xx=[]
yy=[]
yy1=[]
mm=[]
zi=5.6

# for 3rd
l=3
mi=((2*xi)-(l*(l+1))*yi)/(1-xi**2)
for j in range(n):
          x=xi+j*h
          zf=zi+h*mi
          y=yi+h*zi
          mf=((2*x)-(l*(l+1))*y)/(1-x**2)
          zi=zf
          mi=mf
          yi=y
          xx.append(x)
          yy.append(y)
plt.plot(xx,yy)
plt.grid()
plt.show()