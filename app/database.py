# app/database.py
import numpy as np
from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

Base = declarative_base()

class Document(Base):
    __tablename__ = 'documents'
    id = Column(Integer, primary_key=True)
    content = Column(String)
    embedding = Column(String)  # Store as string, later convert to numpy array

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    user_id = Column(String, unique=True)
    request_count = Column(Integer, default=1)

# Database setup
engine = create_engine('sqlite:///database.db')  # Replace with your database
Session = sessionmaker(bind=engine)
session = Session()

def init_db():
    Base.metadata.create_all(engine)  # Create tables

def get_document_embeddings():
    docs = session.query(Document).all()
    embeddings = [np.fromstring(doc.embedding, sep=',') for doc in docs]
    return {'vectors': embeddings, 'docs': docs}

def update_user_api_count(user_id):
    user = session.query(User).filter_by(user_id=user_id).first()
    if user:
        user.request_count += 1
    else:
        user = User(user_id=user_id, request_count=1)
        session.add(user)
    session.commit()

def check_rate_limit(user_id):
    user = session.query(User).filter_by(user_id=user_id).first()
    return user and user.request_count >= 5
