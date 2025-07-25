import numpy as np
import matplotlib.pyplot as plt
n=1000
a=np.pi
xi=-6*a
xf=6*a
h=(xf-xi)/(n-1)
xx=[]
yy=[]
for i in range(n):
	x=xi+i*h
	b=np.sin(x)
	y=10*((b**2)/(x**2))
	xx.append(x)
	yy.append(y)
plt.plot(xx,yy,'-k')
plt.show()