

for _ in range(int(input())):
    
    dub1=set()
    dub2=set()
    input()
    ys=1
    x=list(map(int,input().split()))
    for i in x:
        if i not in dub1:
            dub1.add(i)
        elif i not in dub2:
            dub2.add(i)
        elif i in dub2:
            print('NO')
            ys=0
            break
    
    if ys:
        dub11=list(sorted(dub1))
        dub22=list(sorted(dub2,reverse=True))
        #print(dub11,"f",dub22)
        if dub2 and dub11[-1]==dub22[0]:
                print('NO')
                
        else:
            print('YES')
            mli=dub11+dub22
            for x in mli:
                print(x,end=" ")
            print()
               
               
               
               
               
