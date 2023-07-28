import os

from dotenv import load_dotenv
from tc_messageBroker import RabbitMQ
from tc_messageBroker.rabbit_mq.event import Event
from tc_messageBroker.rabbit_mq.queue import Queue

load_dotenv()

if __name__ == "__main__":
    broker_url = os.getenv("RABBIT_HOST")
    port = os.getenv("RABBIT_PORT")
    username = os.getenv("RABBIT_USER")
    password = os.getenv("RABBIT_PASSWORD")

    rabbit_mq = RabbitMQ(
        broker_url=broker_url, port=port, username=username, password=password
    )
