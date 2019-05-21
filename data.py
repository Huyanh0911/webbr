from pymongo import MongoClient
from bson.objectid import ObjectId
from faker import Faker
from random import randint, choice
faker=Faker()

mongo_uri ="mongodb+srv://admin:admin@cluster0-i9y1y.mongodb.net/test?retryWrites=true"
client = MongoClient(mongo_uri) 
shoesdata = client.db_shoes

shoes_collection = shoesdata["my_data_shoes"]

# for i in range(20):
#     new_shoes = {
#         "name":choice(["Nike Kyrie 2","Under Armour Curry 4","Nike Lebron 13","Nike KD 9","Anta KT 4"]),
#         "price":choice(["150$","200$"]),
#         "size":choice(["39","40","41","42"]),
#     }
#     shoes_collection.insert_one(new_shoes)
#     print("Saving document{0}.....,".format(i+1))
        
        
        
