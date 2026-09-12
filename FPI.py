import numpy as np
import matplotlib.pyplot as plt
from scipy import integrate

xi=-1
xf=1
yi=0
yf=0
n=10001
h=(xf-xi)/(n-1)

Ei=-35
Ef=0
n1=10001
h1=(Ef-Ei)/(n1-1)

EE=[]
EE1=[]
FF=[]
xx=[]
yy=[]
mm=[]

V0=35.0
mu=469.46
hbar=197.32698

factor=2*mu/(hbar**2)

# Energy scanning
for i in range(n1):

    zi=1
    yi=0

    E=Ei+i*h1

    EE.append(E)

    mi=-factor*(E+V0)*yi

    for j in range(n):

        x=xi+j*h

        z=zi+h*mi
        y=yi+h*zi

        m=-factor*(E+V0)*y

        yi=y
        zi=z
        mi=m

    alpha=np.sqrt(-2*mu*E)/(hbar)

    # Finite-well boundary condition
    F=zi+alpha*yi

    FF.append(F)


# Detect energy levels
for i in range(n1-1):

    if FF[i]*FF[i+1]<0:

        EE1.append(EE[i])


print("Detected energy levels:")

for E in EE1:
    print(f"E = {E:.6f} MeV")


# Calculate and plot wavefunctions
for i in range(len(EE1)):

    E=EE1[i]

    yi=0
    zi=1

    mi=-factor*(E+V0)*yi

    xx=[xi]
    yy=[yi]

    for j in range(n):

        x=xi+j*h

        yf=yi+h*zi
        yy.append(yf)

        zf=zi+h*mi
        mf=-factor*(E+V0)*yf

        yi=yf
        zi=zf
        mi=mf

        xx.append(x)

    xx=np.array(xx)
    yy=np.array(yy)

    # Normalize
    N=integrate.simpson(yy**2,x=xx)

    yy=yy/(N**0.5)

    plt.plot(xx,yy,label=f"E = {E:.3f} MeV")

plt.legend()
plt.grid()
plt.show()