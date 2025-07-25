# importing modules
import matplotlib.pyplot as plt
import numpy as np

# Physical constants
h=6.62607015*10**(-34)  # Planck's constant
k=1.380649*10**(-23)   # Boltzmann constant
c=3*10**8        # Speed of light in vacuum

p=np.pi
e=np.e
tt=[1800,2200,2600,3000]   #temperature

tt1=[]
tt2=[]
pp=[]

for j in range(len(tt)):
        xi=400*10**(-9)       #wavelength range
        xf=4000*10**(-9)
        n=1001
        xx=np.linspace(xi,xf,n)
        yy=[]
        for i in range(len(xx)):
            y=(2*h*(c**2)/(xx[i]**5))*(1/(e**((h*c)/(xx[i]*k*tt[j]))-1))
            yy.append(y)
        p=np.trapz(yy,xx)
        pp.append(p)

# slope
s=np.polyfit(np.log(tt),np.log(pp),1)
slope=s[0]
print("Slope of log(P) vs log(T) is ",slope)

#plotting
plt.plot(np.log(tt),np.log(pp),'-r',label=f'slope = {slope: .2f}')
plt.grid()
plt.title("verification of stefan's law")
plt.xlabel("Temperature(K)")
plt.ylabel("Total radiated power")
plt.legend()
plt.show()