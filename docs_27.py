# i=1
# while i<=5:
#     print(i*i,end=",")
#     i=i+1


n=int(input("enter the num:-"))
i=1
sum=0
while i<=n:
    num=i**2
    sum=sum+num
    i=i+1
    print(num)
print(sum)
