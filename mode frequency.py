import numpy as np
n=7
a=[2,2,5,2,2,9,2]
nr=int(9+1)
b=np.zeros(nr)
for i in range(n):
	b[a[i]]=b[a[i]]+1
print('given set of numbers','\n',a)
max=b[0]
for i in range(nr):
	if max<b[i]:
		max=b[i]
		p=i
print('mode is',p,'\n','frequency is',max)