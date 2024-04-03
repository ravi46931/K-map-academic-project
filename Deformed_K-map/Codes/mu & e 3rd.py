import numpy as np
e=np.arange(-5,-1,0.01)
mumin=(3*e-1-np.sqrt(8*e*e-8*e))/(1+e)
 # all the possible values of mu lies in this interval for 3 fixed points
mumax=(3*e-1+np.sqrt(8*e*e-8*e))/(1+e)
import matplotlib.pyplot as plt
plt.plot(e,mumin,label="$\mu_b$",linestyle='dashed',c='b')
plt.plot(e,mumax,label="$\mu_a$",c='b')
plt.xlabel("$\epsilon$")
plt.ylabel("$\mu$")
plt.legend()
#plt.title("The graph between mu and e ")
plt.show()
