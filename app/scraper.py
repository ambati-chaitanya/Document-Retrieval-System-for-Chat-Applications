# app/scraper.py
import requests
from bs4 import BeautifulSoup
from celery import Celery

from app.database import Document, session

celery = Celery('scraper', broker='redis://localhost:6379/0')

@celery.task
def scrape_news():
    # Example scraping logic
    url = "https://example.com/news"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    articles = soup.find_all('article')
    for article in articles:
        content = article.get_text()
        # Generate embedding for content (using the same model as query encoding)
        embedding = encode_query(content)  # This should return a numpy array
        # Convert numpy array to string for storage
        embedding_str = ','.join(map(str, embedding))
        
        # Store in the database
        new_doc = Document(content=content, embedding=embedding_str)
        session.add(new_doc)

    session.commit()
