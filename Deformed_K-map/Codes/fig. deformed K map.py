import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
x=np.arange(0,1.01,0.01)
y=np.zeros(101)
z=np.zeros(101)
mu=4.5
epl=0.001
for i in range(101):
    val=(x[i])/(1+epl*(1-x[i]))
    y[i]= mu*val*(1-val)/(1+val)
    z[i]=x[i]
plt.plot(x,y,color="black")
plt.plot(z,x,color="black")
plt.xlim(0,1)
plt.ylim(0,1)
plt.xlabel("$x_n$")
plt.ylabel("$Deformed K(x)}$")
plt.legend()
plt.show()






