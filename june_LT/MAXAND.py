
for _ in range(int(input())):
    
    dub1=set()
    dub2=set()
    X,nm=input().split()
    nm=int(nm)
    bnlist=list()
    x=list(map(int,input().split()))
    mxx=len(bin(max(x)))-2
    
    mxx=len(bin(max(x)))-2
    for i in x:
        if len(bin(i))-2<mxx:
            tm=mxx-len(bin(i))+2
        else:
            tm=0
        bnlist.append(list(reversed(list(map(int,list('0'*tm+bin(i)[2:]))))))
        
    
    bnl=len(bnlist)
    xx=bnlist[0]
    for i in range(1,bnl):
        xx=list(zip(xx,bnlist[i]))
        
        xxl=len(xx)
        for nn in range(xxl):
            xx[nn]=sum(xx[nn])
    xxl=len(xx)
    for nn in range(xxl):
        xx[nn]*=2**nn
        #x[nn]=list([x[nn],2**nn])
    intr=dict()
    for nn in range(xxl):
        if xx[nn] not in intr:
            intr[xx[nn]]=[nn]
        else:
            intr[xx[nn]].append(nn)
    xx.sort(reverse=True)
    
    print(intr)
    amin=0
    #print(xx,intr)
    if len(xx)-1<nm:
        nm=len(xx)
    xx= xx[:nm]
    print(xx)
    while(nm and xx):
        amin+=2**intr[xx.pop(0)].pop(0)
        
        nm-=1
    print(amin)
        
        

               
               
               
               
               
