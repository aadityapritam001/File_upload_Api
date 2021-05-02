import pymongo
from pymongo import MongoClient
from bson.objectid import ObjectId

clust=MongoClient('mongodb+srv://aaditya:1234567890@cluster0.6qbpm.mongodb.net/resume_data?retryWrites=true&w=majority')
db=clust['resume_data']
collection=db['resume_detail']


def insert(all_file):
    x=collection.insert_many(all_file)
    return x.inserted_ids


def retrieve(collection):
    all_details=[]
    for info in collection.find():
        all_details.append(info)
    return all_details