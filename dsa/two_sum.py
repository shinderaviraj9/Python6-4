def two_sum(input,target):
    left=0
    right= len(input)-1
    while(left<right):
        curr_sum=input[left]+input[right]
        if(curr_sum==target):
            print(left,right)
            return left, right
        elif(curr_sum>target):
            right=right-1
        elif(curr_sum<target):
            left=left+1
    return -1,-1

if __name__=='__main__':
    input = [2, 7, 11, 15]
    target = 9
    result=two_sum(input,target)
    if result[0]!=-1:
        print(f'Found at index {result[0]}, {result[1]}')
    else :
        print('No found')