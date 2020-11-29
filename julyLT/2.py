
def bc(x,y):

    a=bin(x)[2:]+bin(y)[2:]
    b=bin(y)[2:]+bin(x)[2:]
    a=int(a,2)
    b=int(b,2)

    return b-a
    
for _ in range(int(input())):

    n=int(input())

    x=list(map(int,input().split()))
    p=max(x)
    q=min(x)
    Mx=p
    Mxb=bin(p).count('1')

    mx=q
    mxb=bin(q).count('1')
    for i in range(n):
        #print(Mx,mx)
        t=bin(x[i]).count('1')
        #print(t)
        if t > Mxb:
            Mxb=t
            Mx=x[i]
        if t<mxb:
            mxb=t
            mx=x[i]
    print(bc(Mx,mx))
                
        
        
