a=1
b=2
c=3
d=(b**2)-(4*a*c)
if d>=0:
	e=(-b)+(d**0.5)
	r1=e/(2*a)
	f=(-b)-(d**0.5)
	r2=f/(2*a)
	print('roots are real')
	print(r1,'\n',r2)
else:
	r=(-b)/(2*a)
	d=-d
	i=(d**0.5)/(2*a)
	print('roots are imaginary')
	print(r,i)
	print(r,-i)