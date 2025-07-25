n=5
x=[2,1,9,4,6]
max=x[0]
for i in range(n):
	if x[i]>=max:
		max=x[i]
		a=i
print('The maximum number is',max,'and its position is',a)
n=5
x=[2,1,9,4,6]
min=x[0]
for i in range(n):
	if x[i]<=min:
		min=x[i]
		a=i
print('The minimum number is',min,'and its position is',a)