FROM python:3.10-alpine AS base
WORKDIR /project
COPY . .
RUN pip3 install -r requirements.txt

FROM base AS test
CMD ["python3", "-m", "coverage", "run" ,"-m", "pytest", "tests"]

FROM base AS prod
CMD ["python3", "main.py"]
