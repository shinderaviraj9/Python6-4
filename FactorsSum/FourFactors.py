import numpy as np
factors=[]
number=int(input('Enter number to check if it has four factors'))
count=0
for i in range(2,int(np.sqrt(number))):
    if number%i ==0:
        count+=1
        factors.append(int(i))
        other_factor= number/i
        if other_factor!=i:
            count+=1
            factors.append(int(other_factor))
if count==2:
    print('Number has four factors')
    factors.append(1)
    factors.append(number)
else :
    print('number does not have four factors')
print(factors)
