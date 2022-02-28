import pymongo
connection_url = "mongodb://localhost:27017/"
conn = pymongo.MongoClient(connection_url)

database_name = "ISITECH-ANIMALS"
db = conn[database_name]