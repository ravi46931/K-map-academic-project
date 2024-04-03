import numpy as np
import matplotlib.pyplot as plt
e=2.6
#e=float(input("Enter the value of $\epsilon$ : "))
#mu=float(input("Enter the value of mu : "))
mu_a=(3*e-1+np.sqrt(8*e*e-8*e))/(1+e)
#N=int(input("Enter the number of iterations : "))
N=700
xx=np.zeros(N)
#xx[0]=float(input("Enter the value of initial point - "))
xx[0]=0.19
#mu = e+1+0.5
mu = e+1+0.4
#mu=mu_a+0.7
#mu=mu_a-0.5
#mu=((mu_a + e+1)/2) -0.3
#mu=5.8284
#mu=e+1
print(mu)
for i in range(N-1):
    t= xx[i] /(1+e*(1-xx[i]))
    xx[i+1]=mu*t*(1-t)/(1+t)

for i in range(0,N-1):
    a=[xx[i],xx[i]]
    b=[xx[i],xx[i+1]]
    plt.plot(a,b,color="b")
    c=[xx[i+1],xx[i+1]]
    plt.plot(b,c,color='b')


y=np.zeros(N+1)
x=np.arange(0,1+1/N,1/N)

for i in range(N+1):
    t= x[i] /(1+e*(1-x[i]))
    y[i]=mu*t*(1-t)/(1+t)
#plt.plot(x,y,color='black',label ="For $\mu$ = %0.5f" % mu)
plt.plot(x,y,color='black')
plt.xlim(0,1)
plt.ylim(0,1)
plt.plot(x,x,color='black')
#plt.title(" K map ")
plt.xlabel("x(n)")
plt.ylabel("x(n+1)")
plt.legend()
plt.show()



#Change this code effectively
