import json
import pika

from .settings import status_queue

def main():
    connection = pika.BlockingConnection(pika.ConnectionParameters('messaging'))
    status = connection.channel()
    status.queue_declare(status_queue)

    def callback(ch, method, properties, body):
        print(' [x] updating status for job {}'.format(
            json.loads(body).get('id')
        ))

    status.basic_consume(callback, queue=status_queue)
    status.start_consuming()
