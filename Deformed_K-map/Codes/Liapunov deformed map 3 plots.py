import numpy as np
import matplotlib.pyplot as plt
e1=1.2
e2=3.1
e3=4.7
m_u1 = (3*e1-1+np.sqrt(8*e1*e1-8*e1))/(1+e1)
print(m_u1)
m_u2 = (3*e2-1+np.sqrt(8*e2*e2-8*e2))/(1+e2)
print(m_u2)
m_u3 = (3*e3-1+np.sqrt(8*e3*e3-8*e3))/(1+e3)
print(m_u3)
MU=np.arange(1.005,5.9,0.004)
print(len(MU))
X=np.zeros(len(MU))
Y1=np.zeros(len(MU))
Y2=np.zeros(len(MU))
Y3=np.zeros(len(MU))
i=0
for mu in MU:
    x1=np.zeros(3000)
    x2=np.zeros(3000)
    x3=np.zeros(3000)
    x1[0]=np.random.random()
    x2[0]=np.random.random()
    x3[0]=np.random.random()
    for n in range(2999):
        xe1=x1[n]/(1+e1*(1-x1[n]))
        x1[n+1]=mu*xe1*(1-xe1)/(1+xe1)
        xe2=x2[n]/(1+e2*(1-x2[n]))
        x2[n+1]=mu*xe2*(1-xe2)/(1+xe2)
        xe3=x3[n]/(1+e3*(1-x3[n]))
        x3[n+1]=mu*xe3*(1-xe3)/(1+xe3)
        #x[n+1]=mu*x[n]*(1-x[n])/(1+x[n])
    sum1=0
    sum2=0
    sum3=0
    for j in range(3000):
        xe1=x1[j]/(1+e1*(1-x1[j]))
        Dxe1=(1+e1)/((1+e1*(1-x1[j]))*(1+e1*(1-x1[j])))
        l1=abs((mu*(1-2*xe1-xe1*xe1)*Dxe1)/((1+xe1)*(1+xe1)))
        xe2=x2[j]/(1+e2*(1-x2[j]))
        Dxe2=(1+e2)/((1+e2*(1-x2[j]))*(1+e2*(1-x2[j])))
        l2=abs((mu*(1-2*xe2-xe2*xe2)*Dxe2)/((1+xe2)*(1+xe2)))
        xe3=x3[j]/(1+e3*(1-x3[j]))
        Dxe3=(1+e3)/((1+e3*(1-x3[j]))*(1+e3*(1-x3[j])))
        l3=abs((mu*(1-2*xe3-xe3*xe3)*Dxe3)/((1+xe3)*(1+xe3)))
        sum1=sum1 + np.log(l1)
        sum2=sum2 + np.log(l2)
        sum3=sum3 + np.log(l3)
    Y1[i]=sum1/3000 #variation of liapunov exponentr in the direction Y
    Y2[i]=sum2/3000 #variation of liapunov exponentr in the direction Y
    Y3[i]=sum3/3000 #variation of liapunov exponentr in the direction Y
    X[i]=mu #variation of control parameter in the direction of X
    i=i+1
O=np.zeros(len(MU))
plt.plot(X,O,linewidth = 1,c='black')
plt.plot(X,Y1,linewidth = 1,c='g',label="$\epsilon$1 = %0.2f " % e1)
plt.plot(X,Y2,linewidth = 1,c='r',label="$\epsilon$2 = %0.2f " % e2)
plt.plot(X,Y3,linewidth = 1,c='b',label="$\epsilon$3 = %0.2f " % e3)

#plt.ylim(-8,3)
#plt.xlim(1,5.8)

plt.title("Liapunov function - ")
plt.xlabel("$\mu$")
plt.ylabel("Liapunov exponent ($\lambda$)")
plt.legend()
plt.show()

