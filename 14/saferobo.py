for _ in range(int(input())):
    sn=input()
    snl=len(sn)
    x,y=input().split()
    a,b=1,snl
    us=0
    while(a<b and a<=snl and b>=1):
        print("."*(a-1)+"A"+str("."*(b-a-1))+"B"+"."*(snl-b))
        
        a+=int(x)
        b-=int(y)
        if a==b:
            us=1
            print('unsafe')
            
    if not us:
        print("safe")
            
