# Simple Docker App Demo
This example demonstrates a very basic Docker application. It builds an image off of a trivial Python Flask application.

## Running the Demo
Running locally without using Docker:
```bash
pip install -r requirements.txt
python app.py
```

Building as a Docker image:
```bash
docker build .
```

Running a Docker container:
```bash
docker run <IMAGE_NAME>
```
