n=int(input())
for j in range(n-1,-1,-1):
    #print(j+1)
    if j==n-1:
        print(chr(65+j).rjust(j+1))
    else:
        print(str(" "*(j)+chr(65+j)+" "*(2*(n-j-1)-1)+chr(65+j)))
for j in range(1,n):
    if j==n-1:
        print(chr(65+j).rjust(j+1))
    else:
        print(str(" "*(j)+chr(65+j)+" "*(2*(n-j-1)-1)+chr(65+j)))
 
