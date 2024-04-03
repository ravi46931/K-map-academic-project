import numpy as np
import matplotlib.pyplot as plt
def calculate_exponent(n):
    if n==0:
        return 1
    return 2*calculate_exponent(n-1)
n= int(input("Enter the value of n -"))
val=calculate_exponent(n)
for i in range(val):
    x=np.arange(i/val,((i+1)/val)+0.01,0.01)
    y=val*x-i
    plt.plot(x,y)
    plt.xlim(0,1)
    plt.ylim(0,1)
plt.show()