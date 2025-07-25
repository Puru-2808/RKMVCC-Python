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

for j in range(len(tt)):
        xi=400*10**(-9)       #wavelength range
        xf=4000*10**(-9)
        n=1001
        xx=np.linspace(xi,xf,n)
        yy=[]
        for i in range(len(xx)):
            y=(8*np.pi*h*c/(xx[i]**5))*(1/(e**((h*c)/(xx[i]*k*tt[j]))-1))
            yy.append(y)
        plt.plot(xx,yy)
        a=np.trapz(yy,xx)
        print("The Stefan's constant for",tt[j],"is",a/(tt[j]**4))
plt.legend(["T1=1800","T2=2200",
"T3=2600","T4=3000"],loc="upper right")
plt.xlabel('Wavelength')
plt.ylabel('Energy Spectral Density')
plt.title("Plack's Distribution Law")
plt.grid()
plt.show()