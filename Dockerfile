# It's recommended that we use `bullseye` for Python (alpine isn't suitable as it conflcts with numpy)
FROM python:3.10-bullseye AS base 
WORKDIR /project
COPY . .
RUN pip3 install -r requirements.txt

FROM base AS test
RUN python3 -m coverage run -m pytest tests
CMD ["python3", "-m", "coverage", "lcov" ,"-o", "coverage/coverage.lcov"]

FROM base AS prod-server
CMD ["python3", "server.py"]

FROM base as prod-worker
CMD ["python3", "worker.py"]
