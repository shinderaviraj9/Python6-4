import numpy as np
mat= np.arange(24).reshape(6,4)


element =int(input('Enter the Element to Search in 0,24'))
r=len(mat)
c=len(mat[0])

i=r-1
j=0
status=False
while (i>=0 and j<c):
    if mat[i,j]==element:
        status=True
        break
    elif mat[i,j]>element:
        i=i-1
    else :
        j=j+1
print(f' Element is present' if status else 'Element not present')