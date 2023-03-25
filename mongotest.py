import pymongo

client = pymongo.MongoClient("mongodb+srv://gnaneshwargnanu007:0w5cSXi78NQ8sEgu@cluster0.qbae7ca.mongodb.net/?retryWrites=true&w=majority")
db = client.test

print(db)

d = {
    "name":"gnane",
    "email" : "gnane@ineuron.ai",
    "surname" : "barla"
}
db1 = client['mongotest']
coll = db1['test']
coll.insert_one(d )