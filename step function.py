def f1(x):
    return -1
def f2(x):
    return 1
import numpy as np
a=np.pi
xi1=-a
xf1=0
xi2=0
xf2=a
n=1001
N=100
h1=(xf1-xi1)/(n-1)
h2=(xf2-xi2)/(n-1)
xx=[]
yy=[]
xx1=[]
yy1=[]

# a0
for i in range(1,n+1):
    x=xi1+i*h1
    y=f1(x)
    xx.append(x)
    yy.append(y)
s=yy[0]+yy[n-1]
for i in range(1,n-1):
    s=s+2*yy[i]
    a0_1=(1/a)*(h1/2)*s
for i in range(1,n+1):
    x1=xi2+i*h1
    y1=f2(x1)
    xx1.append(x1)
    yy1.append(y1)
s1=yy1[0]+yy1[n-1]
for i in range(1,n-1):
    s1=s1+2*yy1[i]
    a0_2=(1/a)*(h2/2)*s1
a0=a0_1+a0_2    
    
# an
aa_n=[]
for i in range(1,N+1):
    y2=0
    y3=0
    for j in range(n):
        x2= xi1+j*h1
        y2+=f1(x2)*np.cos(i*x2)
        x3= xi2+j*h2
        y3+=f2(x3)*np.cos(i*x3)
    an_1=(1/a)*h1*y2         
    an_2=(1/a)*h2*y3
    an=an_1+an_2  
    aa_n.append(an)  
        
# bn
bb_n=[]
for i in range(1,N+1):
    y4=0
    y5=0
    for j in range(n):
        x4=xi1+j*h1
        y4+=f1(x4)*np.sin(i*x4)
        x5=xi2+j*h2
        y5+=f2(x5)*np.sin(i*x5)
    bn_1=(1/a)*h1*y4   
    bn_2=(1/a)*h2*y5
    bn=bn_1+bn_2    
    bb_n.append(bn)
         
    
# plot
import matplotlib.pyplot as plt
xi3=0
xf3=6*a
h3=(xf3-xi3)/(n-1)
xx2=[]
yy2=[]
for i in range(n):
	x6=xi3+i*h3
	b=0
	for j in range(1,N+1):
		b=b+aa_n[j-1]*np.cos(j*x6)+bb_n[j-1]*np.sin(j*x6)
		y6=(a0/2)+b
	xx2.append(x6)
	yy2.append(y6)
print("a0: ",a0,'\n',"an: ",aa_n,'\n',"bn: ",bb_n)
plt.plot(xx2,yy2,'-r')
plt.grid()
plt.show()