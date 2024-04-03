import numpy as np
import matplotlib.pyplot as plt
R=np.arange(3,4,0.001)
X=np.zeros(1000)
Y=np.zeros(1000)
i=0
for r in R:
    x=np.zeros(2000)
    x[0]=np.random.random()
    for n in range(1999):
        x[n+1]=r*x[n]*(1-x[n])
    sum=0
    for j in range(2000):
        l=abs(r*(1-2*x[j]))
        sum=sum + np.log(l)
    Y[i]=sum/2000 #variation of liapunov exponentr in the direction Y
    X[i]=r #variation of control parameter in the direction of X
    i=i+1
O=np.zeros(1000)
plt.plot(X,O)
plt.plot(X,Y,linewidth = 1)
plt.ylim(-1,1)
plt.xlim(3,4)

plt.title("Liapunov function - ")
plt.xlabel("r")
plt.ylabel("liapunov exponent")
plt.show()

