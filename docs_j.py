i=0
while i<=5:
    print(" "*(5-i),end=" ")
    j=0
    while j-1<i*2:
        if j+1>i+1:
            print((i*2)-j+1,end="")
        j=j+1
    print()
    i=i+1