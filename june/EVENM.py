for _ in range(int(input())):
    n=int(input())
    i=1
    for s in range(n):
        l=list(range(i,i+n))
        if s%2:
            l.reverse()
        for x in l:
            print(x,end=" ")
        i+=n
        print("")
