import requests

try:
    data=requests.get("https://babablacksheephaveyouanywool.com")
    # print(data.text)
    # print(data.status_code)
    if data.status_code == 200:
        print(data.text)
    else:
        print("Somethis is off")
except Exception as e:
    print("Error Detected")