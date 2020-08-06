from pymongo import MongoClient
from pprint import pprint

client = MongoClient(
    'mongodb+srv://admin:admin@cluster0.aenpq.mongodb.net/test?retryWrites=true&w=majority&ssl=true&ssl_cert_reqs=CERT_NONE')

pipeline = [
    {
        '$group': {
            '_id': {'language': '$language'},
            'count': {'$sum': 1}
        }
    },
    {
        '$sort': {'count': -1}
    }
]

# Or

pipeline1 = [
    {
        '$sortByCount': '$language'
    }
]


pprint(list(client.test.movies_initial.aggregate(pipeline1)))
