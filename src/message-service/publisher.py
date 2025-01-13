import pika
import json

# Set up connection parameters to connect to RabbitMQ
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

# Declare a queue for message delivery
channel.queue_declare(queue='chat_queue')

# Define the message
message_data = {
    "user_id": "user123",
    "message": "Hello, this is a test message",
    "room_id": "room1",  # This could be a group or direct message
    "timestamp": "2025-01-12T12:00:00Z"
}

# Convert the message to a JSON string for better structure
message = json.dumps(message_data)

# Publish the message to the queue
channel.basic_publish(exchange='',
                      routing_key='chat_queue',
                      body=message)

print(f" [x] Sent: {message_data}")
connection.close()
