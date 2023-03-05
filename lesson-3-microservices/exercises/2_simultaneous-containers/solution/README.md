1. Do you think this is an efficient process?
2. What are your thoughts about deploying multiple containers manually like this in a large organization with frequent deployments?
3. Is the order in which you run the containers significant?

Deploying this way is an inefficient process. There are many manual steps that introduce room for error. Since this process is so manual and cumbersome, an organization that has a lot of deployments has increased risk from human error. Services don't exist independently of one another and services could have relationships where one depends on another. For example, the database container needs to be started before the API service containers can be started.
