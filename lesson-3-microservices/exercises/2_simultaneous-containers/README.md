# Simultaneous Containers Exercise
This exercise demonstrates a very fundamental way of running multiple containers locally

You're provided with 3 directories that represents a microservice application. Each directory has code that has its own Dockerfile. Developers would be able to work on their code for their respective services and deploy their code independently of one another.

## Instructions
Build each of these applications as Docker images. One at a time, run the containers for these applications until you have 3 active Docker containers running. 

Make sure that the `starter` and `user` applications are running properly. You can query their `/health_check` endpoints with a GET request to verify.

Provide a text response of up to 5 sentences describing your opinion about the process. In your response, make sure you address the following points:
1. Do you think this is an efficient process?
2. What are your thoughts about deploying multiple containers manually like this in a large organization with frequent deployments?
3. Is the order in which you run the containers significant?
