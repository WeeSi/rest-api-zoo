import pymongo
# Connecting to mondodb compass
# MongoDB compass local host URL. You can replace the SRV string if you are connecting with mongodb atlas
connection_url = "mongodb://localhost:27017/"
client = pymongo.MongoClient(connection_url)
client.list_database_names()  # listing the available databases

database_name = "ISITECH-ANIMALS"
zoo_db = client[database_name]
collections_name = ['accommodation',
                    'visit-route',
                    'baie-des-otaries',
                    'espace-griffes-et-crocs',
                    'ferme-et-loenie',
                    'plaine-africaine',
                    'serre-de-minus',
                    'foret-nord-americaine']

accommodation_collection = zoo_db[collections_name[0]]
visitRoute_collection = zoo_db[collections_name[1]]
baie_des_otaries_collection = zoo_db[collections_name[2]]
espace_griffes_et_crocs_collection = zoo_db[collections_name[3]]
ferme_et_loenie_collection = zoo_db[collections_name[4]]
plaine_africaine_collection = zoo_db[collections_name[5]]
# serre_de_minus_collection = zoo_db[collections_name[6]]
# foret_nord_americaine_collection = zoo_db[collections_name[7]]

document = [{
    "type": "A",
    "Keeper": "Franck Ehui"
},
    {
    "type": "B",
    "Keeper": "Alexis Brossette"
},
    {
    "type": "C",
    "Keeper": "Julien B"
},
    {
    "type": "D",
    "Keeper": "Julien C"
},
    {
    "type": "E",
    "Keeper": "Pauline"
},
    {
    "type": "F",
    "Keeper": "Francis"
}]

accommodation_collection.insert_many(document);

document = [{
    "type" : "A",
    "Name" : "Tiger"
},
{
    "type" : "B",
    "Name" : "Lion"
},
{
    "type" : "C",
    "Name" : "hippopotamus"
},
{
    "type" : "D",
    "Name" : "Monkey"
},
{
    "type" : "E",
    "Name" : "Birds"
}]

visitRoute_collection.insert_many(document)

document = [{
    "type" : "Arctocephalus",
    "color" : "Brune à noire",
},
{
    "type" : "Callorhinus",
    "color" : "Brun clair ou gris"
},
{
    "type" : "Eumetopias",
    "color" : "Brune à noire"
},
{
    "type" : "Neophoca",
    "color" : "Brune à noire"
}]

baie_des_otaries_collection.insert_many(document)

document = [{
    "type" : "Tigres",
},
{
    "type" : "Lion",
},
{
    "type" : "Eumetopias",
},
{
    "type" : "Cerf",
},
{
    "type" : "Léopard",
}]

espace_griffes_et_crocs_collection.insert_many(document)

document = [{
    "type" : " Vache",
},
{
    "type" : "Brebis",
},
{
    "type" : "Mouton",
},
{
    "type" : "Poule",
}]

ferme_et_loenie_collection.insert_many(document)

document = [{
    "type" : "Girafe",
},
{
    "type" : "Elephant",
},
{
    "type" : "Rhinocéros",
}]

plaine_africaine_collection.insert_many(document)

# update
newvalues = { "$set": { 'color': "Marron" } }
baie_des_otaries_collection.update_many({"type" : "Arctocephalus"}, newvalues)

# delete
baie_des_otaries_collection.delete_many({"type" : "Eumetopias"})