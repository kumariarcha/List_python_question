# from tkinter import N


n=input("enter the string:-")
lenght=len(n)
# for row in range(lenght):
#     for col in range(row+1):
#         print(n[col],end=" ")
#     print()

row=1
while row<=n:
    col=1
    while col<=row:
        print(str(col),end=" ")
        col=col+1
    print()
    row=row+1
