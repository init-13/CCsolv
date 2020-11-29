n,r=map(int,input().split())
lis=list(map(int,input().split()))
lis.sort()
sm=list()
while(lis):
    nw=lis.pop(0)
    nlis=list()
    nlis.append(0)
    for i in lis:
        if (i%nw)%r==0:
            
            
