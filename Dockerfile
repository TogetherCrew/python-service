FROM python:3.10-alpine AS base
WORKDIR /project
COPY . .
RUN pip3 install -r requirements.txt

FROM base AS test
CMD ["python3", "-m", "coverage", "run" ,"-m", "pytest", "tests"]

FROM base AS prod-server
CMD ["python3", "server.py"]

FROM base as prod-worker
CMD ["python3", "worker.py"]
