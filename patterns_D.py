i=0
while i<6:
    j=0
    while j<6:
        if (i==0 or i==5) and j!=5 or (j==0 or j==5) and 0<i<5:
            print("*",end=" ")
        else:
            print(" ",end=" ")
        j=j+1
    print()
    i=i+1
      