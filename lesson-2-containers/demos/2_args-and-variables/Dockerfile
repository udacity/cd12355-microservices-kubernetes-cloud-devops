# docker build . --build-arg AUTHOR=justin -t demo_args
# docker run demo_args -e "hi there"

FROM python:3.10-slim-buster

ARG AUTHOR
ENV WORDS=$WORDS

RUN echo "print('$BUILD_NUMBER: $WORDS')" > /say_something.py

ENTRYPOINT python /say_something.py
