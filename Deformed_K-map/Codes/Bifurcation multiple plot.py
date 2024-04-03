import numpy as np
import matplotlib.pyplot as plt
e1=5.8
mu1 = (3*e1-1+np.sqrt(8*e1*e1-8*e1))/(1+e1)
print(mu1)
e2=2.6
mu2 = (3*e2-1+np.sqrt(8*e2*e2-8*e2))/(1+e2)
print(mu2)
MU=np.arange(3,5.4,0.00004)
print(len(MU))
X=np.zeros(len(MU))
Y1=np.zeros(len(MU))
Y2=np.zeros(len(MU))
i=0
for mu in MU:
    X[i]=mu
    x1=np.random.random()
    x2=np.random.random()
    for n in range(5000):
        xe1=x1/(1+e1*(1-x1))
        x1=mu*xe1*(1-xe1)/(1+xe1)
        xe2=x2/(1+e2*(1-x2))
        x2=mu*xe2*(1-xe2)/(1+xe2)
    Y1[i]=x1
    Y2[i]=x2
    i=i+1
plt.scatter(X,Y1,s=0.2,c='r',label="$\epsilon$1 = %0.2f " % e1)
plt.scatter(X,Y2,s=0.2,c='g',label="$\epsilon$2 = %0.2f " % e2)
min=min(mu,2)
max=max(mu,2)
#plt.xlim(min,max)
#plt.xlim(-5,10)
#plt.ylim(-1,2)
plt.xlabel("mu")
plt.ylabel("x")
plt.legend()
plt.title("Bifurcation Diagram for the deformed K map " )
plt.show()



