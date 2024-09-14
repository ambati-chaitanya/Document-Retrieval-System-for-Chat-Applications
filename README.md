# API with Redis Caching and Rate Limiting

## Overview

This project is a Python Flask application with Redis caching and rate limiting. It includes a Celery worker for background tasks like scraping news articles and a SQLite database to store document embeddings and user API usage information.

## Features

- **Health Check Endpoint**: `/health` - Check the status of the API.
- **Search Endpoint**: `/search` - Perform a search with rate limiting and caching.
- **Redis Caching**: Cache search results to improve performance.
- **Rate Limiting**: Limit the number of API calls per minute per user.
- **Document Storage**: Store document content and embeddings in a SQLite database.
- **Background Scraping**: Scrape and process news articles using Celery.

## Prerequisites

- **Docker**: Ensure Docker is installed on your machine.
- **Docker Compose**: Required to run multi-container Docker applications.

## Setup

Follow these steps to get the project running:

1. **Clone the Repository**

   ```bash
   git clone <repository-url>
   cd <repository-directory>
