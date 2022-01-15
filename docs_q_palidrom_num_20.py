num=int(input("enter the num:-"))
a=0
i=num
while num<=0:
    a=(a*10)+num%10
    num=num//10
if i==num:
    print("this is palidrom num")
else:
    print("this is not palidrom num")
