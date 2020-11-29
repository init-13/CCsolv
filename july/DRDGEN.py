
for _ in range(1):
    n,q = map(int,input().split())
    H=list(map(int,input().split()))
    T=list(map(int,input().split()))

    for i in range(q):
        Q=list(map(int,input().split()))
        if Q[0]==1:
            T[Q[1]-1]=Q[2]
        else:
            n1=Q[2]-1
            n2=Q[1]-1
            s=0
            nxmx=H[n1]-1
            cp=n1
            if n1<=n2:
                for i in range(n1,n2+1):
                    if H[i]>nxmx:
                        nxmx=H[i]
                        s+=T[i]
                        cp=i
                if cp!=n2:
                    print(-1)
                else:
                    print(s)
            else:
                for i in range(n1,n2-1,-1):
                    if H[i]>nxmx:
                        nxmx=H[i]
                        s+=T[i]
                        cp=i
                if cp!=n2:
                    print(-1)
                else:
                    print(s)
                    
                    

            
        

    
            
            
            
    
    
        
    
    
    
    
