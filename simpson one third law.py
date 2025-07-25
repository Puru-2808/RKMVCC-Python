xi=2
xf=4
n=500
h=(xf-xi)/(n-1)
xx=[ ]
yy=[ ]
for i in range(0,n,1):
	x=xi+i*h
	y=x**2
	xx.append(x)
	yy.append(y)
c=yy[0]+yy[n-1]
for i in range(1,n-1,2):
    c=c+4*yy[i]
s=c
for i in range(2,n-1,2):
    s=s+2*yy[i]
d=(h/3)*s
print(d)