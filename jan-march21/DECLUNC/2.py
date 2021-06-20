for _ in range(int(input())):
    s=input()
    p=dict()
    for i in s:
        if i in p:
            p[i]+=1
        else:
            p[i]=1

    freq=list(p.values())
    c=0
    f=0
    for i in set(freq):
        if i%3:
            f=1
            break
    if not f:
        print(sum(freq)//3)
        continue
        
    #print(type(freq))
    freq.sort(reverse=True)
    while(freq and freq[-1]==0):
        freq.pop()
    #print(freq)
    
    
        
    while len(freq)>1 and freq[0]>1:
        if freq[0]>freq[-1]*2:
            freq[0]-=freq[-1]*2
            c+=freq[-1]
            freq.pop()
            freq.sort(reverse=True)

        elif freq[0]<freq[-1]*2:
            freq[-1]-=freq[0]//2
            c+=freq[0]//2
            freq=freq[1:]

        else:
            c+=freq[-1]
            freq=freq[1:]
            freq.pop()

        #print(c,freq)

    #print(freq,(freq[-1]>=freq[0]//2 or freq[-1]*2>=freq[0]))
    
    print(c)
