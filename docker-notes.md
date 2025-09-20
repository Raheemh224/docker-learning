### What are containers? 
- These are portable lightweight units for running applications. Runs the same in every environment 

## Benefits: 

- Isolation – Prevents conflicts and runs smoothly without interfering. They don’t clash  
- Resource efficient as they share the host kernel. Makes it faster to start up  

## Main Components  

- Docker Engine – A portable, lightweight application runtime and packaging tool. It is a core service which manages containers  
- Docker Hub – A cloud service for sharing applications and automating workflows 

## Images and Containers 
- Images are templates for creating containers  
- Containers are running instances of images  
- A docker file is a file used to create images 

## Importance in modern infrastructure 
- Simplified Deployment  
- Improved Efficiency – lightweight as the docker containers share the host kernal 
- Enhanced Collaboration – Easy to share environments and images 

## Key Differences between VMs and Containers 

 

## Why is it important to know the differences?  
- This helps you choose the right technology for your needs.  

## Docker Images 

## What is a docker file? 
- Series of instructions on how to build a docker image 
- Each instruction in the docker file creates a layer of the image  
- It allows for repeatable builds using the same docker file  

 

## 5 key docker commands  
- FROM – specifies the base images to use for the docker image which serves as a foundation. ‘FROM node:14’ 
- RUN – Executes commands in the container, used to install packages  
- COPY – copies files from the host machine into the container  
- WORKDIR – sets the working directory for subsequent instructions  
- CMD – specifies the command to run when the container runs. 

## How to containerise a web application? 
- Create a dockerfile 
- Run docker build -t hello-flask . To build an image  

## To containerise the image see below:
- To containerise an image run the command
- Docker run –d –p 5000:5000 hello-flask 
- Docker ps – to see current containers  
- Docker stop - to stop a container from running 

 

 

## Introduction into Docker Networking 

- Bridge Network – A bridge network is the default network mode for containers on the same machine. Containers on the bridge network can communicate with each other using their own IP address. It’s isolated from the host network providing an extra layer of security 
- Host Network – In this mode the container uses the host machines network directly without any isolation. Useful for when containers need to closely interact with the host system. 
- None Network – This type gives the container no network interface at all, which makes it completely isolated 

## Why is docker networking important in DevOps? 

- It simplifies the implementation of microservices architecture. Microservices allow different paths of application to run as a single container. Docker networking ensures that these services can communicate with each other efficiently.  

 

## How to link a flask application to a mysql database container/Link containers together  

 

# To create a network, run the command: 

- Docker network create ‘my-custom-network' 
- docker run -d --name myapp --network my-custom-network -p 5000:5000 hello-flask-mysql 

 

## Introduction to Docker Compose 

- Docker Compose helps you run multiple Docker containers together. The main features are:  

- Docker-compose .yml file – lists all the services your container needs.  

## Why is it so important in DevOps? 

- Makes development and testing easier  
- Ensures consistency across different environments 
- Enhances teamwork 

## Docker-compose.yml file 

- Think of this as a recipe of ingredients or services which the container needs 

- version: '3.8' - this is the version of file  
 
- services: - list all the different parts of the app 
  web: 
    build: . - tells docker compose to build the webservice from the dockerfile in the current directory 
    ports: 
      - "5000:5000" 
    depends_on: - this means that the webservice depends on the database service  
      - db 
 
  db: 
    image: mysql:8 
    environment: 
      MYSQL_ROOT_PASSWORD: my-secret-pw 

 

## How do you now start both the flask app and mysql database? 

- Run the command docker-compose up – this tells docker compose to read the yml file, build any images 
- docker-compose up –d makes sure it runs in the background 
- docker-compose up --build –d 

 

## Docker Registries 

This is crucial for storing and distributing docker images. Key features: 

- Public registries – DockerHub 
- Private Registries – AWS ECR  

 

## Why is it important in DevOps? 

- Streamline deployment  
- Enhances collaboration 
- Ensures consistency across different environments  

 

Dockerhub is a public registry where you can store and share docker images. It is widely used due to: 

- Accessibility  
- Trusted resources  

 

Important commands for docker images 

1. docker build -t raheemh224/flask-mysql:v1 . - this is used to create an image which is ready to push 

2. docker push raheemh224/flask-mysql:v1 – this pushes the image into Docker hub  

3. docker pull raheemh224/flask-mysql:v1 to pull it to the machine  

4. docker images – will give you a list of all the images you have locally  

5. docker inspect ‘image ID’ - will give more info about an image  

6. docker rmi ‘image ID’ - will remove an image  

7. docker system prune – will all unused images and containers  

8. docker ps – to see what containers are running  

9. docker rm – removes the container  


- Multistage builds makes images more lighter using less resources. Multistage builds allows you to use multiple FROM statements. 1 stage will build the application and 2nd much lighter stage will create the final image to deploy. This approach discards unnecessary dependencies, making it load up more quicker 

  

## Why use orchestration tools?  

- As apps grow, managing containers manually become harder. These tools are made to: 

- manage large-scale deployments.  
- Ensure high availability 
- Automate scaling and recovery  
- Simple  
- Enhance reliability  
- Resource utilization 

 

## Extra Tips

- Docker exec –it “container ID” /bin/bash - this is used to go inside the terminal of the container. Useful for debugging. 

Don’t get confused with Docker Start and Docker Run. 
- Docker Run – create a new container from an image  
- Docker start – you are running with containers with different options. -d –p 

- Docker compose –f “flask.yml” up 
- FROM python – Install Python  
- RUN mkdir –p /home/app - RUN : execute any Linux command – it creates a /home/app folder it lives/created inside the container  
- COPY . /home/app - this executes on the host machine copying current folder files to /home/app  
- CMD [“node”, “server.js”] - this means to start app with “node server.js”
- CMD is the entrypoint command , can have multiple RUN commands  

 