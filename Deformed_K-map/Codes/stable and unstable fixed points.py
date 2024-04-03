import numpy as np
import matplotlib.pyplot as plt
#e=float(input("Enter the value of epsilon greater than 1:"))
e=3.4
mu_min=(3*e-1+np.sqrt(8*e*e-8*e))/(1+e)
MU=np.arange(mu_min+0.000001,mu_min+4,0.009)
X1=(-(1-e-2*e*e+MU*(1+e))+np.sqrt((1-e-2*e*e+MU*(1+e))*(1-e-2*e*e+MU*(1+e))-4*e*(1+e)*(e-1)*(1+e-MU)))/(2*e*(e-1))
X2=(-(1-e-2*e*e+MU*(1+e))-np.sqrt((1-e-2*e*e+MU*(1+e))*(1-e-2*e*e+MU*(1+e))-4*e*(1+e)*(e-1)*(1+e-MU)))/(2*e*(e-1))
#xx=list(map(lambda x, y: x * y, X1, X1))
#l=1+e*(1-X1)
dKxe1 = np.zeros(len(MU))
dKxe2 = np.zeros(len(MU))
print(len(dKxe1))
x=X1
for i in range(len(MU)):
    dKxe1[i]=(MU[i]*(1+e)*(x[i]*x[i]+2*x[i]*(1+e*(1-x[i]))-(1+e*(1-x[i]))*(1+e*(1-x[i]))))/((1+e*(1-x[i]))*(1+e*(1-x[i]))*(1+x[i]+e*(1-x[i]))*(1+x[i]+e*(1-x[i])))
x=X2
for i in range(len(MU)):
    dKxe1[i]=(MU[i]*(1+e)*(x[i]*x[i]+2*x[i]*(1+e*(1-x[i]))-(1+e*(1-x[i]))*(1+e*(1-x[i]))))/((1+e*(1-x[i]))*(1+e*(1-x[i]))*(1+x[i]+e*(1-x[i]))*(1+x[i]+e*(1-x[i])))

for i in range(len(MU)):
   if abs(dKxe1[i])>1:
        plt.scatter(MU[i],X1[i],c='r',s=0.2)
   else:
        plt.scatter(MU[i],X1[i],c='b',s=0.2)

for i in range(len(MU)):
    if abs(dKxe2[i])>1:
        plt.scatter(MU[i],X2[i],c='r',s=0.2)
    else:
        plt.scatter(MU[i],X2[i],c='b',s=0.2)
print(X2)

#plt.plot(MU,X1)
#plt.plot(MU,X2)
plt.xlabel("$\mu$")
plt.ylabel("fixed points")
plt.ylim(0,1)
plt.legend()
plt.show()