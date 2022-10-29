#Method 1 

# num1=int(input("Enter the value of first: "))
# num2=int(input("Enter the value of second: "))
# num3=int(input("Enter the value of third: "))

# if num1>num2:
#     if num1>num3:
#         print("Num1 is the Largest")
#     else:
#         print("Num3 is the largest")

# elif num2>num3:
#     print("Num2 is bigger")
# else:
#     print("Num3 is bigger")


#Method2
num1=int(input("Enter the value of first: "))
num2=int(input("Enter the value of second: "))
num3=int(input("Enter the value of third: "))

if (num1>num2) and (num1>num3):
    print("Num1is bigger")
elif (num2>num3) and (num2>num1):
    print("Num2 is bugger")
else:
    print("Num3 is bigger")