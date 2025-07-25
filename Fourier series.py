def f(x):
    return x
import numpy as np
a=np.pi
xi=0
xf=2*a
n=1001
N=10
h=(xf-xi)/(n-1)
xx=[]
yy=[]
xx1=[]
yy1=[]

# a0
for i in range(1,n+1):
    x=xi+i*h
    y=f(x)
    xx.append(x)
    yy.append(y)
s=yy[0]+yy[n-1]
for i in range(1,n-1):
    s=s+2*yy[i]
    a0=(1/a)*(h/2)*s
    
# an
aa_n=[]
for i in range(1,N+1):
    y1=0
    for j in range(n):
        x1= xi+j*h
        y1+=f(x1)*np.cos(i*x1)
    an=(1/a)*h*y1
    aa_n.append(an)

# bn
bb_n=[]
for i in range(1,N+1):
    y2=0
    for j in range(n):
        x2=xi+j*h
        y2+=f(x2)*np.sin(i*x2)
    bn=(1/a)*h*y2
    bb_n.append(bn)
    
# plot
import matplotlib.pyplot as plt
xi1=0
xf1=6*a
h1=(xf1-xi1)/(n-1)
for i in range(n):
	x3=xi1+i*h1
	b=0
	for j in range(1,N+1):
		b=b+aa_n[j-1]*np.cos(j*x3)+bb_n[j-1]*np.sin(j*x3)
		y3=(a0/2)+b
	xx1.append(x3)
	yy1.append(y3)
plt.plot(xx1,yy1,'-r')
plt.grid()
plt.show()