def contigious_sum_binary(l:list):
    d={}
    d[0]=-1
    count,seen=0,0
    for i,x in enumerate(l):
       seen+=1 if x else -1
       if seen in d:
           count=max(count,i-d[seen])
       else:
           d[seen]=i

    return count

if __name__ == '__main__':
    print(contigious_sum_binary([0,1]))