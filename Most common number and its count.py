a=["8158910076","9775162180","9735006595","9064650040","9775162180","7797092863","7797092863","9647431487","9064650040"]
n=len(a)
b=[]
c=[]
c1=[]
for i in range(n):
	k=0
	for j in range(n):
		if a[i]==a[j]:
			k=k+1
	b.append(k)
max=b[0]
for i in range(len(b)):
    if b[i]>=max:
        max=b[i]
for i in range(len(b)):
    if b[i]==max:
        c.append(a[i])
for element in c:
    if element not in c1:
        c1.append(element)
print("The most common numbers are ",c1,"and they are",max,"times")