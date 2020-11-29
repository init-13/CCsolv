
        




for i in range(int(input())):
    cp=0
    mp=0
    n=int(input())
    for xi in range(n):
        x=list(input().split())
        a=x[0]
        b=x[1]
        a=list(a)
        b=list(b)
        a=sum(list(map(int,a)))
        b=sum(list(map(int,b)))
        if a>b:
            
            cp+=1
        elif a<b:
            
            mp+=1
        else:
            cp+=1
            mp+=1
    if cp>mp:
        print(0,cp)
    elif mp>cp:
        print(1,mp)
    else:
        print(2,cp)
        
