#!/usr/bin/env python3
"""Redis with Requests"""
import requests
import redis


# Connect to Redis
r = redis.Redis()

def get_page(url: str) -> str:
    """
    Get the HTML content of a particular URL.

    Args:
        url: The URL to fetch.

    Returns:
        The HTML content of the URL.
    """

    # Increment the access count for the URL
    r.incr("count:{}".format(url))

    # Check if the HTML content is cached
    cached_html = r.get("html:{}".format(url))
    if cached_html is not None:
        return cached_html.decode()

    # Fetch the HTML content of the URL
    response = requests.get(url)
    html = response.content

    # Cache the HTML content for 10 seconds
    r.set("html:{}".format(url), html, ex=10)

    return html

