import numpy as np
import matplotlib.pyplot as plt

h=1
w=1
k=1
ti=0.1
tf=5
n=500
h1=(tf-ti)/(n-1)

ee=[]
for i in range(n):
    e=(i+0.5)*h*w
    ee.append(e)

tt=[]
ss1=[]
z=[]
fluc=[]
e_avg=[]
ss3=[]
for j in range(n):
    t=ti+j*h1
    tt.append(t)
    s1=0
    s2=0
    s3=0
    for i in range(n):
        s1+=ee[i]*np.exp(-ee[i]/(k*t))
    ss1.append(s1)
    for i in range(n):
        s2+=np.exp(-ee[i]/(k*t))
    z.append(s2)
    e_avg.append(ss1[j]/z[j])
    for i in range(n):
         s3+=((ee[i]**2)*np.exp(-ee[i]/(k*t)))
    ss3.append(s3)
    fluc.append(((ss3[j]/z[j])-(ss1[j]/z[j])**2)/(k*t**2))

plt.plot(tt,fluc)
plt.plot(tt,z)
plt.plot(tt,e_avg)
plt.show()