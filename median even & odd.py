x=[1,2,3,4]
n=len(x)
m=n%2
if m==0:
	a=(n/2)
	b=(n/2)-1
	c=x[int(a)]+x[int(b)]
	d=c/2
print(d)

#Median odd
x=[1,2,3,4,5]
n=len(x)
m=n%2
if m!=0:
	a=((n+1)/2)-1
	c=x[int(a)]
print(c)