try:
    age=int(input("Enter the age: "))
except ValueError as e:
    print("Error Occured")
    print(e)
print("Are you dumb ?")

try:
    print(age)
except NameError as e:
    print("No Issues")
    print(e)

print("exception handled well")