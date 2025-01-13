import pika

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

channel.queue_declare(queue='chat_queue')

message = "Hello from user!"
channel.basic_publish(exchange='',
                      routing_key='chat_queue',
                      body=message)

print(f" [x] Sent {message}")
connection.close()
