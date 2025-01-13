from pymongo import MongoClient
from datetime import datetime

# Connect to MongoDB
client = MongoClient('mongodb://localhost:27017/')
db = client['chat_system']
messages_collection = db['messages']

# Function to store a message in MongoDB
def store_message(user_id, message, room_id):
    message_data = {
        "user_id": user_id,
        "message": message,
        "timestamp": datetime.utcnow(),
        "room_id": room_id
    }
    messages_collection.insert_one(message_data)
    print(f"Stored message: {message}")

# Store a sample message
store_message("user123", "Hello, world!", "room1")

def get_messages(room_id):
    messages = messages_collection.find({"room_id": room_id}).sort("timestamp", 1)
    for message in messages:
        print(message)
        
# Retrieve messages from a specific room
get_messages("room1")
