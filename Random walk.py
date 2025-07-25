import numpy as np
import matplotlib.pyplot as plt
from scipy.special import comb

N=50   # steps
n=1001    # no of trials
q=0.5     # probability of going right side

final_pos=np.zeros(n)
for i in range(n):
    steps=np.random.choice([-1,1], size=N, p=[q,1-q])
    final_pos[i]=np.sum(steps)

x_values=np.arange(-N,N+1,2)
hist,_=np.histogram(final_pos, bins=np.arange(-N-1,N+2,2), density=True)


k_values=(x_values+N)//2
p_theo=comb(N,k_values)*(q**(k_values))*(1-q)**(N-k_values)


aa=[]
cc=[]
for i in range(1,N+1):
    a=np.log10(i)
    aa.append(a)
    final_pos=np.zeros(n)
    for j in range(n):
        steps=np.random.choice([-1,1], size=i, p=[q,1-q])
        final_pos[j]=np.sum(steps)
    b=0
    for k in range(n):
        b+=final_pos[k]**2
    c=(b/n)**0.5
    cc.append(np.log10(c))

plt.bar(x_values,hist)           # plot any single graph using "#" before code
plt.plot(x_values,p_theo)
plt.plot(aa,cc)
plt.show()