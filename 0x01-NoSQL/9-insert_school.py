#!/usr/bin/env python3
""" Insert a document in Python """


def insert_school(mongo_collection, **kwargs):
    """Inserts a new document in a collection based on kwargs.

    Args:
      mongo_collection: A pymongo collection object.
      **kwargs: Keyword arguments to be used as the fields of the new document.

    Returns:
      The new _id of the document.
    """

    new_document = {}
    for key, value in kwargs.items():
        new_document[key] = value

    result = mongo_collection.insert_one(new_document)
    return result.inserted_id
