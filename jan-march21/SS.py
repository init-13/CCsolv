def chkup(A,n,i):
    for j in range(n-1,i,-1):
        if A[i][j]:
            #print()
            #print(i+1, j+1)
            for x in range(j+1,n):
                #print(i+1,x+1,end=" -> ")
                #print(j+1,x+1,end="$$")
                A[i][x]+=A[j][x]
                



def builm(n):
    A=list()
    for i in range(n):
        A.append(list(range(n)))
        for j in range(n):
            A[i][j]=0
        

    return A

def upi(A,n):
    for i in range(n):
        if i+1<n:
            A[i][i+1]=1        
        if (i+2) < n:
            A[i][i+2]=1
        if (i+3) < n:
            A[i][i+3]=1

for tc in range(int(input())):
    n=int(input())
    n+=2
    A=builm(n)
#print(A)
    upi(A,n)
    #for xx in A:
        #print(xx)
    #print()
    for x in range(n-1,-1,-1):
        chkup(A,n,x)


    for xx in A:
        print(xx)

