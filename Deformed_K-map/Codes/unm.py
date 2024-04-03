import numpy as np
import matplotlib.pyplot as plt

mu=np.arange(0, 6, 0.02)

x=0.62
b=x+2+mu
p=1+x-mu*(1-x)

ep=(-b-`np.sqrt(b*b-4*p))/(2*(1-x))

print(ep)

plt.plot(mu,ep)
plt.show()

