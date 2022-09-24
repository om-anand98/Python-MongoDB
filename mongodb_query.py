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
# query for single document/record

query = {'gender': 'Female'}

query_doc = collection.find(query, {'_id': 0, 'first_name': 1, 'gender': 1})

print('\n Query to print all Documents with Gender "Female" : \n')
for document in query_doc:
    print(document)

# ----------------------------------------------------
# query using regular expressions
# query for gender starting with 'M'
# More regex : https://www.w3schools.com/python/python_regex.asp

query_regex = {'gender': {'$regex': '^M'}}

query_regex_doc = collection.find(
    query_regex, {'_id': 0, 'first_name': 1, 'gender': 1})

print('\n Query to print all Documents with Gender "Male" using RegEx : \n')
for document in query_regex_doc:
    print(document)
