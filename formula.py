import numpy as np
from math import sin , cos , pi

#مختصات محیط دایره
def mohit_dayere_mokhtasat(n):
    l=[]
    gam=2*pi/n
    for j in range(n):
        x=sin(j*gam)
        y=cos(j*gam)
        l.append(np.array( [x,y,0]))
    return l
l=mohit_dayere_mokhtasat(4)
print()
print(l[1]*2)