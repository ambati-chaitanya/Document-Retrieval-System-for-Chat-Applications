# app/query_encoder.py
from sentence_transformers import SentenceTransformer

# Load a pre-trained sentence transformer model
model = SentenceTransformer('all-MiniLM-L6-v2')

def encode_query(query):
    # Encode query to get a vector representation
    query_vector = model.encode(query)
    return query_vector
