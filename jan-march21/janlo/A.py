def dpair(a):
    n=len(a)
    nn=0
    dp=0
    xp=set()
    for i in a:
        if i < 0:
            nn+=1
            if abs(i) in xp:
                dp+=1
        
        else:
            xp.add(i)

    return nn*(n-nn) - dp


for i in range(int(input())):
    fc=set()
    lc=set()
    c=0
    for j in range(int(input())):
        n=list(map(int,input().split()))[1:]
        c+=dpair(n)
        for x in n:
            if abs(x)in lc:
                continue
            elif abs(x) in fc:
                c+=1
                lc.add(abs(x))
                fc.discard(abs(x))
            else:
                fc.add(abs(x))
            
    print(c)
