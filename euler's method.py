# by this we can see the solution of a 1st order differential equation
import matplotlib.pyplot as plt
xi=0
xf=3
yi=0
n=301
h=(xf-xi)/(n-1)
mi=2*xi               # the 1st order differential equation
xx=[]
yy=[]
xx1=[]
yy1=[]
xx.append(xi)
yy.append(yi)
for i in range(1,n):
    x=xi+i*h
    yf=yi+h*mi #in loop after that it will be yf=yf+h*mf
    yy.append(yf)
    xx.append(x)
    mf=2*x
    yi=yf
    mi=mf
# actual graph and euler graph comparision
for j in range(n):
    x1=xi+j*h
    y1=x1**2
    xx1.append(x1)
    yy1.append(y1)
plt.plot(xx1,yy1,'-r') #actual graph
plt.plot(xx,yy,'-k') #euler graph
plt.show()  