 
def poow(st,wli):
    s=0
    for i in st:
        s+=wli[ord(i)-97]
    return s

def chk(sb,st):
    if not sb or not st:
        return 0
    if sb[0]!=st[0] or st[-1] not in sb:
        return 0
    sl=len(sb)
    stl=len(st)
    
    
    s=0
    while(s+sl<=stl):
        if st[s:s+sl]!=sb:
            return 0
        else:
            s+=sl
    #print(st[:s],st[s:],sb[:stl-s])
    if not stl%sl or st[s:] == sb[:stl-s]:
        return s//sl
    else: return 0


def POW(st,wli):
    if len(st)>1 :
        s=poow(st,wli)
        for i in range(len(st)):
            
            sb=st[:i]
            
            nc=chk(sb,st)
            if nc:
                #print(sb,st,nc)
                s+=poow(sb,wli)
                '''
                #print(sb,st,nc)
                if nc*len(sb)==len(st):
                    #print(1)
                    return nc*(nc+1)*poow(sb,wli)//2
                else:
                    #print(2)
                    return nc*(nc+1)*poow(sb,wli)//2 + poow(st,wli)'''
    else:return poow(st,wli)
    return s
#wli=list(map(int,input().split()))
for _ in range(int(input())):
    s=input()
    #print(s,POW(s,wli))
    wli=list(map(int,input().split()))
    n=0
    ind=dict()
    nn=len(s)
    if nn>100:continue
    for x in range(nn):
        for xx in range(x,nn):
            ss=s[x:xx+1]
            if ss in ind:
                ind[ss]+=1
            else:
                ind[ss]=1
    
    
    #print(ind)
    for x in ind:
        #print(x,POW(x,wli),ind[x])
        n+=(POW(x,wli)*ind[x])
        #n=int(n%998244353)
    #n=int(n%998244353)
    print(n)
    nn=nn*(nn+1)//2
    print(int((n*pow(nn,998244351,998244353))%998244353))
    
        
        
        
        
            
