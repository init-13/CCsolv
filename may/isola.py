def gdic(s):
    mydic=dict()
    for i in s:
        if i in mydic:
            mydic[i]+=1
        else:
            mydic[i]=1
    return mydic   
    #print(mydic)
def minq(mydic,n):
    rem=0
    for i in mydic:
        if mydic[i]>n:
            rem+=mydic[i]-n
    print(rem)

for _ in range(int(input())):
    i,j=input().split()
    s=input()
    st=gdic(s)
    for x in range(int(j)):
        minq(st,int(input()))
