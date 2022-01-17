row=0
while row<=5:
    col=0
    while col<5:
        if row==0 and col%4!=0 or row==3 and col%4!=0 or row!=0 and col==0 or row!=0 and col==4:
            print("*",end=" ")
        else:
            print(" ",end=" ")
        col=col+1
    row=row+1
    print()