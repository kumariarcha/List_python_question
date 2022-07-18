a=[["g","f","g"],["i","s"],["b","e","s","t"]]
i=0
b=[]
c=""
while i<len(a):
    b.extend(a[i])
    i=i+1
j=0
while j<len(b):
    c+=b[j]
    j=j+1
print(c)






