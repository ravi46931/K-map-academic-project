import numpy as np
import matplotlib.pyplot as plt
MU=np.arange(1,5.8,0.001)
X=np.zeros(4800)
Y=np.zeros(4800)
i=0
for mu in MU:
    x=np.zeros(2000)
    x[0]=np.random.random()
    for n in range(1999):
        x[n+1]=mu*x[n]*(1-x[n])/(1+x[n])
    sum=0
    for j in range(2000):
        l=abs(mu*(1-2*x[j]-x[j]*x[j])/((1+x[j])*(1+x[j])))
        sum=sum + np.log(l)
    Y[i]=sum/2000 #variation of liapunov exponentr in the direction Y
    X[i]=mu #variation of control parameter in the direction of X
    i=i+1
O=np.zeros(4800)
plt.plot(X,O,linestyle='dashed')
plt.plot(X,Y,linewidth = 1)
plt.ylim(-8,1)
plt.xlim(1,5.8)

plt.title("Liapunov function - ")
plt.xlabel("r")
plt.ylabel("liapunov exponent")



"""
XX=np.zeros(4700)
YY=np.zeros(4700)
i=0
for r in MU:
    XX[i]=r
    x=np.random.random()
    for n in range(500):
        x=r*x*(1-x)/(1+x)
    YY[i]=x
    i=i+1
plt.scatter(XX,YY,s=0.2)

plt.show()
"""
"""
for i in range(470):
    if Y[i] <=0 and Y[i] > -0.01:
        print(X[i])
#Modify this code
"""

M=np.arange(1,5.8,0.00005)
XX=np.zeros(96000)
YY=np.zeros(96000)
i=0
for mu in M:
    XX[i]=mu
    x=np.random.random()
    for n in range(5000):
        x=mu*x*(1-x)/(1+x)
    YY[i]=x
    i=i+1
plt.scatter(XX,YY,s=0.2)
plt.show()



