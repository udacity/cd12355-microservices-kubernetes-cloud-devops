1. Build Docker Image
```bash
docker build .
```

2. Run the Docker Image
```bash
docker run <IMAGE_NAME>
```

3. Create an ECR Repository for the Image in AWS Console

4. Tag the Docker Image
```bash
docker tag <IMAGE_NAME> aws_account_id.dkr.ecr.region.amazonaws.com/<REPOSITORY_NAME>:<VERSION>
```

5. Log Into ECR
You only need to do this once every 12 hours so you don't need to run this every push.
```bash
aws ecr get-login-password --region region | docker login --username AWS --password-stdin aws_account_id.dkr.ecr.region.amazonaws.com
```

6. Push the Docker Image
```bash
docker push aws_account_id.dkr.ecr.region.amazonaws.com/<REPOSITORY_NAME>:<VERSION>
```
