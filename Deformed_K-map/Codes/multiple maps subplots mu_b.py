e1=1.7
e2=3.5
e3=4.75
e4=6.3
import numpy as np
x=np.arange(0,1,0.01)
xe1=x/(1+e1*(1-x))
xe2=x/(1+e2*(1-x))
xe3=x/(1+e3*(1-x))
xe4=x/(1+e4*(1-x))
mu1=(3*e1-1-np.sqrt(8*e1*e1-8*e1))/(1+e1) # Bifurcation happens at this value of mu
mu2=(3*e2-1-np.sqrt(8*e2*e2-8*e2))/(1+e2)
mu3=(3*e3-1-np.sqrt(8*e3*e3-8*e3))/(1+e3)
mu4=(3*e4-1-np.sqrt(8*e4*e4-8*e4))/(1+e4)
Kxe1 = mu1*xe1*(1-xe1)/(1+xe1)
Kxe2 = mu2*xe2*(1-xe2)/(1+xe2)
Kxe3 = mu3*xe3*(1-xe3)/(1+xe3)
Kxe4 = mu4*xe4*(1-xe4)/(1+xe4)
import matplotlib.pyplot as plt
plt.subplot(2,2,1)
plt.plot(x,Kxe1,label="$\mu$ = %0.3f" %mu1)
plt.title("At $\epsilon$  = %0.2f" %e1)
plt.plot(x,x)
plt.xlabel("x")
plt.ylabel("K([x]$\epsilon$)")
plt.legend()
plt.subplot(2,2,2)
plt.plot(x,Kxe2,label="$\mu$ = %0.3f" %mu2)
plt.title("At $\epsilon$ = %0.2f" %e2)
plt.plot(x,x)
plt.xlabel("x")
plt.ylabel("K([x]$\epsilon$)")
plt.legend()
plt.subplot(2,2,3)
plt.plot(x,Kxe3,label="$\mu$ = %0.3f" %mu3)
plt.title("At $\epsilon$ = %0.2f" %e3)
plt.plot(x,x)
plt.xlabel("x")
plt.ylabel("K([x]$\epsilon$)")
plt.legend()
plt.subplot(2,2,4)
plt.plot(x,Kxe4,label="$\mu$ = %0.3f" %mu4)
plt.title("At $\epsilon$ = %0.2f" %e4)
plt.plot(x,x)
plt.xlabel("x")
plt.ylabel("K([x]$\epsilon$)")
plt.legend()
plt.subplots_adjust(bottom=0.076, right=0.73, top=0.914, left=0.276, wspace=0.34, hspace=0.478)
plt.show()
