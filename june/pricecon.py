for _ in range(int(input())):
    n,k=input().split()
    k=int(k)
    l=list(map(int,input().split()))
    con=0
    for i in l:
        if i>k:
            con+=i-k
    print(con)
