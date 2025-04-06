import math
height=[4,2,0,3,2,5]
lval=height[0]
rval=height[len(height)-1]
lindex=0
rindex=len(height)-1
water_hold= [0 for i in range(len(height))]
print(water_hold)
left=lindex+1
right=rindex-1

while left<=right:
    if lval<=rval :
       water_hold[left]=max(0,lval-height[left])
       left=left+1
    else:
       water_hold[right]=max(0,rval-height[right])
       right=right-1

print(water_hold)
sum_water=sum(water_hold)
print(sum_water)


