for i in range(int(input())):
    n=int(input())
    c,c1=64+n,66
    ch,ch1=64+n-1,66
    for j in range(1,2*n):
        if(j<=8):
            for k in range(1,n+1):
                if(j+k==n+1):
                    print(chr(c),end="")
                    c-=1
                else:
                    print(" ",end="")
            
            for k in range(n+1,2*n+1):
                if((k-n)==j and j>1):
                    print(chr(ch),end="")
                    ch-=1
                else:
                    print(" ",end="")
            print()
        else:
            for k in range(1,n):
                if(j-n==k-1):
                    print(chr(c1),end="")
                    c1+=1
                else:
                    print(" ",end="")
            for k in range(n,2*n):
                if(((j-n)+(k-n))==n):
                    print(chr(ch1),end="")
                    ch1+=1
                else:
                    print(" ",end="")
            print()
        
