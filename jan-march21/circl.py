import math
r1=int(input())
r2=int(input())
s1=int(input())
s2=int(input())
t=int(input())
d=int(input())

pi=3.141592653589793
if (r1+r2<d):
    print("no crash")
    quit()
ACOS=(r1**2 -r2**2+d**2)/(2*r1*d)
BCOS=(r2**2 -r1**2+d**2)/(2*r2*d)

ang_A=2 * math.degrees(math.acos(ACOS))
ang_B=2 * math.degrees(math.acos(BCOS))

ang_A/=360
ang_B/=360

A_time=0
B_time=0

Art=2*pi*r1/abs(s1)
Brt=2*pi*r2/abs(s2)

Af=2*pi*r1*ang_A/abs(s1)
Bf=2*pi*r2*ang_B/abs(s2)
print(Af,Bf)
Alis=list()
Blis=list()

if s1>0 and t>Af:
    Alis.append(math.floor(Af))
    A_time+=Af

if s2>0 and t>Bf:
    Blis.append(math.floor(Bf))
    B_time+=Bf
r=0
while(A_time<t  or B_time<t):
    if not r%2:
        A_time+=Art-Af
        B_time+=Brt-Bf
    else:
        A_time+=Af
        B_time+=Bf

    Alis.append(math.floor(A_time))
    Blis.append(math.floor(B_time))
    
Alis.pop()
Blis.pop()
print(Alis)
print(Blis)
bff=0
for i in range(len(Alis)):
    for j in range(len(Blis)):
        if Alis[i] == Blis[j] and abs(i-j)%2:
            if r1+r2==d:
                FF='E&D'
            elif not i%2:
                FF='E'
            else:
                FF='F'
            print(Alis[i],FF)
            bff=1
            break
    if bff:
        break
if not bff:
    print("no crash")
        
    


