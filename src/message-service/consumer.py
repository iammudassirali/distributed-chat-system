import pika
import json

# Function to handle the incoming message
def callback(ch, method, properties, body):
    message_data = json.loads(body)
    print(f" [x] Received: {message_data['message']} from user {message_data['user_id']} in room {message_data['room_id']}")

# Set up the connection to RabbitMQ
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

# Declare the same queue where messages are sent
channel.queue_declare(queue='chat_queue')

# Set up the consumer to listen to messages
channel.basic_consume(queue='chat_queue', on_message_callback=callback, auto_ack=True)

print(' [*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()
