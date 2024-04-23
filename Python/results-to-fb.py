import json
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
from firebase_admin import firestore

cred = credentials.Certificate("digit-210-firebase-adminsdk-s0o5k-a0a46f9545.json")
firebase_admin.initialize_app(cred)

db = firestore.client()

doc_ref_article = db.collection(u'articles')

# File name of the JSON file
json_file = "results.json"

# Read the JSON file and parse its content into a Python dictionary
with open(json_file, "r") as file:
    data = json.load(file)

for key, value in data.items():
    doc_ref_article = db.collection(u'articles').add({
        u'text': key,
        u'neg': value.get("neg"),
        u'neu': value.get("neu"),
        u'pos': value.get("pos"),
        u'compound': value.get("compound"),
        u'date': value.get("date"),
        u'sentiment': value.get("sentiment")
         })
   
    # print(key)
    # print(value.get("compound"))
    # for v in value:
    #     print(v)
        
    # for k in key:
    #     print(k)
        
