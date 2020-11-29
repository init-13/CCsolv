import math
def mod(n,d):
    if(int(d)==0):
        return 1
    elif(int(n)==0):
        return 0
            
    if len(d)>5:
        n=int(n)
        d=int(d)
        while(n>d):
            n-=d
        return n-d
            
    m=0

    for i in range(len(n)):
        m=(m*10 +int(n[i]))%int(d)

    return m 

#print(mod('999999999','111111111'))

for _ in range(int(input())):

    s=""
    n,sl=input().split()
    l=list(map(int,input().split()))
    for i in range(int(n)):
        xin=l[i]
        if int(xin)==0:
            s+='1'
            continue
        try:
            x=math.fmod(int(xin),int(sl))
            if not x :
                s+="1"
            else:
                s+="0"
        except:
            s+='0'
    print(s)
