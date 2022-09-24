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

# delete one
query = {'gender': 'Female'}

# deletes the first instance (if multiple)
collection.delete_one(query)

# delete many
query_regex = {'gender': {'$regex': '^M'}}

# deletes all instances where query matches
delete_doc = collection.delete_many(query_regex)

# no. of documents deleted
# delete_doc.deleted_count

# delete all
delete_doc = collection.delete_many({})
