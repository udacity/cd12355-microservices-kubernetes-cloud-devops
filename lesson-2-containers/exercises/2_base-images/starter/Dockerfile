FROM debian:buster-slim

# Install dependencies needed to compile Python
RUN apt update && apt install wget xz-utils make build-essential zlib1g-dev -y

# Compile Python from source
RUN wget https://www.python.org/ftp/python/3.10.9/Python-3.10.9.tar.xz && tar -xvf Python-3.10.9.tar.xz
RUN cd Python-3.10.9 && ./configure --enable-optimizations && make install -j $(nproc)

# Clean up build tools that are no longer needed
RUN apt remove wget xz-utils make build-essential zlib1g-dev -y

# Set up symlink so we can run `python` instead of `python3`
RUN ln -s $(which python3) /usr/local/bin/python

RUN echo "print('hello!')" > /say_hello.py

ENTRYPOINT python /say_hello.py