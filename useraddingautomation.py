import os

def useradding():
    count =0
    while count < 5:
        username=input(f"Enter The username of user {count}: ")
        os.system(f"sudo useradd {username} ")
        count +=1

# useradding()
def deletinguser():
    confirm="Y"
    while confirm != "N":
        username=input("Enter the Username you want to delete: ")
        os.system(f"sudo userdel -r {username}")
        confirm=input("Do you want to delete more users? Answer Y/N").upper()

deletinguser()