import numpy as np
import matplotlib.pyplot as plt
MU=np.arange(1,5.8,0.00005)
X=np.zeros(96000)
Y=np.zeros(96000)
i=0
for mu in MU:
    X[i]=mu
    x=np.random.random()
    for n in range(5000):
        x=mu*x*(1-x)/(1+x)
    Y[i]=x
    i=i+1
plt.scatter(X,Y,s=0.2)
plt.xlim(1,5.8)
plt.ylim(0,1)
plt.xlabel("r")
plt.ylabel("x")
plt.title("Bifurcation Diagram for the K map - ")
plt.show()



