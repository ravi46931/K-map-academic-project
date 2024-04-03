import numpy as np
import matplotlib.pyplot as plt

mu=float(input("Enter the value of mu : "))
N=int(input("Enter the number of iterations : "))
xx=np.zeros(N)
xx[0]=float(input("Enter the value of initial point - "))
for i in range(N-1):
    xx[i+1]=mu*xx[i]*(1-xx[i])/(1+xx[i])

for i in range(300,N-1):
    a=[xx[i],xx[i]]
    b=[xx[i],xx[i+1]]
    plt.plot(a,b,color="black")
    c=[xx[i+1],xx[i+1]]
    plt.plot(b,c,color='black')


y=np.zeros(N+1)
x=np.arange(0,1+1/N,1/N)

for i in range(N+1):
    y[i]=mu*x[i]*(1-x[i])/(1+x[i])
#plt.plot(x,y,color='black',label ="For $\mu$ = %0.5f" % mu)
plt.plot(x,y,color='black')
plt.xlim(0,1)
plt.ylim(0,1)
plt.plot(x,x,color='black')
plt.title(" K map ")
plt.xlabel("x(n)")
plt.ylabel("x(n+1)")
plt.legend()
plt.show()



#Change this code effectively
