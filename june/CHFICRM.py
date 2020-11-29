for _ in range(int(input())):
    Ll=int(input())
    L=list(map(int,input().split()))
    #print(L)
    cdi=dict()
    cdi[5]=0
    cdi[10]=0
    cdi[15]=0
    no=False
    for i in L:
        if i not in cdi:
            no=True
            break
        cdi[i]+=1
        if i==10:
            cdi[5]-=1
        elif i==15:
            if cdi[10]:
                cdi[10]-=1
            else:
                cdi[5]-=2
        print(cdi)
        if -1 in cdi.values() or -2 in cdi.values():
            no=True
            break
        
    if no:
        print("NO")
    else:
        print("YES")
