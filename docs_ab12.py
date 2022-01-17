i=1
while i<=6:
    j=1
    k=ord("A")        
    while j<=i:
        if i%2!=0:
            print(j,end=" ")
        else:
            print(chr[80],end=" ")
            j=j+1
            k=k+1
        print()
        i=i+1