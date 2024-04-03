import numpy as np
#e=float(input("Enter the value of epsilon greater than 1:"))
e=4.9
mu_min=(3*e-1+np.sqrt(8*e*e-8*e))/(1+e)
MU=np.arange(mu_min+0.000001,mu_min+4,0.01)
X1=(-(1-e-2*e*e+MU*(1+e))+np.sqrt((1-e-2*e*e+MU*(1+e))*(1-e-2*e*e+MU*(1+e))-4*e*(1+e)*(e-1)*(1+e-MU)))/(2*e*(e-1))
X2=(-(1-e-2*e*e+MU*(1+e))-np.sqrt((1-e-2*e*e+MU*(1+e))*(1-e-2*e*e+MU*(1+e))-4*e*(1+e)*(e-1)*(1+e-MU)))/(2*e*(e-1))
import matplotlib.pyplot as plt
plt.plot(MU,X1)
plt.plot(MU,X2)
plt.xlabel("$\mu$")
plt.ylabel("fixed points")
plt.ylim(0,1)
plt.show()