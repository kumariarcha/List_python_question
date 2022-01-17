row=0
while row<6:
    col=0
    while col<6:
        if col==1 or col==5 or row==3 and col>1 and col<6:
            print("*",end=" ")
        else:
            print(" ",end=" ")
        col=col+1
    row=row+1
    print()
