#!/usr/bin/env python3
""" Python function that lists all documents in a collection """
import pymongo


def list_all(mongo_collection):
    """Lists all documents in a collection.

    Args:
      mongo_collection: A pymongo collection object.

    Returns:
      A list of all documents in the collection.
    """

    if mongo_collection is None:
        return []
    else:
        return list(mongo_collection.find())
