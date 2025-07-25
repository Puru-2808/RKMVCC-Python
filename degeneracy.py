aa=[]
for i in range(0,10):
    for j in range(0,10):
        for k in range(0,10):
            if i+j+k==9:
                a=i,j,k
                print(a)
                aa.append(a)
print(len(aa))