for _ in range(int(input())):
    s='^'+input()+'$'
    
    l=len(s)
    ch=0
    for i in range(2,l):
        if s[i]!=s[i-1]:
            if s[i-1]==s[i-2]:
                ch+=40
            else:
                ch+=8
    l-=2
    print(8*l - ch)
