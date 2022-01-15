n=5
i=1
while i<=n:
    j=1
    while j<=i:
        if i%2!=0:
            print(j,end="")
            j=j+1
        else:
            print("*",end="")
            j=j+1
    i=i+1
    print()
