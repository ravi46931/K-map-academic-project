e1=1.13 # picked randomly
e2=3.7
e3=8.7
#e=float(input("Enter the value of of e :"))
import numpy as np
x=np.arange(0,1.01,0.01)
xe1=x/(1+e1*(1-x))
xe2=x/(1+e2*(1-x))
xe3=x/(1+e3*(1-x))
mu1=(3*e1-1+np.sqrt(8*e1*e1-8*e1))/(1+e1) # Bifurcation happens at this value of mu
mu2=(3*e2-1+np.sqrt(8*e2*e2-8*e2))/(1+e2)+0.65
mu3=(3*e3-1+np.sqrt(8*e3*e3-8*e3))/(1+e3)+0.2
print(mu1,mu2,mu3)
Kxe1 = mu1*xe1*(1-xe1)/(1+xe1)
Kxe2 = mu2*xe2*(1-xe2)/(1+xe2)
Kxe3 = mu3*xe3*(1-xe3)/(1+xe3)
import matplotlib.pyplot as plt
plt.plot(x,Kxe1,label="$\epsilon$ = %0.2f " % e1,linestyle='dotted',c='r')
#plt.plot(x,Kxe1,label="$\epsilon$ = %0.2f " % mu1,linestyle='dotted',c='r')
plt.plot(x,Kxe2,label="$\epsilon$ = %0.2f " % e2,linestyle='dashed',linewidth=1.5,c='r')
plt.plot(x,Kxe3,label="$\epsilon$ = %0.2f " % e3,linewidth=1.5,c='r')
plt.title("The deformed K-map ")
plt.plot(x,x,c='black')
plt.xlabel("x")
plt.ylabel("K[x]$\epsilon$")
plt.xlim(0,1)
plt.ylim(0,1)
plt.legend()
plt.show()