from math import gcd
from math import sqrt
def cof(a,b):
    n=list()
    gc=gcd(a,b)
    for i in range(1, int(sqrt(gc))+1):
        if gc%i==0:
            n.append(i)
            if gc!=i*i:
                n.append(int(gc/i))
    return n


def cdi(a,b,c):
    a=abs(a)
    b=abs(b)
    c=abs(c)
    cd=list()
    x=cof(a,b)
    for t in x:
        if not c%t:
            cd.append(t)
    return cd
    
def is1(A,B):
    C=list()
    ad=list()
    ml=list()
    popl=list()
    s2=0
    for i in range(3):
        if s2==2:
            return 1
        if A[i]==B[i]:
            s2+=1
        else:
            ad.append(B[i]-A[i])
            if A[i]!=0:
                ml.append(B[i]/A[i])
            else:
                if B[i]==0:
                    ml.append(0)
    
    if (len(ad)):
        if all(x==ad[0] for x in ad):
            return 1
    if (len(ml)>1):
        if all(x==ml[0] for x in ml):
            return 1
    return 0

def is2(A,B):
    ad=list()
    ml=list()
    for i in range(3):
        if A[i]==B[i]:
            return 1
        else:
            ad.append(B[i]-A[i])
            if A[i]!=0:
                ml.append(B[i]/A[i])
    if ad[0]==ad[1] or ad[1]==ad[2] or ad[2]==ad[0]:
        return 1
    if (len(ml)==3):
        if ml[0]==ml[1] or ml[1]==ml[2] or ml[2]==ml[0]:
            return 1 
    elif (len(ml)==2):
        if ml[0]==ml[1]:
            return 1
        
        
    if ad[0]+ad[1]==ad[2] or ad[1]+ad[2]==ad[0] or ad[2]+ad[0]==ad[1] :
        return 1
    if (len(ml)==3):
        if ml[0]*ml[1]==ml[2] or ml[1]*ml[2]==ml[0] or ml[2]*ml[0]==ml[1]:
            return 1
    
    a=A[0]
    b=A[1]
    c=A[2]
    x=B[0]
    y=B[1]
    z=B[2]
    cd=cdi(x-y,y-z,z-x)
    for t in cd:
        if x-a*t== y-b*t == z-c*t :
            return 1
    if (0 not in A):
        for q in range(3):
            tmp=A[1]*B[2]-A[2]*B[1]
            if tmp==A[1]*(B[0]-A[0]) or tmp==B[1]*(B[0]-A[0]):
                return 1
            if B[0]*A[2]-A[0]*B[2]==(B[2]-B[0])*(B[1]-A[1]):
                return 1
            A=A[2:]+A[:2]
            B=B[2:]+B[:2]
    
        
        
    return 0
        
def isw(A,B):
    if A==B:
        return 0
    if is1(A,B):
        return 1
    elif is2(A,B):
        return 2
    else:
        return 3
if __name__=='__main__':    
    for _ in range(int(input())):
        A=list(map(int,input().split()))
        B=list(map(int,input().split()))
        
        print(isw(A,B))
