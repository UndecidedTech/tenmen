#babynames
#from bson import ObjectId (unique ids)
#create array of objects containing object id,firstname,lastname,username,email
import string
import random 
import os
import requests
import json
from bson import ObjectId
names = ["Emily","Hannah","Madison","Ashley","Sarah","Alexis","Samantha","Jessica","Elizabeth","Taylor","Lauren","Alyssa","Kayla","Abigail","Brianna","Olivia","Emma","Megan","Grace","Victoria","Rachel","Anna","Sydney","Destiny"]

def createusers(names):
    url = 'https://localhost:5000/user'
    headers = {'content-type': 'application/json'}
 
    r = requests.post(url, data=json.dumps(payload), headers=headers)
    users = []
    for i in range(len(names)):
        user = {}
        user["password"]= names[i] + str(os.urandom(2))
        user["firstname"] = names[i]
        user["id"] = ObjectId()
        if i == (len(names)-1):
            user["lastname"] = names[0]
        else:
            user["lastname"] = names[i+1]
        r.requests.post(url, data=json.dumps(user), headers=headers)
        users.append(user)
    print( users )
createusers(names)
# remember tocall ur function at the end or else nothing will run
# objects "object= {} is an object"
# to create a property within {} object["theobjectproperty"]
# emily = {}
# emily["firstname"] = emily
# emily["lastname"]= Hannah
# emily["id"] = randomnumber
#  ---------equivalent--------
# #  how data is perceived
# emily = {
#     "firstname": "emily",
#     "lastname": "hannah",
#     "id": '5e13f2a31cc55631bce76b7a'
# }   