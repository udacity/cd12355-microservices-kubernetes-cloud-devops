# Solution

* Run the commands (replace `my-repo` and `my-release` with applicable names)
```bash
helm repo add demo-redis https://charts.bitnami.com/bitnami
helm install --set master.persistence.enabled=false --set replica.replicaCount=1 --set replica.persistence.enabled=false demo-redis demo-repo/redis
```

* This will show the Redis pod being created
```bash
kubectl get pods
```

* Retrieve the password
```bash
export REDIS_PASSWORD=$(kubectl get secret --namespace default redis -o jsonpath="{.data.redis-password}" | base64 -d)
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

* Cleanup
```bash
helm delete demo-redis
```