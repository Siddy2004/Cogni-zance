# QUESTION-1

import numpy as np
n1 = int(input("Enter First Number:\n"))
n2 = int(input("\nEnter Second Number:\n"))
a1 = np.arange(n1,n2+1)
a2 = np.copy(a1)

print("\nOriginal Vector:")
print(a1,"\n")
# No. of consecutive zeroes to be inserted
n = 5

for i in range(len(a1)*n):
    for j in range(n):
        if a2[i] in a1:                
            a2 = np.insert(a2,i+1,0)
            
a2 = a2.astype('float')
print("Vector after insertion of zeros")
print(a2)