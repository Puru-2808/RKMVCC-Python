#Solution of Legendre Differential Eqn
#(1-x²)y'' - 2xy' + l(l+1)y=0
#BC- y(-1)=-1 , y(1)=1

import numpy as np
import matplotlib.pyplot as plt

def f(x,y,z,l):
	return (2*x*z-l*(l+1)*y)/(1-x**2)  #dz/dx

def soln(x,y,ypi,l):
	xx,yy=[],[]
	xx.append(x)
	yy.append(y)
	z=ypi
	for i in range(1,n-1):
		x=xi+i*h
		ya=y
		y=y+h*z
		z=z+h*f(x,ya,z,l)
	
		xx.append(x)
		yy.append(y)
		
	return xx,yy
	
#3rd Legendre Polynomial
xi,xf=-1,1
yi,yf=-1,1
n=10000
h=(xf-xi)/(n-1)

x=xi
y=yi
ypi=-10
ypi1,ypi2=-10,10
k=500
d=(ypi2-ypi1)/(k-1)

for i in range(0,k):
	ypi+=d
	pp=soln(x,yi,ypi,3)
	xx,yy=pp[0],pp[1]
	if abs(yf-yy[-1])<=0.005:
		plt.plot(xx,yy)

#4th Legendre Polynomial
xi,xf=-1,1
yi,yf=1,1
n=10000
h=(xf-xi)/(n-1)

x=xi
y=yi
ypi=-10
ypi1,ypi2=-10,10
k=500
d=(ypi2-ypi1)/(k-1)

for i in range(0,k):
	ypi+=d
	qq=soln(x,yi,ypi,4)
	mm,nn=qq[0],qq[1]
	if abs(yf-nn[-1])<=0.005:
		plt.plot(mm,nn)

plt.title('Legendre Polynomials')
plt.axhline()
plt.axvline()
plt.xlabel('x$\\rightarrow$')
plt.ylabel('P(x)$\\rightarrow$')
plt.show()