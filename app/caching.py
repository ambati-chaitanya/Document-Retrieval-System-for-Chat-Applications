# app/caching.py
import json

import redis

# Connect to Redis
cache = redis.StrictRedis(host='localhost', port=6379, db=0)

def cache_query(query, results):
    cache_key = f"query:{query}"
    cache.set(cache_key, json.dumps(results), ex=3600)  # Cache expires in 1 hour

def get_cached_results(query):
    cache_key = f"query:{query}"
    cached_results = cache.get(cache_key)
    return json.loads(cached_results) if cached_results else None
