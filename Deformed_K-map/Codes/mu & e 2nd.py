import numpy as np
e=np.arange(1,6,0.01)
mu=(3*e-1-np.sqrt(8*e*e-8*e))/(1+e) # all the possible values of mu are equal or less than
import matplotlib.pyplot as plt
plt.plot(e,mu,c='g')
plt.xlabel("$\epsilon$")
plt.ylabel("$\mu$")
#plt.title("The graph between mu and e ")
plt.show()
