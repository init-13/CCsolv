def sed(smli,sli,idc,s,t):
    sm=0
    si=idc[s][0][0]
    ti=idc[t][0][0]
    mli=sli[si]
    while(si!=ti):
        
        
        if idc[s][0][1]: sm+=( smli[si][-2]-smli[si][idc[s][0][1]-1]  )
        else: sm+=( smli[si][-2])
        s=mli[-1]
        
        si=idc[s][0][0]
        ti=idc[t][0][0]
        mli=sli[si]
    
    if idc[s][0][1]: return sm + ( smli[ti][idc[t][0][1]]-smli[si][idc[s][0][1]-1]  )
    else: return sm+ ( smli[ti][idc[t][0][1]])
        

def upsed(smli,smlir,idc,idcr,t,i,inew):
    #global smli
    diff=inew-t[i]
    t[i]=inew
    if i in idc:
        sp=0
        for x in idc[i]:
            if not sp:
                for xx in range(x[1],len(smli[x[0]])):
                    smli[x[0]][xx]+=diff
                sp=1
            else:
                smli[x][-1]+=diff
    if i in idcr:
        sp=0
        for x in idcr[i]:
            if not sp:
                for xx in range(x[1],len(smlir[x[0]])):
                    smlir[x[0]][xx]+=diff
                sp=1
            else:
                smlir[x][-1]+=diff

'''                
sli=[[1,4,8,9,11,17,21],[2,5,8]]
idc=dict()
idc[2]=[[1,0]]
idc[8]=[[0,2],1]
idc[17]=[[0,5]]
smli=[[3,6,9,14,23,46,59],[1,4,7]]

print(sed(smli,sli,idc,2,17))
'''    


for _ in range(1):
    sli=list()
    smli=list()
    idc=dict()

    slir=list() 
    smlir=list()
    idcr=dict()
    
    n,q = map(int,input().split())
    H=list(map(int,input().split()))
    T=list(map(int,input().split()))
    sp=0
    spr=0
    for i in range(q):
        Q=list(map(int,input().split()))
        if Q[0]==1:
            upsed(smli,smlir,idc,idcr,T,Q[1]-1,Q[2])
        else:
            n1=Q[2]-1
            n2=Q[1]-1
            s=0
            nxmx=H[n1]-1
            cp=n1
            if n1<=n2:
                ii=n1
                sl=list()
                sml=list()
                s=0
                ix=0
                yes=0

                if ii in idc:
                    #idc[ii].append(sp)
                    try:
                        print(s+sed(smli,sli,idc,ii,n2))
                        yes=1
                    except:
                        yes=0
                else:
                
                    while ( ii<n ):
                        if H[ii]>nxmx:
                            if ii in idc:
                                idc[ii].append(sp)
                                try:
                                    print(s+sed(smli,sli,idc,ii,n2))
                                    yes=1
                                except:
                                    yes=0

                                break
                            elif ii not in idc:
                                idc[ii]=[(sp,ix)]
                                ix+=1
                                sl.append(H[ii])
                                s+=T[ii]
                                sml.append(s)
                                nxmx=H[ii]
                                if ii==n2:
                                    print(s)
                                    yes=1
                        ii+=1

                if not yes:
                    print(-1)
                sli.append(sl)
                smli.append(sml)
                sp+=1   
                #sl.clear()
                #sml.clear()
                    
                '''   
                for i in range(n1,n2+1):
                    if H[i]>nxmx:
                        nxmx=H[i]
                        s+=T[i]
                        cp=i
                if cp!=n2:
                    print(-1)
                else:
                    print(s)
                    '''
            else:
                #print('back')
                ii=n1
                sl=list()
                sml=list()
                s=0
                ix=0
                yes=0

                if ii in idcr:
                    #idc[ii].append(sp)
                    try:
                        print(s+sed(smlir,slir,idcr,ii,n2))
                        yes=1
                    except:
                        yes=0
                else:
                
                    while ( ii>=0 ):
                        if H[ii]>nxmx:
                            if ii in idcr:
                                idcr[ii].append(spr)
                                try:
                                    print(s+sed(smlir,slir,idcr,ii,n2))
                                    yes=1
                                except:
                                    yes=0

                                break
                            elif ii not in idcr:
                                idcr[ii]=[(spr,ix)]
                                ix+=1
                                sl.append(H[ii])
                                s+=T[ii]
                                sml.append(s)
                                nxmx=H[ii]
                                if ii==n2:
                                    print(s)
                                    yes=1
                        ii-=1

                if not yes:
                    print(-1)
                slir.append(sl)
                smlir.append(sml)
                spr+=1
                #sl.clear()
                #sml.clear()
    #print(idc,idcr)
    #print(sli,slir)
    #print(smli,smlir)
                    
                    

            
        

    
            
            
            
    
    
        
    
    
    
    
