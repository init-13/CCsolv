for _ in range(int(input())):
    n,m=map(int,input().split())
    ni=n
    x=list(map(int,input().split()))
    while(1):
        p=set(map(lambda xx:xx%ni, x))
        print(p)
        p.discard(0)
        if not p:
            break
        ni=min(p)
    print(n-ni)
    
    
    
    
