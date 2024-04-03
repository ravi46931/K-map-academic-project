import numpy as np
import matplotlib.pyplot as plt
e=4.7
m_u = (3*e-1+np.sqrt(8*e*e-8*e))/(1+e)
print(m_u)
MU=np.arange(1.005,5.9,0.1)
print(len(MU))
X=np.zeros(len(MU))
Y=np.zeros(len(MU))
i=0
for mu in MU:
    x=np.zeros(3000)
    x[0]=np.random.random()
    for n in range(2999):
        xe=x[n]/(1+e*(1-x[n]))
        x[n+1]=mu*xe*(1-xe)/(1+xe)
        #x[n+1]=mu*x[n]*(1-x[n])/(1+x[n])
    sum=0
    for j in range(3000):
        xe=x[j]/(1+e*(1-x[j]))
        Dxe=(1+e)/((1+e*(1-x[j]))*(1+e*(1-x[j])))
        l=abs((mu*(1-2*xe-xe*xe)*Dxe)/((1+xe)*(1+xe)))
        sum=sum + np.log(l)
    Y[i]=sum/3000 #variation of liapunov exponentr in the direction Y
    X[i]=mu #variation of control parameter in the direction of X
    i=i+1
O=np.zeros(len(MU))
plt.plot(X,O,linewidth = 1,c='black')
plt.plot(X,Y,linewidth = 1,c='g')


#plt.ylim(-8,1)
#plt.xlim(1,5.8)

plt.title("Liapunov function - ")
plt.xlabel("$\mu$")
plt.ylabel("Liapunov exponent ($\lambda$)")
plt.show()

