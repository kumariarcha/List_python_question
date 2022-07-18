# n=int(input("enter the num:-"))
# i=1
# l=[]
# while i<=n:
#     l.append(i)
#     i=i+1
# j=-1
# m=[]
# while j>=-len(l):
#     m.append(l[j])
#     j=j-1
# print(m)


l=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
i=0
a=1
b=[]
while i<len(l):
    c=l[i-a+i]
    b.append(c)
    a=a+1
    i=i+1
print(b)