import numpy as np
e=np.arange(1,6,0.01)
mu=(3*e-1+np.sqrt(8*e*e-8*e))/(1+e) # all the possible values of mu are equal or greater than
import matplotlib.pyplot as plt
plt.plot(e,mu,c='m')
plt.xlabel("$\epsilon$")
plt.ylabel("$\mu$")
plt.show()
