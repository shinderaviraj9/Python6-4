def nesting_array(arr):
    n=len(arr)
    seen=[False]*n
    ans=0
    for num in arr:
        l=0
        while not seen[num]:
            seen[num] = True
            l=l+1
            num=arr[num]
        ans=max(ans,l)
    return ans

if __name__ == '__main__':
    print(nesting_array([5,4,0,3,1,6,2]))