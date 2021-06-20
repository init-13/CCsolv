for _ in range(int(input())):
    s=input()
    ac=0
    zc=0
    for i in s:
        if i=='1':
            ac+=1
        else:
            zc+=1
   # print(ac,zc,abs(ac-zc))
    if not abs(ac-zc)%2 and ac and zc:
        print(abs(ac-zc)//2)
    else:
        print(-1)
