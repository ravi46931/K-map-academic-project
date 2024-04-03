import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
x1=np.arange(0,1.01,0.01)
x2=np.arange(0,1.01,0.01)
y1=np.zeros(101)
y2=np.zeros(101)
z=np.zeros(101)
mu1=4.7
mu2=0.9
for i in range(101):
    y1[i]= mu1*x1[i]*(1-x1[i])/(1+x1[i])
    z[i]=x1[i]

for i in range(101):
    y2[i]= mu2*x2[i]*(1-x2[i])/(1+x2[i])
    z[i]=x2[i]

plt.plot(x1,y1,color="b",label= "$\mu$ = %0.3f" %mu1)
plt.plot(x2,y2,color="b",label= "$\mu$ = %0.3f" %mu2,linestyle='dashed')
plt.plot(z,x1,color="black")
plt.xlim(0,1)
plt.ylim(0,1)
plt.xlabel("$x$")
plt.ylabel("$K(x)}$")
plt.title("The K-map")
plt.legend()
plt.show()