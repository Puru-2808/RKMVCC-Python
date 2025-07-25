import numpy as np

h=6.626*10**(-34)
k=1.38*10**(-23)
c=3*10**8

TT=[1200,1400,1600,1800]
pp=[]
for j in range(len(TT)):
    xi=400*10**(-9)
    xf=4000*10**(-9)
    n=1001
    h1=(xf-xi)/(n-1)
    xx=[]
    yy=[]
    for i in range(n):
        x=xi+i*h1
        xx.append(x)
        y=((2*h*c**2)/(x**5))*(1/(np.e**((h*c)/(x*k*TT[j]))-1))
        yy.append(y)
    max=yy[0]
    for i in range(n):
        if yy[i]>=max:
            max=yy[i]
            d=i
    print(xx[d]*TT[j])