for _ in range(int(input())):
    s=input()
    n=len(s)
    c=0
    i=0
    while i in range(n):
        i+=1
        if i==n:break
        if s[i]!=s[i-1]:
            c+=1
            i+=1
    print(c)
