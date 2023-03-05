# Using Docker File Exercise
This exercise is used to help reinforce your understanding of Dockerfiles, the Docker build process, and how Docker images are used.

This project uses a Debian image and runs a very simple Python script that prints "hello". The Dockerfile used in this project works but can be significantly improved.

## Improving the Build Process
The Dockerfile is unnecessarily complicated.

This existing Docker image installs Python on the image so that we can run Python. The way it sets up Python is by compiling it from source. This is complicated to write and exposes room for errors.

### Instructions
We want to improve the maintenance, runtime, and reliability of this by using a *base image*.

#### 1. Build the Existin Docker Image
```bash
docker build . -t starter-image --no-cache
```
Take note of how long it took to build the image.

#### 3. Use a Base Image
Replace the *base image* used in the starter Dockerfile with a Debian-based Python 3.10 base image. Remove the extra code used to set up `python`.

#### 4. Build the New Image
```bash
docker build . -t updated-image --no-cache
```
Take note of how long it took to build the image.

To confirm whether or not the image works properly, run:
```bash
docker run <IMAGE_NAME>

OR

docker run updated-image
```
The created container should print `hello!` and exit itself. There should be no errors on the screen.

#### 5. Comparisons
Then run the following command and take note of the size of the old and new images.
```bash
docker images
```

Note the differences of build time and image size.
