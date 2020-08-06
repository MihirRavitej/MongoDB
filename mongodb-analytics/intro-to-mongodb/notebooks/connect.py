from pymongo import MongoClient
import sys
from pprint import pprint

print(sys.executable)

client = MongoClient(
    'mongodb+srv://admin:admin@cluster0.aenpq.mongodb.net/test?retryWrites=true&w=majority&ssl=true&ssl_cert_reqs=CERT_NONE')

print(client.test)


cursors = client.test.movies_initial.find({'language': 'Telugu'})

print(cursors)

for cursor in cursors:
    pprint(cursor)
