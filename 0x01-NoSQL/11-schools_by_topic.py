#!/usr/bin/env python3
"""
list of school
"""
import pymongo


def schools_by_topic(mongo_collection, topic):
    """Returns the list of schools having a specific topic.

    Args:
      mongo_collection: A pymongo collection object.
      topic (string): The topic to search for.

    Returns:
      A list of schools that have the given topic.
    """

    query = {'topics': topic}
    schools = mongo_collection.find(query)

    return list(schools)
