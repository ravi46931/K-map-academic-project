import numpy as np
import matplotlib.pyplot as plt
e=[1.01,1.2,1.7,2.2,2.6,3.1,3.8,4.2,4.7,5.3,5.8]
mu_inf=[5.2260,5.2262,5.2340,5.2456,5.2555,5.2688,5.2884,5.2992,5.3144,5.3292,5.3427]
print(len(e),len(mu_inf))
plt.plot(e,mu_inf)
plt.xlabel('$\epsilon$')
plt.ylabel('$\mu_2^{\infty}$')
plt.show()