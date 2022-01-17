
# n=input("enter the string:-")
# lenght=len(n)
# for row in range(lenght):
#     for col in range(row+1):
#         print(n[col],end=" ")
#     print()



a="python"
x=len(a)
i=0
while i<x:
    j=0
    while j<=i:
        print(a[j],end=" ")
        j=j+1
    print()
    i=i+1