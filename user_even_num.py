n=int(input("enter the num:-"))
i=1
while i<=n:
    if n%2==0:
        a=n-2
        b=a-2
        print(a)
        print(b)
        break
    elif n%2!=0:
        a=n+2
        b=a+2
        print(a)
        print(b)
        break
    i=i+1