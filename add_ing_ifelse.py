# i=1
# while i<=100:
#     print(i)
#     i=i+1
#     if i==50:
#         continuei

# i=1
# while i<=5:
#     print("*"*i)
#     i=i+1


user=str(input("enter the word"))
if "ing" not in user:
    print(user+"ing")
elif "ing" in user:
    print(user+"ly")
else:
    print(user)