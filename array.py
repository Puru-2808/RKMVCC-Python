import numpy as np
p=np.pi
xi=-p
xf=p
n=256
h=(xf-xi)/(n-1)
xx=[ ]
yy=[ ]
for i in range(n):
	  x=xi+i*h
	  y=np.sin(x)
	  xx.append(x)
	  yy.append(y)
print(xx,yy)