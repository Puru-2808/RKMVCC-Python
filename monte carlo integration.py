import numpy as np
xi=0
xf=2
yi=0
yf=4
XX=[]
YY=[]
N=100000
for i in range(N):
    x=np.random.uniform(xi,xf)
    XX.append(x)
    y=np.random.uniform(yi,yf)
    YY.append(y)
k=0
for i in range(N):
    x=XX[i]
    if YY[i]<=x**2:
        k=k+1
a=(xf-xi)*(yf-yi)    # surface of the rectangle the by random points 
print((k/N)*a)

#or

# importing necessary modules 
import numpy as np
import matplotlib.pyplot as plt
import random

# defining function
def f_(x):
    return x**2

# initialization 
xi,xf=0,2
yi,yf=f_(xi),f_(xf)
n=100001

# creating array
xx=[]
yy=[]
xx1=[]
yy1=[]

# generating random points
for i in range(n):
    x=random.uniform(xi,xf)
    xx.append(x)
    y=random.uniform(yi,yf)
    yy.append(y)

# integration 
k=0
for i in range(n):
    k+=f_(xx[i])
    
int=((xf-xi)/n)*k
print(int)

# plotting 
for i in range(n):
    if yy[i]<=f_(xx[i]):
        xx1.append(xx[i])
        yy1.append(yy[i])
plt.plot(xx1,yy1,'.r')
plt.show()