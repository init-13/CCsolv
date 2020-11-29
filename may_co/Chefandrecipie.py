

for _ in range(int(input())):
    nl=int(input())
    nl+=1
    lis=list(input().split())
    lis.append('$')
    print(lis)
    ui=set()
    nui=set()
    n=1
    for i in range(nl-1):
        
        if lis[i] in ui:
            print('NO')
            break
        elif lis[i]!=lis[i+1]:
            if n in nui:
                print('NO')
                break
            nui.add(n)
            n=1
            ui.add(lis[i])
            
        else:n+=1
    if (i+2)==nl:
        print('YES')
            
