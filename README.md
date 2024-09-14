# Python Flask API with Redis Caching, Rate Limiting, and Celery

## Overview

This project demonstrates a Python Flask application with Redis caching, rate limiting, and Celery for background tasks. It uses a SQLite database to store document embeddings and user API usage information. The application provides endpoints for health checks and search queries, while Celery handles news scraping tasks.

![Project Diagram](images/project-diagram.png)  <!-- Add a diagram of your project's architecture -->

## Features

- **Health Check Endpoint**: `/health` - Verifies if the API is running.
- **Search Endpoint**: `/search` - Allows users to perform searches with caching and rate limiting.
- **Redis Caching**: Caches search query results to improve performance.
- **Rate Limiting**: Limits API calls to 5 per minute per user.
- **Document Storage**: Stores document content and embeddings in a SQLite database.
- **Background Tasks**: Uses Celery to scrape news articles and process them.

## Prerequisites

- **Docker**: To containerize the application and its dependencies.
- **Docker Compose**: To manage multi-container Docker applications.

## Setup

### 1. Clone the Repository

```bash
git clone <repository-url>
cd <repository-directory>
