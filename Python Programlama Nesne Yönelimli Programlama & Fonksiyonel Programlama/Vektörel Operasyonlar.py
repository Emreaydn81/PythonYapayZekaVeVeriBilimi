#Vektorel Operasyonlar

a = [1,2,3,4]
b = [2,3,4,5]

ab = []

range (0, len(a))

for i in range(0, len(a)):
    print(i)


for i in range(0, len(a)):
    ab.append(a[i]*b[i])
    
    ab

#FP

import numpy as np

a = np.array([1,2,3,4])
b = np.array([2,3,4,5])

a*b
