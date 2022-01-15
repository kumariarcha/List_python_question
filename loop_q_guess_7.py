guess=int(input("enter the num:-"))
i=0
chance=5
while i<=5:
    num=int(input("enter the num:-"))
    if num==guess:
        print("you have won")
        break
    else:
        print("you have  chance")
    i=i+1
    chance=chance-1
    print(chance)




    
