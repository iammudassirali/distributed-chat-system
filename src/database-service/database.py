from pymongo import MongoClient
from datetime import datetime

client = MongoClient('mongodb://localhost:27017/')
db = client['chat_system']
messages_collection = db['messages']

def store_message(user_id, message, room_id):
    msg = {
        "user_id": user_id,
        "message": message,
        "timestamp": datetime.utcnow(),
        "room_id": room_id
    }
    messages_collection.insert_one(msg)
    print(f"Stored message: {message}")

def get_messages(room_id):
    messages = messages_collection.find({"room_id": room_id}).sort("timestamp", 1)
    for message in messages:
        print(message)
