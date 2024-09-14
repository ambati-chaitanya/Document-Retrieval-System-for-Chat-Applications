# Document Retrieval System for Chat Applications

## Overview

The **Document Retrieval System for Chat Applications** is a Python-based application designed to retrieve and process documents to provide context for large language models (LLMs). This system utilizes Redis for caching, implements rate limiting, and stores document embeddings in a SQLite database. It also supports background tasks for scraping news articles using Celery.

## Features

- **Health Check Endpoint**: `/health` - Verifies if the API is running.
- **Search Endpoint**: `/search` - Accepts a query and user ID, performs a search, and caches results with rate limiting.
- **Redis Caching**: Caches search results to enhance performance.
- **Rate Limiting**: Limits API requests to prevent abuse.
- **Document Storage**: Stores document content and embeddings in a SQLite database.
- **Background Scraping**: Uses Celery to scrape news articles and update the database.
  
![Flask Logo](https://flask.palletsprojects.com/en/2.0.x/_images/flask-logo.png)

## Requirements

- Docker
- Docker Compose
- Redis
- Python 3.9
- Celery
- Flask
- SQLAlchemy
- Redis Python client
- Sentence Transformers
- BeautifulSoup4
- Requests

## Project Structure

- `app/caching.py`: Handles caching of search results using Redis.
- `app/database.py`: Manages SQLite database interactions.
- `app/query_encoder.py`: Encodes queries into vector representations.
- `app/scraper.py`: Background task for scraping news articles.
- `app/search.py`: Performs the search and retrieval logic.
- `Dockerfile`: Defines the Docker image for the application.
- `docker-compose.yml`: Defines the services (app and Redis) for the application.

## Setup Instructions

### 1. Clone the Repository

```bash
git clone <repository-url>
cd Document-Retrieval-System-for-Chat-Applications
