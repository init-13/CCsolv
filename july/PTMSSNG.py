
for i in range(int(input())):
    n=int(input())
    N=4*n-1
    px=dict()
    py=dict()
    MX=0
    MY=0
    for i in range(N):
        x,y=(map(int,input().split()))
        if x in px:
            px[x]+=1
        else:
            px[x]=1

        if y in py:
            py[y]+=1
        else:
            py[y]=1

    for i in px:
        if px[i]%2:
            MX=i
            break
    for i in py:
        if py[i]%2:
            MY=i
    print(MX,MY)
            
            
    
    
        
    
    
    
    
