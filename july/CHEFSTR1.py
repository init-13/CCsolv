for i in range(int(input())):
    n=int(input())
    x=list(map(int,input().split()))
    sc=0
    for xi in range(1,n):
        tp=abs(x[xi]-x[xi-1])
        if tp:
            tp-=1
        sc+=tp
    print(sc)
        
