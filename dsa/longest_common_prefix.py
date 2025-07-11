def lcp(l:list)->str:
    c=""
    for i in range(len(l[0])):
        for s2 in l[1:]:
            if i==len(s2) or s2[i]!=l[0][i]:
                return c
        c+=l[0][i]
    return c

if __name__=="__main__":
    print(lcp(['flowers','flow','flock']))