#mongoDB mini project Phase 1
#import a json file, which records all the airports information in the world, into mongoDB
from pymongo import MongoClient
import json
import bson

client = MongoClient()
db = client.airports.database
posts = db.posts
collection = db.airports_collection


inputfile = open('airports.json','r')
	result = json.loads(inputfile.read())
	for info in result:
		posts.insert_one(info)
