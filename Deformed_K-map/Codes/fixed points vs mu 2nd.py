import numpy as np
e2=5.8
e1=2.65
e3=4.5
e4=5.7
#e5=3.5
#e6=4.2
#e=[e1,e2,e3,e4,e5,e6]
e=[e1,e2]
o=np.arange(0,1.5,0.5)
print(len(o))
mu_min=[0]*2
MU=[0]*2
X1=[0]*2
X2=[0]*2
l=np.zeros(2)
for i in range(2):
    mu_min[i]=(3*e[i]-1+np.sqrt(8*e[i]*e[i]-8*e[i]))/(1+e[i])
    l[i]=mu_min[i]-0.02
    MU[i]= np.arange(0,mu_min[i]+7,0.01)
    X1[i]=(-(1-e[i]-2*e[i]*e[i]+MU[i]*(1+e[i]))+np.sqrt((1-e[i]-2*e[i]*e[i]+MU[i]*(1+e[i]))*(1-e[i]-2*e[i]*e[i]+MU[i]*(1+e[i]))-4*e[i]*(1+e[i])*(e[i]-1)*(1+e[i]-MU[i])))/(2*e[i]*(e[i]-1))
    X2[i]=(-(1-e[i]-2*e[i]*e[i]+MU[i]*(1+e[i]))-np.sqrt((1-e[i]-2*e[i]*e[i]+MU[i]*(1+e[i]))*(1-e[i]-2*e[i]*e[i]+MU[i]*(1+e[i]))-4*e[i]*(1+e[i])*(e[i]-1)*(1+e[i]-MU[i])))/(2*e[i]*(e[i]-1))
import matplotlib.pyplot as plt
for i in range(2):
    t=i+1
    plt.subplot(2,2,t)
    plt.plot(MU[i],X1[i],c='b')
    plt.plot(MU[i],X2[i],c='b',linestyle='dashed')
    u=[e[i]+1,e[i]+1,e[i]+1]
    k=[l[i],l[i],l[i]]
    #plt.plot(k,o,linewidth=0.6,c='k')
    plt.plot(u,o,linewidth=0.6,c='k')
    plt.title("At $\epsilon$ = %0.2f " % e[i])
    plt.xlabel("$\mu$")
    plt.ylabel("fixed points")
    plt.ylim(0,1)
    plt.xlim(0,l[i]+7.02)
plt.subplots_adjust(bottom=0.15, right=0.728, top=0.81, left=0.24, wspace=0.398, hspace=0.51)
plt.show()