# i=5
# while i>=1:
#     j=1
#     while j<=i:
#         print("*",end=" ")
#         j=j+1
#     print()
#     i=i-1


# for row in range(7):
#     for col in  range(4):
#         if (row==0 or row==3 or row==6) and (0<col<3) or (col==0 and 0<row<3) or (col==3 and 3<row<6):
#             print("*",end=" ")
#         else:
#             print(end="  ")
#     print()


row=0
while row<=7:
    col=0
    while col<=7:
        if (row==0 or row==3 or row==6) and (0<col<3) or (col==0 and 0<row<3) or (col==3 and 3<row<6):
            print("*",end=" ")
        else:
            print(end="  ")
        col=col+1
    row=row+1
    print()

    