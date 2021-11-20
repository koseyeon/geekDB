from pymongo import MongoClient

client = MongoClient('localhost', 27017)

db = client['baedalgeek_test']
col = db['Users']
name = input()
age = int(input())
x = col.insert_one({"name":name, "age":age})

for k in col.find(): 
    print(k)

print(client.list_database_names())