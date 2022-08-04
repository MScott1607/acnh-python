import requests
import json


#I just want to view all fish data in a nicely formatted way


allfish = requests.get("http://acnhapi.com/v1/fish/")
print(allfish.status_code)

def jprint(formatted):
    text=json.dumps(formatted, sort_keys=True, indent=4)
    print(text)

jprint(allfish.json())

 # allfish['availability']['month-array-northern'] == inputmonth