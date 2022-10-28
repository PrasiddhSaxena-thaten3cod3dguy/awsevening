def reverse(number):
    rev=0
    while(number>0):
        rem=number % 10
        rev= rev * 10 + rem
        number = number // 10 
    return rev

def checkpalindrome(number):
    x=reverse(number)
    print(f"Reverse of number is {x}")
    print(f"original Number is {number}")
    if x == number:
        print("Palindrome")
    else:
        print("Nope")

checkpalindrome(133)