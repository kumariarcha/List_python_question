i=0
while i<6:
    j=0
    while j<6:
        if (i==0 or i==2 ) or (j==0) and (i!=0 and i!=2):
            print("*",end=" ")
        else:
            print(end="")
        j=j+1
    print()
    i=i+1