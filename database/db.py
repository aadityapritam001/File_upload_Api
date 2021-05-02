import pymongo
from pymongo import MongoClient
from bson.objectid import ObjectId

clust=MongoClient(<Put your database url here>)
db=clust[<database name here>]
collection=db[<collection name here>]


def insert(all_file):
    x=collection.insert_many(all_file)
    return x.inserted_ids


def retrieve(collection):
    all_details=[]
    for info in collection.find():
        all_details.append(info)
    return all_details
