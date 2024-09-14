# API with Redis Caching and Rate Limiting

![API Illustration](https://source.unsplash.com/1600x900/?technology,code)

## Overview

This project is a Python Flask application that demonstrates how to build an API with caching and rate limiting. The app integrates Redis for caching query results, uses SQLite for storing document embeddings and user data, and Celery for background tasks. This setup is ideal for applications needing efficient search capabilities and rate management.

## Features

- **Health Check Endpoint**: `/health` - Check if the API is running.
- **Search Endpoint**: `/search` - Search for documents, with caching and rate limiting.
- **Redis Caching**: Caches search results to improve performance.
- **Rate Limiting**: Limits the number of API requests per user.
- **Document Storage**: Uses SQLite to store document content and embeddings.
- **Background Scraping**: Uses Celery to scrape and process news articles.

![Flask Logo](https://flask.palletsprojects.com/en/2.0.x/_images/flask-logo.png)

## Requirements

- Docker
- Docker Compose

## Setup

### 1. Clone the Repository

```bash
git clone <repository-url>
cd <repository-directory>


### Adding Images to Your README

1. **API Illustration**: Find a relevant image on [Unsplash](https://unsplash.com/).
2. **Flask Logo**: Source from the official [Flask website](https://flask.palletsprojects.com/en/2.0.x/).
3. **SQLite Logo**: Download from the [official SQLite website](https://www.sqlite.org/).

**Note**: Replace placeholders like `<repository-url>`, `<repository-directory>`, and `[your-email@example.com]` with actual values relevant to your project. 

Feel free to adjust the text and images based on your project needs!
