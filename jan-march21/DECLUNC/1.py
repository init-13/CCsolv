#from collections import deque
for _ in range(int(input())):
    n=int(input())
    s=input()
    p=input()
    c0=0
    f=0
    for i in range(n):
        if s[i]=='1' and p[i]=='0':
            c0+=1
        elif p[i]=='1' and s[i]=='0':
            c0-=1

        if c0<0:
            f=1
            break

    if f or c0:
        print("No")
    else:
        print("Yes")
        
            
            
        
