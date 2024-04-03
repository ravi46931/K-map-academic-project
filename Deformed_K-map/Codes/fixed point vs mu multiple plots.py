import numpy as np
e1=1.0
e2=1.6
e3=2.0
e4=2.8
e5=3.5
e6=4.2
e=[e1,e2,e3,e4,e5,e6]
mu_min=[0]*6
MU=[0]*6
X1=[0]*6
X2=[0]*6
for i in range(6):
    mu_min[i]=(3*e[i]-1+np.sqrt(8*e[i]*e[i]-8*e[i]))/(1+e[i])
    MU[i]= np.arange(mu_min[i]+0.000001,mu_min[i]+4,0.01)
    X1[i]=(-(1-e[i]-2*e[i]*e[i]+MU[i]*(1+e[i]))+np.sqrt((1-e[i]-2*e[i]*e[i]+MU[i]*(1+e[i]))*(1-e[i]-2*e[i]*e[i]+MU[i]*(1+e[i]))-4*e[i]*(1+e[i])*(e[i]-1)*(1+e[i]-MU[i])))/(2*e[i]*(e[i]-1))
    X2[i]=(-(1-e[i]-2*e[i]*e[i]+MU[i]*(1+e[i]))-np.sqrt((1-e[i]-2*e[i]*e[i]+MU[i]*(1+e[i]))*(1-e[i]-2*e[i]*e[i]+MU[i]*(1+e[i]))-4*e[i]*(1+e[i])*(e[i]-1)*(1+e[i]-MU[i])))/(2*e[i]*(e[i]-1))
import matplotlib.pyplot as plt
for i in range(6):
    t=i+1
    plt.subplot(3,2,t)
    plt.plot(MU[i],X1[i])
    plt.plot(MU[i],X2[i])
    plt.title("At e = %0.2f " % e[i])
    plt.xlabel("$\mu$")
    plt.ylabel("fixed points")
    plt.ylim(0,1)
plt.subplots_adjust(bottom=0.076, right=0.73, top=0.914, left=0.276, wspace=0.34, hspace=0.478)
plt.show()