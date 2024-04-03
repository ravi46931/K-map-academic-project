import numpy as np
import matplotlib.pyplot as plt
R=np.arange(0,4,0.00005)
X=np.zeros(200000)
Y=np.zeros(200000)
i=0
for r in R:
    X[i]=r
    x=np.random.random()
    for n in range(200):
        x=r*x*(1-x)
    Y[i]=x
    i=i+1
plt.scatter(X,Y,s=0.2)
plt.xlim(0,4)
plt.ylim(0,1)
plt.xlabel("r")
plt.ylabel("x")
plt.title("Bifurcation Diagram - ")
plt.show()