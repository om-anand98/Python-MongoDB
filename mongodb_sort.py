# ----------------------------------------------------
# ----------------------------------------------------

# MONGODB BASIC - Finding one, all, specific fields

# ----------------------------------------------------
# ----------------------------------------------------

# pymongo or mongoengine can be
# used as connectors
import pymongo as mdb

# mongodb connection
client = mdb.MongoClient(host='127.0.0.1', port=27017)
# print(client)

# print databases present in mongodb at present
print(f'\n Databases List : {client.list_database_names()}')

# ----------------------------------------------------

# using database if exists
# creating (virtually) if doesn't exist
# not created until data goes into it
demodb = 'demodb'
db = client[demodb]
# using demodb database

# print collections present in database
print(f'\n Collections in {demodb} : {db.list_collection_names()}')

# ----------------------------------------------------

# using collection if exists
# creating (virtually) if it doesn't exist
# not created until data goes into it
# collections= tables (MySQL)
collection = db['democol']

# ----------------------------------------------------
# sort('column name', 1) #ascending DEF
# sort('column name', -1) #descending

sort_doc = collection.find(
    {}, {'_id': 0, 'first_name': 1, 'gender': 1}).sort('first_name', -1)
# sorting all documents by descending order of first name

print('\n Printing all Documents sorted in Descending Order of First Name : \n')
for document in sort_doc:
    print(document)
