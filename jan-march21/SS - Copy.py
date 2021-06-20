
for tc in range(int(input())):
    n=int(input())
    i=1
    j=1
    k=2
    #print(i+j+k)
    #print(i,j,k)
    for xx in range(n):
        #print(i,j,k)
        tm = i+j+k
        #print(tm)
        i=j
        j=k
        k=tm
        #print(i,j,k)
    print(j)
