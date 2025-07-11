def longestconsecutive(l:list)->int:
    s=set(l)
    longest=0
    for n in l:
        length=0
        if n-1 not in s:
            while n+length in s:
                length+=1
        longest =max(longest,length)

    return longest

if __name__=="__main__":
    print(longestconsecutive([100,101,102,1,2,3,4,500]))




