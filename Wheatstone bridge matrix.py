a=[[60,10,20,0],[40,10,10,0],[0,20,30,-20]]
n=len(a)
for m in range(0,n-2+1):
    for i in range(m+1,n-1+1):
         k=a[i][m]/a[m][m]
         for j in range(m,n+1):
             a[i][j]=a[i][j]-a[m][j]*k
for i in range(n):
    print(a[i])
print("this is row echelon form")
xi=a[n-1][n]/a[n-1][n-1]
xx=[]
xx.append(xi)
for j in range(2,n+1):
    m=0
    for k in range(1,j-1+1):
        m=m+a[n-j][n-k]*xx[k-1]
    x=(1/a[n-j][n-j])*(a[n-j][n]-m)
    xx.append(x)
xx1=[]
for i in range(len(xx)-1,-1,-1):
    x1=xx[i]
    xx1.append(x1)
print("and the solution is: ")
for i in range(n):
    print("I%d=%f"%(i,xx1[i]))
print(xx1[1]-xx1[2])