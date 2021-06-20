
def chl(O,A,i,j):
    fi,fj=0,0
    jset=set()
    iset=set()
    jpos,fpos=0,0
    for xx in range(len(A)):
        if i in A[xx]:
            fi=xx+1
            iset=A[xx]
        elif j in A[xx]:
            fj=xx+1
            jset=A[xx]
    #print(A,fj,fi)
    if fi and fj:
        first=max(fi,fj)-1
        second=min(fi,fj)-1
        del A[first]
        del A[second]
        #A.discard(fset)
        
        A.append(jset.union(iset))
        return
        
    for xx in A:
        if i in xx:
            xx.add(j)
            O.discard(j)
            return
        if j in xx:
            xx.add(i)
            O.discard(i)
            return
        
    A.append(set([i,j]))
    O.discard(i)
    O.discard(j)


def mx(A,W):
    mx=-1
    mx_set={}
    for i in A:
        tm=0
        for xx in i:
            tm+=W[xx-1]
            
        if tm>mx or (tm==mx and len(i)<len(mx_set)):
            mx=tm
            mx_set=i
    #print(mx)
    return sorted(list(mx_set))
        
    
n=int(input())
O=set()
for i in range(1,n+1):
    O.add(i)
A=list()
W=list(map(int,input().split()))
for x in range(int(input())):
    i,j=map(int,input().split())
    chl(O,A,i,j)
    #print(A,O)
for x in O:
    A.append(set([x]))
#print(A)
for ii in mx(A,W):
    print(ii,end=" ")
print()
