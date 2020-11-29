for _ in range(int(input())):
    n,mx=input().split()
    mx=int(mx)
    cl=list(map(int,input().split()))
    x=cl.count(mx)
    cll=len(cl)
    cl=set(cl)
    lens=0
    for i in cl:
        if i<=int(mx):
            lens+=1
    #print(lens)
    if lens==mx:
        print(cll-x)
    elif lens==mx-1:
        print(cll)
    else:
        print(-1)
            
