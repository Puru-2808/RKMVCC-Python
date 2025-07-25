a=[2,5,7,6,9]
n=5
s1=0
for i in range(n):
	s1=s1+a[i]
av=s1/n
print('the avarage value is',av)
s2=0
for i in range(n):
	s2=s2+(a[i]-av)**2
std=(s2/n)**0.5
print('the standard deviation is',std)
s3=0
for i in range(n):
	s3=s3+a[i]**2
rms=(s3/n)**0.5
print('the rms value is',rms)	