import json
jsondict={
    "Aruljothi":1,
    "HussainBasha":2.5,
    "Vishal":["Gupta",21,"Male"],
    "Prasiddh":{
        "Surname":"Saxena",
        "Profession":"Cyber Crime Investigation"
    },
}

with open("tryingjson.json","w") as file:
    json.dump(jsondict,file,indent=4)



print(jsondict["Prasiddh"]["Profession"])
print(jsondict["Vishal"][2])