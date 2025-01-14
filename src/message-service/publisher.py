import pika
from pymongo import MongoClient
from datetime import datetime
import logging
from flask import Flask, jsonify
from flask_swagger_ui import get_swaggerui_blueprint

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# MongoDB connection setup
client = MongoClient('mongodb://database-service:27017/')
db = client['chat_database']
messages_collection = db['messages']

# Set up Flask app
app = Flask(__name__)

# Swagger configuration
SWAGGER_URL = '/swagger'  # URL for accessing Swagger UI
API_URL = '/static/swagger.json'  # Path to the Swagger JSON file
swagger_ui = get_swaggerui_blueprint(SWAGGER_URL, API_URL)

# Register Swagger UI blueprint
app.register_blueprint(swagger_ui, url_prefix=SWAGGER_URL)

# Define the API endpoints

@app.route('/api/v1/messages', methods=['GET'])
def get_messages():
    """
    Get all messages
    ---
    responses:
        200:
            description: List of messages
            content:
                application/json:
                    schema:
                        type: object
                        properties:
                            messages:
                                type: array
                                items:
                                    type: string
                                example: ["Hello", "Hi there"]
    """
    # Fetching all messages from the database
    messages = [message['message'] for message in messages_collection.find()]
    return jsonify({"messages": messages})

@app.route('/api/v1/messages', methods=['POST'])
def post_message():
    """
    Post a new message
    ---
    parameters:
        - name: message
          in: query
          type: string
          required: true
          description: The message to post
    responses:
        200:
            description: Message successfully posted
    """
    message = "New message posted"
    # Here, you can call your send_message_to_rabbitmq and save_message_to_db functions if needed.
    send_message_to_rabbitmq(message)
    save_message_to_db(message)
    return jsonify({"message": message})

# MongoDB and RabbitMQ functions remain unchanged
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

# Run the app
if __name__ == '__main__':
    app.run(debug=True)
