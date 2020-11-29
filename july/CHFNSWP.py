
for i in range(int(input())):
    N=int(input())
    A=list(map(int,input().split()))
    B=list(map(int,input().split()))
    A.sort()
    B.sort()
    j=0
    i=0
    aset=0
    bset=0
    xset=0
    xxm=9999999
    #print(A,B)
    while(i<len(A)):
        #print(A,B)
        while(j<len(B) and B[j]<A[i]):
            j+=1
            
        if j<len(B) and B[j]==A[i]:
            if not xset:
                xset=1
                xxm=min(A[i],B[j])
            A.pop(i)
            B.pop(j)
        else:
            i+=1
    Aun=list()
    Bun=list()
    #print(A,B)
    N=len(A)
    if A==B:
        print(0)
        continue
    elif N==1 and A!=B:
        print(-1)
        continue
    no=0
    i=0
    Asam=list()
    Bsam=list()
    while (i<N-1):
        tmp=1
        while(i<N-1 and A[i]==A[i+1]):
            if not aset and xxm>A[i]:
                aset=1
                xxm=A[i]
            tmp+=1
            i+=1
        if tmp%2 and tmp!=1:
            print(-1)
            no=1
            break
        else:
            for x in range(tmp//2):
                Asam.append(A[i])
        if no:
            break
        if tmp==1:
            Aun.append(A[i])
            
        i+=1
        if i==N-1:
            Aun.append(A[i])

    if no:
        continue
    i=0
    while (i<N-1):
        tmp=1
        while(i<N-1 and B[i]==B[i+1]):
            if not bset and xxm>B[i]:
                bset=1
                xxm=B[i]
            tmp+=1
            i+=1
        if tmp%2 and tmp!=1:
            print(-1)
            no=1
            break
        else:
            for x in range(tmp//2):
                Bsam.append(B[i])
        if no:
            break
        if tmp==1:
            Bun.append(B[i])
        i+=1
        if i==N-1:
            Bun.append(B[i])
    #print(Aun,Bun)
    
    '''AXsam=[ix for ix in Asam if ix not in Bsam]
    Bsam=[ix for ix in Bsam if ix not in Asam]
    Asam=AXsam'''
    #print(Asam,Bsam)
    if Aun!=Bun or len(Asam)!=len(Bsam):
        print(-1)
        no=1
        continue
    if no:
        continue
    else:
        Bsam.reverse()
        akun=list(zip(Asam,Bsam))
        ms=0
        for xx in akun:
            xm=min(xx)
            if xm<2*xxm:
                ms+=xm
            else:
                ms+=2*xxm
        print(ms)
        continue



            
        

    
            
            
            
    
    
        
    
    
    
    
