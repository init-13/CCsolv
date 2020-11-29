lb1=1

ub1=int(input())
s='!'
print(1)
s=input()

tc=0
if s=='L':
    tc=1
while(s!='E'):
    if tc==1 :
        mid=(1+ub1+lb1)//2
        print(mid)
        s=input()
        if s=='L':
            ub1=mid-1
        elif s=='G':
            lb1=mid
        tc=0
    
    print(1)
    if input()=='L':
        tc=1
        
