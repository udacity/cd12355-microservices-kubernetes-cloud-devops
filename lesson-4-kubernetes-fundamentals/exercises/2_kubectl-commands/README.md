# kubectl Commands
`kubectl` is a very powerful tool that provides most of the functionality needed to interface with Kubernetes environments. While there are many other tools that can be used, `kubectl` has very few abstractions and understanding how to use it will help you be able to learn other tools very quickly.

It's unrealistic to go through every single `kubectl` command. In this exercise, we'll do some common operations with `kubectl` by referencing official documentation.

## Prerequisites
You should have the deployments and services in the `starter/deployment/` directory running. If you have done previous exercises, this is the same set of configurations from before.

You can set up the resources by running the following:
```bash
kubectl apply -f starter/deployment/
```

## Instructions
Given the official Kubernetes cheatsheet and simple tasks, identify and run the command to complete the task.

All commands can be constructed from the [kubectl cheatsheet](https://kubernetes.io/docs/reference/kubectl/cheatsheet/).

### 1. Retrieving YAML Configuration
If we wanted to retrieve information about a deployment, we can run the following command:
```bash
kubectl get deployment <DEPLOYMENT_NAME>
```

For our exercise, we can run the following to retrieve information about the User API deployment:
```bash
kubectl get deployment user-api
```

Sometimes, it can be useful to get the actual YAML configuration for the deployment.

**How can you modify this command to have it return the YAML configuration rather than the metadata for the `user-api` deployment?**

### 2. Copying Files
It can be useful to copy files to/from a pod. This is often done with log files that need to be pulled out from a container. Or a script that needs to be copied onto the container so that it can be run.

`starter/file_to_copy.sh` is a simple script that we want to run in our container. It simply prints a message and shows the filesystem usage.

For our exercise, we want to copy this into the main container running in the pod `user-api`.

**What command can we use to copy the `file_to_copy.sh` script into `user-api` into the `/tmp` directory?**

After it's been copied over, we can verify it by running the following:
```bash
kubectl exec -it <POD_NAME> bash /tmp/file_to_copy.sh
```
This should print out the filesystem information on the actual container that it's running on.

### 3. Deleting Resources
There are times when it's important to kill a running pod. If the pod was created through a deployment configuration, Kubernetes should recognize that the pod was killed and create a new pod to restore itself to a stable state.

**What command would I use to delete a pod for `user-api`?**

Once deleted, running the following should show the old pod being deleted and a new one being spawned:
```bash
kubectl get pods
```
