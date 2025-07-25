import numpy as np
xi=0.5
yi=np.cos(xi)
mi=-np.sin(xi)
for i in range(4):
    x=xi-yi/mi
    y=np.cos(x)
    mf=-np.sin(x)
    xi=x
    yi=y
    mi=mf
print(x)