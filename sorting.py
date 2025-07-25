x=[2,3,4,5]
n=len(x)
for i in range(n):
	for j in range(i+1,n):
		if x[i]>x[j]:
			temp=x[i]
			x[i]=x[j]
			x[j]=temp
print('increasing order is',x)
for i in range(n):
	for j in range(i+1,n):
		if x[i]<x[j]:
			temp=x[i]
			x[i]=x[j]
			x[j]=temp
print('decreasing order is',x)