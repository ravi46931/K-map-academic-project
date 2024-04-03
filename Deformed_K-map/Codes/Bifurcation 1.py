# Edit it
import numpy as np
import matplotlib.pyplot as plt
e=0.8 # fixed this value, change according to need
mu = (3*e-1+np.sqrt(8*e*e-8*e))/(1+e)
print(mu)
MU=np.arange(5,5.6,0.0000075)
print(len(MU))
X=np.zeros(len(MU))
Y=np.zeros(len(MU))
i=0
for mu in MU:
    X[i]=mu
    x=np.random.random()
    for n in range(5000):
        xe=x/(1+e*(1-x))
        x=mu*xe*(1-xe)/(1+xe)
    Y[i]=x
    i=i+1
plt.scatter(X,Y,s=0.2)
min=min(mu,2)
max=max(mu,2)
#plt.xlim(min,max)
#plt.xlim(-5,10)
#plt.ylim(-1,2)
plt.xlabel("mu")
plt.ylabel("x")
plt.title("Bifurcation Diagram for the deformed K map at e = %0.3f " % e)
plt.show()



