# Kubernetes Configurations
This exercise focuses on creating and applying deployment files with Kubernetes.

The starter code contains a microservice application. It is deployed as 3 distinct services: a database, user API, and admin API.

You are given examples of deployment and service configurations in the starter code. For this exercise, you are to create and apply the Kubernetes service and deployment for the user API.

## Instructions
### 1. Apply the Existing Configs
Create the resources in your Kubernetes environment. Multiple deployments can be applied by running:
```bash
kubectl -f apply deployment/
```
### 2. Create User API Service and Deployment
Create a new file called user-api.yaml that contains the service and deployment definitions for the application.

### 3. Apply the User Service and Deployment
Create the service and deployment by applying your configurations
```bash
kubectl -f apply user-api.yaml
```

You can review the status of your apply with the following commands:
```bash
kubectl get services
kubectl get pods
```

Your pod should have a `Status` of `Running` if the configuration was successful.
