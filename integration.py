xi=2
xf=5
n=10000
h=(xf-xi)/(n-1)
xx=[ ]
yy=[ ]
for i in range(n):
	x=xi+i*h
	y=x**2
	yy.append(y)
s=yy[0]+yy[n-1]
for i in range(1,n-1):
	s=s+2*yy[i]
s=(h*s)/2
print(s)