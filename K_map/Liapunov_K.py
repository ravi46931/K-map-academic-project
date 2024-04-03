import numpy as np
import matplotlib.pyplot as plt
MU=np.arange(1,5.8,0.0005)
X=np.zeros(9600)
Y=np.zeros(9600)
i=0
for mu in MU:
    x=np.zeros(3000)
    x[0]=np.random.random()
    for n in range(2999):
        x[n+1]=mu*x[n]*(1-x[n])/(1+x[n])
    sum=0
    for j in range(3000):
        l=abs(mu*(1-2*x[j]-x[j]*x[j])/((1+x[j])*(1+x[j])))
        sum=sum + np.log(l)
    Y[i]=sum/3000 #variation of liapunov exponentr in the direction Y
    X[i]=mu #variation of control parameter in the direction of X
    i=i+1
O=np.zeros(9600)
plt.plot(X,O)
plt.plot(X,Y,linewidth = 1)
plt.ylim(-8,1)
plt.xlim(1,5.8)

plt.title("Liapunov function - ")
plt.xlabel("$\mu$")
plt.ylabel("Liapunov exponent ($\lambda$)")
plt.show()

