from math import log2
for _ in range(int(input())):
    num=int(input())
    if num<=0:
        print(0)
        continue
    if log2(num).is_integer() or num<3:
        print(0)
    else:
        x=bin(num)
        b=1
        xl=len(x)
        #print(x,xl)
        for i in range(xl-1,0,-1):
            if x[i]=='1':
                break
            b+=1
            
        print(num//pow(2,b))
    
