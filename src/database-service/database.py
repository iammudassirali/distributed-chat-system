from pymongo import MongoClient
import logging

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# MongoDB connection setup
client = MongoClient('mongodb://database-service:27017/')
db = client['chat_database']
messages_collection = db['messages']

def save_message_to_db(message):
    try:
        message_data = {
            'message': message,
            'timestamp': datetime.utcnow()
        }
        messages_collection.insert_one(message_data)
        logger.info(f"Message saved to database: {message}")
    except Exception as e:
        logger.error(f"Failed to save message to database: {str(e)}")

def get_all_messages():
    try:
        messages = messages_collection.find()
        return list(messages)
    except Exception as e:
        logger.error(f"Failed to retrieve messages from database: {str(e)}")
        return []

# Example usage
message = "Test message"
save_message_to_db(message)
