import numpy as np
import matplotlib.pyplot as plt
def calculate_exponent(n):
    if n==0:
        return 1
    return 2*calculate_exponent(n-1)
n= int(input("Enter the value of n -"))
val=calculate_exponent(n)
vals=calculate_exponent(n-1)
for i in range(vals):
    x=np.arange(2*i/val,((2*i+1)/val)+0.01,0.01)
    y=val*x-2*i
    plt.plot(x,y)
    plt.xlim(0,1)
    plt.ylim(0,1)
    xx=np.arange((2*i+1)/val,((2*i+2)/val)+0.01,0.01)
    yy=2*(i+1) - val*xx
    plt.plot(xx,yy)
    plt.xlim(0,1)
    plt.ylim(0,1)
plt.show()