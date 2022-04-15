import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
from os import system

system("clear")
cred = credentials.Certificate("key.json")
firebase_admin.initialize_app(cred)

db=firestore.client()


#data={'surname':'Shadow'}
#db.collection('person').document('Desa').set(data,merge=True)

result=db.collection('person').where("name","==","Desa").get()

for i in result:
    print("Name:",i.to_dict()["name"],"Surname:",i.to_dict()["surname"],"Age:",i.to_dict()["Age"])