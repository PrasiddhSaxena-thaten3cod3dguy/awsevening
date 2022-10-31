insulin={
    "Insulin1":5,
    "Insulin2":7,
    "Insulin3":11
}

# print(insulin["Insulin3"])


thekeys=list(insulin.keys())


sum=0
for i in thekeys:
    sum += insulin[i]


print(sum)

# print(thekeys)
# print(type(thekeys))
