import time

def co(ss,s):
	p=0
	n=0
	c=0
	while n<len(s):
	    #print(s[i:i+n])
	    p=s.find(ss,n)
	    
	    if p==-1:
	        break;
	    else:
	        c+=1
	        n=p+1
	    
	return(c)
def pleasure(dct,sr):
    sm=0
    for i in dct:
        sm+=co(i[0],sr)*i[1]
    return sm
	
def maxP(a,b,n):
    start_time = time.time()    
    fav=list()
    for _ in range(int(n)):
        k,v=input().split()
        fav.append((k,int(v)))
    MAX=0
    al=len(a)
    bl=len(b)
    sset=list()
    '''for j in range(al):
            for i in range(bl-1):
                sset.extend(a[j:]+b[i:])'''
    for j in range(bl+1):
            for i in range(al+1):
                new=a[:i]+b[j:]
                if new not in sset:
                        sset.append(new)
    for x in sset:
        p=pleasure(fav,x)
        if p > MAX:
            MAX=p
    print(MAX)
    print("--- %s seconds ---" % (time.time() - start_time))
for _ in range(int(input())):
        maxP(input(),input(),input())

        
                            
    
        
        


 
