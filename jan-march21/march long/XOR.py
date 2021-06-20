for _ in range(int(input())):
    x=input()
    if x=='1':
        print(0)
        continue
    if x=='0':
        print(1)
        continue
        
    n=list(bin(int(x))[2:])
    #print(n)
    for i in range(len(n)):
        if n[i]=='1':
            n[i]='0'
        else:
            n[i]='1'
            
    n="".join(n)
    #print(n)
    print(int('1'+n[1:],2)*int('1'*(len(n)-1),2))
