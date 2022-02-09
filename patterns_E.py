i=0
while i<7:
    j=0
    while j<7:
        if (i==0 or i==3 or i==6) or (j==0) and (i!=0 and i!=3):
            print("*",end="")
        else:
            print(end=" ")
        j=j+1
    print()
    i=i+1



