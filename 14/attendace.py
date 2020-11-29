for _ in range(int(input())):
    sn=input()
    snl=len(sn)-1
    x,y=input().split()
    ss=int(x)+int(y)
    if snl%ss:
        print('safe')
    else:print('unsafe')
