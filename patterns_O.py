row=0
while row<=4:
    col=0
    while col<=4:
        if row==0 and col%5!=0 or row==4 and col%5!=0 or row!=5 and col==0 or row!=0 and col==4:
            print("*",end=" ")
        else:
            print(" ",end=" ")
        col=col+1
    row=row+1
    print()