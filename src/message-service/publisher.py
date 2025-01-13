import pika
from pymongo import MongoClient
from datetime import datetime
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

def send_message_to_rabbitmq(message):
    try:
        connection = pika.BlockingConnection(pika.ConnectionParameters('rabbitmq'))
        channel = connection.channel()

        # Declare a queue
        channel.queue_declare(queue='message_queue', durable=True)

        # Send message to the queue
        channel.basic_publish(
            exchange='',
            routing_key='message_queue',
            body=message,
            properties=pika.BasicProperties(
                delivery_mode=2,  # Make message persistent
            )
        )
        logger.info(f" [x] Sent {message}")
        connection.close()
    except Exception as e:
        logger.error(f"Failed to send message to RabbitMQ: {str(e)}")

# Example usage
message = "Hello, World!"
send_message_to_rabbitmq(message)
save_message_to_db(message)
