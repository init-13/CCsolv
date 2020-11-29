from math import gcd
from math import sqrt
def cof(a,b):
    a=abs(a)
    b=abs(b)
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
def ch20(t,A,B):
    cd=cof(B[0],B[1])
    
    for x in cd:
        if B[1]/x - A[1] == B[0]/x - A[0] == t or B[1]/x - A[1] == B[0]/x - A[0] == x*t :
            return 11
    for f in range(2):
        for x in cd:
            if (B[0]/x - A[0] == t or B[0]/x - A[0] == t/x) and B[1]/x==A[1] :
                return 12
        r=B[1]-A[1]
        if r%t==0 and (B[0]*r/t - A[0] == 0 or B[0]*r/t - A[0] == r):
            return 13
        A=A[1:]+A[:1]
        B=B[1:]+B[:1]
    return 0
    
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
    if any(lambda x:not x.is_integer() for x in ml):
        ml=[]
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
            if A[i]!=0 and B[i]%A[i]==0:
                ml.append(B[i]/A[i])

    if ad[0]==ad[1] or ad[1]==ad[2] or ad[2]==ad[0]:
        return 2
    if (len(ml)==3):
        if ml[0]==ml[1] or ml[1]==ml[2] or ml[2]==ml[0]:
            return 3 
    elif (len(ml)==2):
        if ml[0]==ml[1]:
            return 4
        
       
    if ad[0]+ad[1]==ad[2] or ad[1]+ad[2]==ad[0] or ad[2]+ad[0]==ad[1] :
        return 5
    if (len(ml)==3):
        if ml[0]*ml[1]==ml[2] or ml[1]*ml[2]==ml[0] or ml[2]*ml[0]==ml[1]:
            return 6
    
    a=A[0]
    b=A[1]
    c=A[2]
    x=B[0]
    y=B[1]
    z=B[2]
    cd=cdi(x-y,y-z,z-x)
    for t in cd:
        if x-a*t== y-b*t == z-c*t :
            return 7
    if (0 not in A):
        for q in range(3):
            A=A[2:]+A[:2]
            B=B[2:]+B[:2]
            tmp=A[1]*B[2]-A[2]*B[1]
            if (tmp==A[1]*(B[0]-A[0]) or tmp==B[1]*(B[0]-A[0])) and B[1]%A[1]==0:
                return 8
            if (B[0]*A[2]-A[0]*B[2]==(B[2]-B[0])*(B[1]-A[1]) or B[0]*A[2]-A[0]*B[2]==(A[2]-A[0])*(B[1]-A[1])) and B[0]%(A[0]*(B[1]-A[1]))==0:
                return 9
            
        A.reverse()
        B.reverse()
        for q in range(3):
            A=A[2:]+A[:2]
            B=B[2:]+B[:2]
            tmp=A[1]*B[2]-A[2]*B[1]
            if (tmp==A[1]*(B[0]-A[0]) or tmp==B[1]*(B[0]-A[0]) or tmp==A[1]*B[0]-A[0]*B[1]) and B[1]%A[1]==0:
                return 8
            if (B[0]*A[2]-A[0]*B[2]==(B[2]-B[0])*(B[1]-A[1]) or B[0]*A[2]-A[0]*B[2]==(A[2]-A[0])*(B[1]-A[1])) and B[0]%(A[0]*(B[1]-A[1]))==0:
                return 9
            
    elif(A.count(0)==2):
        O1=0
        O2=0
        for x in range(3):
            if A[x]==0:
                if O1:
                    O2=B[x]
                else:
                    O1=B[x]
            else:
                c1=A[x]
                c2=B[x]
                    
        tmp=c1*(max(O1,O2)/min(O2,O1))
        if tmp==c2 or tmp==c2-max(O2,O1) and max(O1,O2)%min(O2,O1)==0:
            return 10
    elif(A.count(0)==1):
        X=list()
        Y=list()
        for x in range(3):
            if A[x]==0:
                t=B[x]
            else:
                X.append(A[x])
                Y.append(B[x])
        return ch20(t,X,Y)
        
    return 0
def isw(A,B):
    if A==B:
        return 0
    elif (B.count(0)==3):
        return 1
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
