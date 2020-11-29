
def st(nli):
    sts=""
    fy=0
    fn=0
    MIN=0
    chkmin=0
    for i in range(len(nli)-1):
        dif=nli[i]-nli[i+1]
        if abs(dif)<3:
            sts+='Y'
            fy+=1
            chkmin=0
        else:
            sts+=' '
            fn+=1
            chkmin+=1
            if chkmin==2:
                MIN=1
    #print(sts)
    ml=set(map(lambda x:len(x)+1,sts.split()))
    if fy and not fn:
        print(len(nli),len(nli))
    elif fn and not fy:
        print(1,1)
    elif MIN or sts[0]==' ' or sts[-1]==' ':
        print(1,max(ml))
    else:
        print(min(ml),max(ml))

if __name__=='__main__':
    for _ in range(int(input())):
        input()
        st(list(map(int,input().split())))
