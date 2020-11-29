

for _ in range(int(input())):
    
    tag,denm=map(int,input().split())
    if tag&1:
        num=1
        tag-=1
    else:num=0
    #print(tag,bin(tag)[-1],num)
    if  denm>=tag :
        if tag:
            print(num+1)
        else:
            print(num)
        continue
    else:
        while tag:
            x=tag//denm
            num+=x
            tag-=x*denm
            denm=tag%denm
        print(num)      
               
               
               
               
               
