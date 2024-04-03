import numpy as np
R=np.arange(0.0001,1,0.0001)
b=np.zeros(9999)
for i in range(9999):
    b[i]=(1+R[i])/(R[i]*(1-R[i]))
    #print(b[i])

max=0
for r in b:
    if r>max:
        max=r
print(max)
k=R[9998]
j=(1+k)/(k*(1-k))
















