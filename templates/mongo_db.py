import json

from pymongo import MongoClient


def get_mongo_client():
    return MongoClient('localhost', 27017)


DB_TE = 'te'
COLLECTION_TEMPLATE = 'template'


def insert(customer_id):
    client = get_mongo_client()

    db = client[DB_TE]
    collection = db[COLLECTION_TEMPLATE]

    data_to_insert = {
        "type": "customer",
        "entity": "entity",
        "law": "base",
    }
    cursor = db.template.aggregate([{'$match': {'customerId': 'system'}},
                                    {'$project': {'fields': 1, '_id': 0}},
                                    {'$unwind': '$fields'},
                                    {'$group': {'_id': '', 'fields': {'$push': '$fields'}}}])

    fields = list(cursor)[0]

    data_to_insert['fields'] = fields['fields']

    collection.update({"customerId": customer_id}, {'$set': data_to_insert}, upsert=True)


def fetch_customer_template(customer_id):
    client = get_mongo_client()

    db = client[DB_TE]
    collection = db[COLLECTION_TEMPLATE]
    cursor = collection.find_one({'customerId': customer_id})
    if not cursor:
        return

    cursor.pop('_id')
    return cursor



