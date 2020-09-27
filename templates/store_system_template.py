import json

from templates import mongo_db
from templates.mongo_db import get_mongo_client


def add_system_templates():
    client = get_mongo_client()

    db = client[mongo_db.DB_TE]
    collection = db[mongo_db.COLLECTION_TEMPLATE]

    with open('template_examples.json') as f:
        file_data = json.load(f)

    for f in file_data:
        collection.insert(f)
    client.close()


if __name__ == '__main__':
    add_system_templates()
