# API with Redis Caching and Rate Limiting

![API Overview](https://via.placeholder.com/800x400.png?text=API+Overview) <!-- Replace with actual image link -->

## Overview

This project is a Python Flask application that implements an API with caching and rate limiting features. It utilizes Redis for caching query results and a rate limiter to control API usage. The application also integrates with a SQLite database to store document embeddings and user API usage information. Additionally, it uses Celery for background tasks like scraping news articles.

## Features

- **Health Check Endpoint**: `/health` - Returns the status of the API.
- **Search Endpoint**: `/search` - Accepts a query and user ID, performs a search, caches results, and enforces rate limits.
- **Redis Caching**: Caches search query results to reduce computation time.
- **Rate Limiting**: Limits the number of API calls per minute per user.
- **Document Storage**: Stores document content and embeddings in a SQLite database.
- **Background Scraping**: Uses Celery to scrape and process news articles.

## Architecture

![Architecture Diagram](https://via.placeholder.com/800x400.png?text=Architecture+Diagram) <!-- Replace with actual image link -->

## Requirements

- Docker
- Docker Compose

## Setup

1. **Clone the Repository**

   ```bash
   git clone <repository-url>
   cd <repository-directory>
