
for i in range(int(input())):
    n=int(input())
    r=n//8
    c=n%8
    xx=list()
    for i in range(8):
            
        if i<r:
            tp='.'*8
        elif i==r:
            tp='X'*(8-c)+'.'*c
        else:
            tp='X'*8
        xx.append(tp)
    if r%2:
        nx=xx[0]
        nx='O'+nx[1:]
        xx[0]=nx
    else:
        nx=xx[0]
        nx=nx[:-1]+'O'
        xx[0]=nx
    s='\n'.join(xx)
    print(s)
        
        
    
        
            
            
