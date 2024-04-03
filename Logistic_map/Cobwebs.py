import numpy as np
import matplotlib.pyplot as plt

r=float(input("Enter the value of r : "))
N=int(input("Enter the number of iterations : "))
xx=np.zeros(N)
xx[0]=float(input("Enter the value of initial point - "))
for i in range(N-1):
    xx[i+1]=r*xx[i]*(1-xx[i])

for i in range(N-1):
    a=[xx[i],xx[i]]
    b=[xx[i],xx[i+1]]
    plt.plot(a,b)
    c=[xx[i+1],xx[i+1]]
    plt.plot(b,c,color='green')

y=np.zeros(N+1)
x=np.arange(0,1+1/N,1/N)

for i in range(N+1):
    y[i]=r*x[i]*(1-x[i])
plt.plot(x,y,label ="For r = %0.5f" % r)
plt.xlim(0,1)
plt.ylim(0,1)
plt.plot(x,x)
plt.title(" Logistic map ")
plt.xlabel("x(n)")
plt.ylabel("x(n+1)")
plt.legend()
plt.show()