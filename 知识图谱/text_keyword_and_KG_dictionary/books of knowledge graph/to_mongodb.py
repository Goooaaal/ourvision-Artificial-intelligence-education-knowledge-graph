import pymongo
from pymongo import MongoClient


# 创建实例,连接数据库
client = MongoClient('47.75.70.164', 27017)
if client:
    print(True)



db = client['YJ_DB']
collection = list(db['books'].find())
for i in collection:
    print(i)
print(type(collection))