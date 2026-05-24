# Use a lightweight Python base image from AWS ECR to avoid Docker Hub rate limits
FROM public.ecr.aws/docker/library/python:3.12-slim

# Set the working directory in the container
WORKDIR /app

# Copy the local repository contents to the container
COPY . /app/

# Set the default command to start a bash session
# This allows students to interactively explore and run scripts
CMD ["bash"]
