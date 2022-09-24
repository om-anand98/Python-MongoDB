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

# finds first document
one_doc = collection.find_one()

print(f'\n Printing 1 Document : \n\n {one_doc}')

# ----------------------------------------------------

# finds all documents
# similar to select *
all_doc = collection.find()

print('\n Printing all Documents : \n')
for document in all_doc:
    print(document)

# ----------------------------------------------------

# finds specific columns of documents
# similar to select [column/s]
specific_all_doc = collection.find(
    {}, {'_id': 0, 'first_name': 1, 'gender': 1})
# 1 = include
# 0 = exclude
# mongodb internally assigns the visibility values
# if certain column is marked 0, then
# all other columns will be marked 1 and vice versa
# using 2 columns with 0 and 1 will throw an error
# NOTE : Doesn't apply to _id
# NOTE : is case sensitive so specify column names
# the same way as in original collection
# if the column doesn't exist no error is shown

print('\n Printing all Documents with specific columns : \n')
for document in specific_all_doc:
    print(document)

# ----------------------------------------------------
