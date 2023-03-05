# AWS CodeBuild
CodeBuild is a straightforward way to implemented *continuous integration (CI)* to automate Docker image builds. We will want to 

While CodeBuild is not the most popular build tool, its simplicity and accessibility is a great way to introduce CI processes. Learning how to use CodeBuild will provide a lot of redundant skills that are transferrable to other CI tools and platforms.

## Instructions
1. Copy the starter code into a GitHub repository that you own. You may need to create a new GitHub repository.
2. Set up an AWS CodeBuild pipeline that has access to pull from this GitHub repository.
3. Create a new ECR repository for this project.
4. Create a `buildspec.yml` file that builds and pushes a Docker image to ECR. Store it in the root of your GitHub repository.
5. Run the build!
