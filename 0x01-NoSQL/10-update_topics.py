#!/usr/bin/env python3
""" Change all topics of a school document based on the name """


def update_topics(mongo_collection, name, topics):
    """Changes all topics of a school document based on the name.

    Args:
      mongo_collection: A pymongo collection object.
      name (string): The school name to update.
      topics (list of strings): The list of topics approached in the school.
    """

    query = {'name': name}
    update = {'$set': {'topics': topics}}

    mongo_collection.update_many(query, update)
