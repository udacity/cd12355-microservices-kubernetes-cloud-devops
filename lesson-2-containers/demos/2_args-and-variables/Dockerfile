# docker build . --build-arg BUILD_NUMBER="4"
# docker run -e WORDS="hello there" <IMAGE_ID>

FROM python:3.10-slim-buster

ARG BUILD_NUMBER

RUN echo "import os" > /say_something.py
RUN echo "print('Build Number: $BUILD_NUMBER')" >> /say_something.py
RUN echo "print(os.getenv('WORDS'))" >> /say_something.py

ENTRYPOINT python /say_something.py
