def rotate_list(l,k):
    start=0
    end=len(l)-1
    rot=k%len(l)
    while start<end:
        l[start],l[end]=l[end], l[start]
        start+=1
        end-=1
    print(l)
    start1=0
    end1=rot-1
    while start1<=end1:
        l[start1],l[end1]=l[end1], l[start1]
        start1+=1
        end1-=1

    start2 = rot
    end2 = len(l)-1
    while start2 <= end2:
        l[start2], l[end2] = l[end2], l[start2]
        start2 += 1
        end2 -= 1
    print(l)

if __name__ == '__main__':
    rotate_list([1,2,3,4],2)