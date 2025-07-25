import matplotlib.pyplot as plt
import numpy as np

e = np.e
xi = 0
yi = 1
xf = 1
yf = 2
n = 101
h = (xf - xi) / (n - 1)
xx = []
yy = []
yy1 = []

zi = 10
mi = 2*zi-yi

for j in range(n):
    x = xi + j * h
    zf = zi + h * mi
    y = yi + h * zi
    y1 = (1 + (2/e - 1)*x)*e**x
    mf = 2*zf-y
    zi = zf
    mi = mf
    yi = y
    xx.append(x)
    yy.append(y)
    yy1.append(y1)
    
c = yy[n - 1] - yf
while abs(c) >= 0.001:
    yy2 = []  
    for i in range(len(yy)):
        y2 = (yy[i] + yy1[i]) / 2
        yy2.append(y2)
        yy[i]=yy2[i]
    c = yy[n - 1] - yf

plt.plot(xx, yy)
plt.plot(xx, yy1, '.-r')
plt.show()