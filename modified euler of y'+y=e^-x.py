import matplotlib.pyplot as plt
import numpy as np
xi=0
xf=4
yi=0
n=1000
a=np.e
mi=a**(-xi)-(xi*a**(-xi))
h=(xf-xi)/(n-1)
xx=[]
yy=[]
for i in range(1,n):
    x=xi+i*h
    mf=a**(-x)-(x*a**(-x))
    y=yi+(h/2)*mi+(h/2)*mf
    yi=y
    mi=mf
    xx.append(x)
    yy.append(y)
plt.plot(xx,yy,'-k')
plt.grid()
plt.show()