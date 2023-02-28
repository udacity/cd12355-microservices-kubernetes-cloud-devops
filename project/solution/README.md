# Solution Overview
* `analytics/` directory shouldn't contain anything new. This is just carried over from the starter. Students are not expected to modify the source code here. They may modify the port number that's set inside the application and as long as the application still works as expected, there shouldn't be any issues. The main thing to look for is the addition of a Dockerfile.

* `db/` directory shouldn't contain anything new. This is just carried over from the starter. Students may modify the seed scripts to add new users and tokens but they should not be modifying the table schema.

* `deployment/` directory should contain the Kubernetes configs used to deploy the app service and files for configuring its credentials and environment variables. The `db-configmap.yaml` should contain an actual endpoint that corresponds with the database name created with Helm. This can be cross-referenced with the screenshot that the student provides of the `kubectl svc` command.