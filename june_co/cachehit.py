for _ in range(int(input())):
    n,b,m=input().split()
    cl=list(map(int,input().split()))
    cll=len(cl)
    cn=1
    b=int(b)
    for i in range(1,cll):
        if cl[i-1]//b != cl[i]//b:
            cn+=1
    print(cn)
            
