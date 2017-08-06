import json
import random
import time

import pika

from .settings import work_queue, status_queue

def main():
    connection = pika.BlockingConnection(pika.ConnectionParameters('messaging'))
    work_orders = connection.channel()
    work_orders.queue_declare(work_queue)
    status = connection.channel()
    status.queue_declare(status_queue)

    def callback(ch, method, properties, body):
        time.sleep(random.randint(0, 20))
        print(' [x] Good job')
        time.sleep(random.randint(0, 20))
        status.basic_publish(
            exchange='',
            routing_key=status_queue,
            body=json.dumps({
                'id': json.loads(body).get('job_id') or 'no-id',
                'status': 'complete'
            })
        )

    work_orders.basic_consume(callback, queue=work_queue, no_ack=True)
    work_orders.start_consuming()
