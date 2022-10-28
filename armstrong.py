def sumofnumbers(hussain):
    sum=0
    while (hussain > 0):
        rem= hussain % 10
        sum = sum + (rem ** 3)
        hussain = hussain // 10
    return sum

valuetobechecked=153
x=sumofnumbers(valuetobechecked)

if valuetobechecked == x:
    print("ArmStrong's Number")
else:
    print("Nope")



#arulbroisagoodboy