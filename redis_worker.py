import os

import redis
from dotenv import load_dotenv
from rq import Worker
import logging

load_dotenv()

def worker_exception_handler(job, exc_type, exc_value, traceback):
    logging.error(" ========= RQ Exception =========")
    logging.error(f"JOB: {job}")
    logging.error(f"exc_type: {exc_type}")
    logging.error(f"exc_value: {exc_value}")
    logging.error(f"traceback: {traceback}")


if __name__ == "__main__":
    host = os.getenv("REDIS_HOST")
    port = os.getenv("REDIS_PORT")
    password = os.getenv("REDIS_PASSWORD")

    logging.basicConfig()
    logging.getLogger().setLevel(logging.INFO)

    redis_connection = redis.Redis(host=host, port=port, password=password)
    worker = Worker(
        queues=["default"], connection=redis_connection, exception_handlers=worker_exception_handler
    )
    try:
        worker.work(with_scheduler=True, max_jobs=1)
    except KeyboardInterrupt:
        worker.clean_registries()
        worker.stop_scheduler()