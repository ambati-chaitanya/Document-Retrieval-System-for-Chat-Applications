# Flask API with Redis Caching, Rate Limiting, and Background Tasks

## Overview

This project is a Python-based Flask API with Redis caching, rate limiting, and background tasks using Celery. It includes a search functionality with vector embeddings for document similarity and utilizes a SQLite database to store documents and user request data.

## Features

- **Health Check Endpoint**: `/health` - Returns the status of the API.
- **Search Endpoint**: `/search` - Performs a search query, applies rate limits, and caches results.
- **Redis Caching**: Caches search results to improve performance.
- **Rate Limiting**: Limits the number of requests per user per minute.
- **Document Storage**: Uses SQLite to store document content and embeddings.
- **Background Scraping**: Scrapes news articles and stores them in the database using Celery.

## Setup

### Prerequisites

- Docker
- Docker Compose

### Getting Started

1. **Clone the Repository**

   ```bash
   git clone <repository-url>
   cd <repository-directory>
