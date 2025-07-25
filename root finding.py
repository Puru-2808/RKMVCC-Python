def fx(x):
	return x**3-8*x**2+19*x-12
esc=0.0001
#first root
diff=1
a=3.5
b=4.5
while diff>esc:
	x1=(a+b)/2
	res=fx(x1)
	if res>0:
		b=x1
	else:
		a=x1
		diff=abs(a-b)
#second root
diff=1
a=3.5
b=2.5
while diff>esc:
	x2=(a+b)/2
	res=fx(x2)
	if res>0:
		b=x2
	else:
		a=x2
		diff=abs(a-b)
#third root
diff=1
a=0
b=1.5
while diff>esc:
	x3=(a+b)/2
	res=fx(x3)
	if res>0:
		b=x3
	else:
		a=x3
		diff=abs(a-b)
print(x1,x2,x3)