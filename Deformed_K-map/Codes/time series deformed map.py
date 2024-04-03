import numpy as np
import matplotlib.pyplot as plt
e=2.6
#e=float(input("Enter the value of $\epsilon$ : "))
#mu=float(input("Enter the value of mu : "))
mu_a=(3*e-1+np.sqrt(8*e*e-8*e))/(1+e)
#xx[0]=float(input("Enter the value of initial point - "))
mu=2.2
#mu = e+1-0.5
#mu = e+1+0.4
mu=mu_a+0.7
mu=mu_a-0.5
mu=((mu_a + e+1)/2) -0.3
#mu=5.8284
#mu=5.3489
mu=5.313
print(mu)

x=np.zeros(100)
x[0]=0.69
#x[0]=float(input("Enter the initial value - "))
for n in range(99):
    t= x[n] /(1+e*(1-x[n]))
    x[n+1]=mu*t*(1-t)/(1+t)
y=np.arange(0,100,1)
plt.plot(y,x,marker='*',markerfacecolor='blue')
#plt.title( "At $\epsilon$ = %0.2f" % e)
plt.xlabel("No. of iterations")
plt.ylabel("x(n)")
plt.xlim(-0.5,100)
plt.ylim(0,1)
plt.legend()
plt.show()
print(x[60])
print(x[61])
print(x[62])
