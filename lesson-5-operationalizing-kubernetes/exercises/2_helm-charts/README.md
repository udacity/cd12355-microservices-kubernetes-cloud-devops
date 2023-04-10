# Helm Chart
This exercise focuses on setting up a Redis service with a Helm chart. The goal of this exercise is to not only set up a Helm chart, but to also go through a particular Helm chart's official documentation to get it up and running.

No Redis knowledge is required to complete this exercise. While there is an optional portion to connect and run commands against the Redis deployment, every command that you would need to run is already provided.

## Instructions
### 0. Capacity Management
Your cluster should be able to handle running Redis. If you find that your pods are in a `Pending` state for an extended period of time, you may need to increase the capacity of your cluster.

Setting your cluster with a node group that has 2 replicas of `m6g.large` should be sufficient.

Once you're done with the exercise, I recommend scaling back the capacity of your cluster to save costs.

### 1. Set Up Redis
Reference the following documentation to set up your Redis deployment using a Helm chart: https://artifacthub.io/packages/helm/bitnami/redis

Redis deployments can be complicated. In order to simplify Redis in this exercise:
* Set both the master and replica to use no persistence
* Set the replica count to 0

(Hint: the following flags are used to simplify your deployment)
```bash
--set master.persistence.enabled=false
--set replica.persistence.enabled=false
--set replica.replicaCount=1
```
Add this these flags right in between `helm install` and the rest of the command.

### 2. Check Redis is Running
Run `kubectl get pods`. You should see Redis pods have been configured.

### 3. (Optional) Query Against Redis
* Retrieve the password
```bash
export REDIS_PASSWORD=$(kubectl get secret --namespace default demo-redis -o jsonpath="{.data.redis-password}" | base64 -d)
```

* Connect to the Redis pod named `redis-master-?` so we can use the `redis-cli` tool without having to install it locally (simplifies the dependencies to run this exercise)
```bash
kubectl exec -it <POD_NAME> bash
```

* Run the following command to launch the Redis CLI
```bash
REDISCLI_AUTH=<PASTE_PASSWORD_HERE_THAT_WAS_STORED_IN_$REDIS_PASSWORD> redis-cli
```

* Run this command to set and get the value `helm_chart_exercise`
```bash
SET helm_chart_exercise incomplete
GET helm_chart_exercise
```

* Run this command to set and get a new value `helm_chart_exercise`
```bash
SET helm_chart_exercise complete!
GET helm_chart_exercise
```

### 4. Tear Down Redis
Reference the following documentation on how to destroy your Redis resource that was created with a Helm chart: https://artifacthub.io/packages/helm/bitnami/redis

And remember to scale back your cluster capacity!
