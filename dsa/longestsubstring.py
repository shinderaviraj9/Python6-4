def longestnotrepeatedsubstring(substring):
    start,longest,visited=0,0,[False for _ in range(256)]

    for i,s in enumerate(substring):
        if visited[ord(s)]==True:
            while s!=substring[start]:
                visited[ord(s)] = False
                start+=1
            start+=1
        else:
            visited[ord(s)]=True
        longest =max(longest,i-start+1)

    return longest


if __name__ == '__main__':
    print(longestnotrepeatedsubstring('abcdaez'))