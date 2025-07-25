import numpy as np
import matplotlib.pyplot as plt
n=1000
a=np.pi
xi=-4*a
xf=4*a
h=(xf-xi)/(n-1)
xx=[]
yy=[]
for i in range(n):
	x=xi+i*h
	b=np.sin(x)
	c=10*b
	d=np.sin(c)
	y=5*((d**2)/c**2)
	xx.append(x)
	yy.append(y)
plt.plot(xx,yy,'-k')
plt.show()