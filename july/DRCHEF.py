from math import log2
from math import ceil
from math import floor
for i in range(int(input())):
    n,x=map(int,input().split())
    pli=list(map(int,input().split()))
    pli.sort()
    qli=list()
    for xx in pli:
        qli.append(xx)
    newli=list('1'*n)
    newqli=list('1'*n)
    tag=-1
  #  print(pli,qli)
    for i in range (n):
        if pli[i]<x:
            newli[i]=1
            newqli[i]=1
        else:
            tag=i
            break
  #  print(tag)
    
    if tag!=-1:
        #print("ekjfkajfhkslflk")
        newli[tag]=1+ceil(log2(pli[tag]/x))
        '''if pli[tag]>=2*x:
            pli[tag]=x*(2**floor(log2(pli[tag]/x)))'''
       # print(tag,n)
        for i in range(tag+1,n):
            #print("sdsd")
            newli[i]=ceil(log2(pli[i]/pli[i-1]))
            '''if pli[i]>=2*pli[i-1]:
                pli[i]=pli[i-1]*(2**floor(log2(pli[i]/pli[i-1])))'''
            #print(pli)
            if newli[i]==0:
                newli[i]=1
        if tag==0:
            #print(newli)
            print(sum(newli))
        else:
            #print(pli,qli)
            for i in range(tag,n):
                newqli[i]=ceil(log2(qli[i]/qli[i-1]))
                '''if qli[i]>=2*qli[i-1]:
                    qli[i]=qli[i-1]*(2**floor(log2(qli[i]/qli[i-1])))'''
                if newqli[i]==0:
                    newqli[i]=1
            #print(pli,qli,newli,newqli)
            print(min(sum(newli),sum(newqli)))
            
    else:            
    #print(tag,newli)
        print(sum(newli))

