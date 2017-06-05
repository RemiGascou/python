#Sine LERP 2D
from math import *
import numpy as np
import matplotlib.pyplot as plt

def SineLERP(x, y):
    LERP_precision = 2
    LERP_x, LERP_y = [],[]

    for old_x in x:
        for new_x in np.linspace(0, 1, 2+LERP_precision):
            LERP_x.append(old_x + new_x)
    print(LERP_x)
    
    for old_y in y:
        for new_x in np.linspace(0, 1, 2+LERP_precision):
            LERP_y.append(old_y*cos(new_x))
    
    return LERP_x,LERP_y


x,y = [0,1,2,3,4,5],[1,0,1,0,1,0]



plt.plot(x,y,color = 'red')
LERPx, LERPy = SineLERP(x,y)
plt.plot(LERPx, LERPy,color = 'blue')

plt.show()