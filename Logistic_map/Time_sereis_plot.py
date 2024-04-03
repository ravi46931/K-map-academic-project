import numpy as np
import matplotlib.pyplot as plt
r=float(input("Enter the value of r "))
x=np.zeros(150)
x[0]=0.1
for n in range(149):
    x[n+1]=r*x[n]*(1-x[n])
y=np.arange(0,150,1)
plt.plot(y,x)
plt.title("Time series plot r = %0.5f" % r)
plt.xlabel("n")
plt.ylabel("x(n)")
plt.show()