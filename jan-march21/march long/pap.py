def srtslp(a):
    i=len(a)
    for x in range(i):
        a[x]=[a[x],a[x]/(x+1),x+1]

    return sorted(a,key=lambda x:x[1])

print(srtslp([3 ,2 ,5 ,3 ,2 ,4 ,3]))
