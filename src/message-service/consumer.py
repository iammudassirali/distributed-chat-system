import pika
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

def callback(ch, method, properties, body):
    message = body.decode()
    logger.info(f" [x] Received {message}")
    save_message_to_db(message)  # Save message to MongoDB

def consume_messages_from_rabbitmq():
    # Set up RabbitMQ consumer
    connection = pika.BlockingConnection(pika.ConnectionParameters('rabbitmq'))
    channel = connection.channel()

    # Declare the queue
    channel.queue_declare(queue='message_queue', durable=True)

    # Consume messages from the queue
    channel.basic_consume(queue='message_queue', on_message_callback=callback, auto_ack=True)

    logger.info(' [*] Waiting for messages. To exit press CTRL+C')
    channel.start_consuming()

# Start consuming messages
consume_messages_from_rabbitmq()
