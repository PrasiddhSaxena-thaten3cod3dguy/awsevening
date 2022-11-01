# import os 
import subprocess
# for i in range(150):
#     os.system("echo 'blah' ")

# output=os.system("wmic product get name")
output=subprocess.check_output("wmic product get name")

print("Im a beast of all times ")
print(output)