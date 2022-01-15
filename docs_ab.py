# i=1
# k=1
# while i<=5:
#     b=1
#     while b<=5-i:
#         print(" ",end=" ")
#         b=b+1
#     j=1
#     while j<=k:
#         print(i,end=" ")
#         j=j+1
#     k=k+2
#     print()
#     i=i+1


# i=65
# k=65
# while i<=69:
#     b=65
#     while b<=69-i:
#         print(" ",end=" ")
#         b=b+1
#     j=65
#     while j<=k:
#         print(chr(i),end=" ")
#         j=j+1
#     k=k+2
#     print()
#     i=i+1


i=0
while i<5:
    print('  '*(4-i)+(chr(65+i)+' ')*((i*2)+1))
    i=i+1