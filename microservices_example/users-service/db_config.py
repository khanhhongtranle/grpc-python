import pymongo
from pymongo import MongoClient

DB_NAME = "users"
mongo_client = MongoClient('localhost', 27017)
db = mongo_client[DB_NAME]
