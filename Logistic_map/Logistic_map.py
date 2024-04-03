import numpy as np
import matplotlib.pyplot as plt
y=np.zeros(101)
x=np.arange(0,1.01,0.01)
r=float(input("Enter the value of r : "))
for i in range(101):
    y[i]=r*x[i]*(1-x[i])
plt.plot(x,y,label ="For r = %0.5f" % r)
plt.xlim(0,1)
plt.ylim(0,1)
plt.plot(x,x)
plt.title(" Logistic map ")
plt.xlabel("x")
plt.ylabel("rx(1-x)")
plt.legend()
plt.show()

