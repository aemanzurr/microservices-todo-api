# Microservices Project: Authentication and Tasks (DevOps Part)

## Description

This project consists of the development of a microservices based architecture using Python. It consists of two main services:

- **Authentication Service**: User management and authentication with JWT.
- **Task Service (To-Do List)**: Allows users to create, list, update and delete tasks.

The goal is to implement modern development principles, including containerization, orchestration and automated deployment in the cloud using DevOps tools.

## Technologies Used

- Python 
- Docker 
- kubectl 
- AWS 
- Terraform 

---

## Project Architecture

The project is composed of **four main pods** deployed on a Kubernetes cluster:

1. **auth-service**: exposes endpoints for login, registration and token validation.
2. **task-service**: enables CRUD operations on tasks associated with authenticated users.
3. **nginx**: acts as Ingress Controller (load balancer) and exposes services to the outside.
4. **db**: database that persists microservices information.

All services are:

- **Connected on the same network**, both in Docker and Kubernetes, allowing them to communicate securely internally.
- Configured with **environment variables** that specify the internal network addresses (hostnames and ports), facilitating the connection between microservices (e.g.: the task service knows how to communicate with the authentication service, and both with the database).

---

## DevOps Implementation Guide

### Prerequisites

- Active AWS account 
- Docker and kubectl installed 
- Terraform CLI installed 
- AWS CLI configured with credentials 

### Step 1: Clone the repository

bash
git clone https://github.com/tu-usuario/nombre-proyecto.git
cd project-name

### Step 2: Build the Docker images

Normally this is done inside the folder where you have the Dockerfile.

docker build . -t [IMAGE_NAME] mysql:latest

### Raise database engine on local and k8s

docker run --name [CONTAINER_NAME] --network [NETWORK_NAME] -e [NETWORK_VARIABLE] -d mysql: latest

### Access local and k8s database engine (-p -> admin-password)

docker exec -it [ID_CONTENEDOR] mysql -u root -p

### Create local and k8s database

CREATE DATABASE [DATABASE_NAME];

### Verify local and k8s creation

SHOW DATABASES;

### Build the other images and raise the containers

docker build . -t [IMAGE_NAME]

docker run --name [CONTAINER_NAME] --network [NETWORK_NAME] -e [ENVIRONMENT_VARIABLE] -d [IMAGE_NAME]

### Step 3: Create infrastructure with Terraform on AWS

cd /microservices-all-api/terraform

terraform init

terraform plan

terraform apply

This will create the required resources on AWS such as:

- EKS (Elastic Kubernetes Service) cluster

- VPC, subnets, roles, etc.

### Step 4: Configure EKS cluster access

aws eks --region <your-region> update-kubeconfig --name <cluster-name>

### Step 5: Deploy services in Kubernetes

kubectl apply -f /microservices-all-api/deployments/deployments.yaml

kubectl apply -f /microservices-all-api/deployments/services. yaml

### Step 6: Check status

kubectl get nodes

kubectl get pods

kubectl get services

kubectl get ingress

### Step 7: Access the API

Once Ingress is deployed, you can access the authentication and task endpoints from your browser or Postman, using the public URL assigned by AWS (or a custom domain if configured).
