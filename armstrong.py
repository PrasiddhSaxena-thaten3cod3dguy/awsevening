def sumofnumbers(arul):
    sum=0
    while (arul > 0):
        rem= arul % 10
        sum = sum + (rem ** value_length)
        arul = arul // 10
    return sum

valuetobechecked=input("enter the number: ")
#to check the multi digit numbers
value_length=len(valuetobechecked) 
valuetobechecked=int(valuetobechecked)
x=sumofnumbers(valuetobechecked)

if valuetobechecked == x:
    print("ArmStrong's Number")
else:
    print("Nope")