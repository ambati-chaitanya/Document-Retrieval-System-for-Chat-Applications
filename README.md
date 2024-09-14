# API with Redis Caching and Rate Limiting

Welcome to the API project! This project is a Python Flask application that demonstrates a RESTful API with Redis caching, rate limiting, and background scraping capabilities. It also integrates with a SQLite database to manage document embeddings and user request counts.

![API Overview](https://example.com/path/to/overview-image.png)  <!-- Replace with actual image URL -->

## Features

- **Health Check Endpoint**: `/health` - Verifies if the API is running.
- **Search Endpoint**: `/search` - Processes search queries, caches results, and applies rate limiting.
- **Redis Caching**: Caches search results to enhance performance.
- **Rate Limiting**: Limits API calls to prevent abuse.
- **Document Storage**: Saves document contents and embeddings in a SQLite database.
- **Background Scraping**: Uses Celery to scrape and store news articles in the database.

## Requirements

- **Docker** - For containerizing the application and dependencies.
- **Docker Compose** - To manage multi-container Docker applications.

## Getting Started

### 1. Clone the Repository

First, clone this repository to your local machine:

```bash
git clone <repository-url>
cd <repository-directory>
