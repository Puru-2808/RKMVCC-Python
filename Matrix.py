a=[[1,1,3,5,6,23],[1,2,3,4,5,19],[1,1,1,1,1,5],[1,1,1,3,1,11],[1,1,1,1,5,13]]
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
    print("x%d=%f"%(i,xx1[i]))