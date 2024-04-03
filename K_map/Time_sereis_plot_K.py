import numpy as np
import matplotlib.pyplot as plt
mu=float(input("Enter the value of mu -  "))
x=np.zeros(100)
x[0]=float(input("Enter the initial value - "))
for n in range(99):
    x[n+1]=mu*x[n]*(1-x[n])/(1+x[n])
y=np.arange(0,100,1)
plt.plot(y,x,marker='*',markerfacecolor='blue')
plt.title("Time series plot r = %0.5f" % mu)
plt.xlabel("n")
plt.ylabel("x(n)")
plt.xlim(-0.5,100)
plt.ylim(0,1)
plt.show()
print(x[60])
print(x[61])
print(x[62])



















