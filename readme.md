# Proyecto de Microservicios: Autenticación y Tareas (Parte DevOps)

## Descripción

Este proyecto consiste en el desarrollo de una arquitectura basada en microservicios utilizando Python. Se compone de dos servicios principales:

- **Servicio de Autenticación**: Gestión de usuarios y autenticación con JWT.
- **Servicio de Tareas (To-Do List)**: Permite a los usuarios crear, listar, actualizar y eliminar tareas.

El objetivo es poner en práctica principios de desarrollo moderno, incluyendo contenerización, orquestación y despliegue automatizado en la nube mediante herramientas DevOps.

## Tecnologías Utilizadas

- Python  
- Docker  
- kubectl  
- AWS  
- Terraform  

---

## Arquitectura del Proyecto

El proyecto está compuesto por **cuatro pods principales** desplegados en un clúster de Kubernetes:

1. **auth-service**: expone endpoints para login, registro y validación de tokens.
2. **task-service**: permite operaciones CRUD sobre tareas asociadas a usuarios autenticados.
3. **nginx**: actúa como Ingress Controller (load balancer) y expone los servicios al exterior.
4. **db**: base de datos que persiste la información de los microservicios.

Todos los servicios están:

- **Conectados en una misma red**, tanto en Docker como en Kubernetes, lo cual permite que se comuniquen internamente de manera segura.
- Configurados con **variables de entorno** que especifican las direcciones de red internas (hostnames y puertos), facilitando la conexión entre microservicios (por ejemplo: el servicio de tareas sabe cómo comunicarse con el de autenticación, y ambos con la base de datos).

---

## Guía de Implementación DevOps

### Requisitos Previos

- Cuenta activa en AWS  
- Docker y kubectl instalados  
- Terraform CLI instalado  
- AWS CLI configurado con credenciales  

### Paso 1: Clonar el repositorio

bash
git clone https://github.com/tu-usuario/nombre-proyecto.git
cd nombre-proyecto

### Paso 2: Construir las imágenes Docker

Normalmente esto se hace dentro de la carpeta donde tienes el Dockerfile.

docker build . -t [NOMBRE_IMAGEN] mysql:latest

# Levantar motor de base de datos en local y k8s

docker run --name [NOMBRE_CONTAINER] --network [NOMBRE_RED] -e [VARIABLE_DE_ENTORNO] -d mysql:latest

# Acceder al motor de base de datos local y k8s (-p -> admin-password)

docker exec -it [ID_CONTENEDOR] mysql -u root -p

# Crear base de datos local y k8s

CREATE DATABASE [nombre_de_base_de_datos];

# Verificar creción local y k8s

SHOW DATABASES;

# Construir las demas imagenes y levantar los containers

docker build . -t [NOMBRE_IMAGEN]

docker run --name [NOMBRE_CONTAINER] --network [NOMBRE_RED] -e [VARIABLE_DE_ENTORNO] -d [NOMBRE_IMAGEN]

### Paso 3: Crear infraestructura con Terraform en AWS

cd /microservicios-todo-api/terraform

terraform init

terraform plan

terraform apply

Esto creará los recursos necesarios en AWS como:

- Cluster de EKS (Elastic Kubernetes Service)

- VPC, subredes, roles, etc.

### Paso 4: Configurar acceso al cluster EKS

aws eks --region <tu-región> update-kubeconfig --name <nombre-cluster>

### Paso 5: Desplegar servicios en Kubernetes

kubectl apply -f /microservicios-todo-api/deployments/deployments.yaml
kubectl apply -f /microservicios-todo-api/deployments/services.yaml

### Paso 6: Verificar el estado

kubectl get nodes
kubectl get pods
kubectl get services
kubectl get ingress

### Paso 7: Acceder a la API

Una vez desplegado el Ingress, puedes acceder a los endpoints de autenticación y tareas desde tu navegador o Postman, usando la URL pública asignada por AWS (o un dominio personalizado si lo configuraste).