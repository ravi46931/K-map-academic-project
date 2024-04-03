import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
x=np.arange(0,1.01,0.01)
y=np.zeros(101)
z=np.zeros(101)
mu=4.7
for i in range(101):
    y[i]= mu*x[i]*(1-x[i])/(1+x[i])
    z[i]=x[i]
plt.plot(x,y,color="b")
plt.plot(z,x,color="black")
plt.xlim(0,1)
plt.ylim(0,1)
plt.xlabel("$x$")
plt.ylabel("$K(x)}$")
plt.title("THe K-map")
plt.legend()
plt.show()