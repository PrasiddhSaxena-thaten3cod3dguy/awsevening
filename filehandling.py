# file=open("awsevening.txt","w")
# thedata="""
# Who is best,
# its me i guess 
# why my ops are in stress 
# its me i guess 
# """
# file.write(thedata)
# file.close()

# with open("awsevening.txt","r") as file:
#     thedata="Rhymeas are dimes"
#     file.writelines(thedata)

import json

# thedict={
#     "Lohit":1,
#     "Stephen":2,
#     "manvitha":3,
#     "Ankita":4
# }

# with open("tryingjson.json","w") as fp:
#     json.dump(thedict,fp,indent=4)


thefile=open("tryingjson.json","r")
data=json.loads(thefile.readlines())

print(data)

