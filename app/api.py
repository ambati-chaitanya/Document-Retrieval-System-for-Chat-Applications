from flask import Flask, jsonify, request
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address

app = Flask(__name__)

# Set up the rate limiter
limiter = Limiter(get_remote_address, app=app, default_limits=["5 per minute"])

@app.route('/health', methods=['GET'])
def health_check():
    return jsonify({"status": "API is running"})

@app.route('/search', methods=['POST'])
@limiter.limit("5 per minute")
def search():
    data = request.get_json()
    
    # Basic validation
    if not data or "text" not in data or "user_id" not in data:
        return jsonify({"error": "Invalid input, 'text' and 'user_id' are required"}), 400

    query = data.get("text", "")
    user_id = data.get("user_id", "")

    # Simplified: Replace this with the actual search logic
    results = {
        "query": query,
        "user_id": user_id,
        "results": ["doc1", "doc2", "doc3"]
    }

    return jsonify(results)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
