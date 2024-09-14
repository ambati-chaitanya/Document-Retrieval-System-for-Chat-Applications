# app/search.py
import numpy as np

from app.caching import cache_query, get_cached_results
from app.database import (check_rate_limit, get_document_embeddings,
                          update_user_api_count)
from app.query_encoder import \
    encode_query  # Assume we have a query encoder module


def perform_search(query, user_id, top_k=5, threshold=0.5):
    if check_rate_limit(user_id):
        return {"error": "Rate limit exceeded"}, 429

    # Check cache first
    cached_results = get_cached_results(query)
    if cached_results:
        return cached_results, 200

    # Encode query into vector
    query_vector = encode_query(query)

    # Fetch document embeddings from the DB
    doc_embeddings = get_document_embeddings()
    
    # Normalize query vector
    query_vector = query_vector / np.linalg.norm(query_vector)

    # Normalize document vectors
    doc_vectors = [vec / np.linalg.norm(vec) for vec in doc_embeddings['vectors']]

    # Compute cosine similarity
    similarities = np.dot(doc_vectors, query_vector)

    # Filter results based on threshold
    results = [
        {
            "document": doc.content,
            "similarity": similarities[i]
        } 
        for i, doc in enumerate(doc_embeddings['docs']) 
        if similarities[i] >= threshold
    ]

    # Sort results by similarity and return top_k
    results = sorted(results, key=lambda x: -x['similarity'])[:top_k]

    # Cache query results
    cache_query(query, results)

    # Increment user API call count
    update_user_api_count(user_id)

    return results, 200
