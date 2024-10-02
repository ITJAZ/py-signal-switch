from fastapi import FastAPI
from pymongo import MongoClient
import os

app = FastAPI()

mongo_user = os.getenv('MONGO_USER')
mongo_password = os.getenv('MONGO_PASSWORD')
mongo_host = os.getenv('MONGO_HOST', 'localhost')
mongo_port = os.getenv('MONGO_PORT')

@app.get('/hi')
def hi():
  try:
    client = MongoClient(f'mongodb://{mongo_user}:{mongo_password}@{mongo_host}:{mongo_port}')
    db = client.get_database('topics')

    collection = db.get_collection('bk')
    return collection.find().to_list()
  finally:
    client.close()