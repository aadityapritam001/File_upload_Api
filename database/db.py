import pymongo
from pymongo import MongoClient
from bson.objectid import ObjectId

clust=MongoClient(<put your db url here>)
db=clust[<DB name here>]
collection=db['resume_detail']


def insert(file_path):
    access=retrieve(collection)
    x=collection.insert_one({'path':file_path})
    return file_path


def retrieve(collection):
    all_details=[]
    for info in collection.find():
        all_details.append(info)
    return all_details
