import pymongo

# Connecting to mondodb compass
# MongoDB compass local host URL. You can replace the SRV string if you are connecting with mongodb atlas
connection_url = "mongodb://localhost:27017/"
client = pymongo.MongoClient(connection_url)
client.list_database_names()  # listing the available databases

database_name = "ISITECH-ANIMALS"
zoo_db = client[database_name]

def collection_baie_des_otaries():
    return zoo_db['baie-des-otaries']