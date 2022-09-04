# Docker - Basic Tutorial  
![Docker](https://github.com/sansinghsanjay/Misc_python_scripts/blob/master/docker_project/images/docker_image.png)  
Docker is an open platform for developing, shipping, and running applications. Docker enables you to separate your applications from your infrastructure so you can deliver software quickly. With Docker, you can manage your infrastructure in the same ways you manage your applications.  
Docker provides the ability to package and run an application in a loosely isolated environment called a container. The isolation and security allows you to run many containers simultaneously on a given host. Containers are light-weight and contain everything needed to run the application, so you do not need to rely on what is currently installed on the host. You can easily share containers while you work, and be sure that everyone you share with gets the same container that works in the same way.  
Advantages of Docker:  
1. Fast, consistent delivery of your applications  
2. Responsive deployment and scaling  
3. Running more workloads on the same hardware  
  
## Docker Architecture  
![Docker Architecture](https://github.com/sansinghsanjay/Misc_python_scripts/blob/master/docker_project/images/Docker-Architecture.png)  
Docker uses a client-server architecture. The docker client talks to the docker daemon which does the heavy lifting of building, running, and distributing your docker containers. The docker client and daemon can run on the same system or you can connect a docker client to a remote docker daemon. The docker client and daemon communicate using a REST API, over UNIX sockets or a network interface. Another docker client is "Docker Compose" that lets you work with applications consisting of a set of containers.  
### The Docker Daemon  
The docker daemon (`dockerd`) listens for Docker API requests and manages Docker objects such as images, containers, networks, and volumes. A daemon can also communicate with other daemons to manage docker services.  
### The Docker Client  
The docker client (`docker`) is the primary way that many Docker users interact with Docker. When you use commands such as `docker run`, the client sends these commands to `dockerd` which carries them out. The docker command uses the docker API. The docker client can communicate with more than one daemon.  
### Docker Desktop  
Docker desktop is an easy to install application that enables you to build and share continerized applications and microservices. Docker desktop includes docker daemon, docker client, docker compose, docker content trust, kubernetes, and credential helper.  
### Docker Registeries  
A docker registry stores docker images. Docker Hub is a public registry that anyone can use. You can run your own private registry. When you use the `docker pull` or `docker run` commands, the required images are pulled from your configured registry. When you use the `docker push` command, your image is pushed to your configured registry.  
### Docker Objects  
When you use docker, you are creating and using images, containers, networks, volumes, plugins, and other objects:  
1. Images: An image is a read-only template with instructions for creating a docker container. Often, an image is based on another image with some additional customization.  
2. Container: A container is a runnable instance of image. You can create, start, stop, move, or delete a container using the Docker API or CLI (Command Line Interface). You can connect a container to one or more networks, attach storage to it, or even create a new image based on its current state. By default, a container is well isolated from other containers and its host machine. You can control how isolated a container's network, storage, or other underlying subsystems are from other containers or from the host machine.  
  
## Create Docker  
Following are the steps:  
1. First create your docker project folder. Put all your project files and sub-folders inside it.  
2. Create a file "Dockerfile" inside the project folder.  
3. Write your code inside the Dockerfile. This includes instruction for:  
i. Using the base OS file  
ii. Copying (or adding) the files and sub-directories of your project  
iii. Installing required packages (or libraries)  
iv. Exposing port (if required)  
v. Command to run the project  
4. Open terminal  
5. Navigate to your project folder in the terminal  
6. Run the following command to create the Docker image:  
`$ docker build -t <user_name>/<docker_image_name> .`  
7. Run the following command to check if the image is create or not:  
`$ docker images`  
8. Run the following command to run the Docker image (after this command, an instance of the Docker image will form, called as "Container"):  
`$ docker run <user_name>/<docker_image_name>`  
9. If the container is running for a long time, then you can check the details of running container by running the following command:  
`$ docker ps`  
10. Run the following command to save the image into a .tar file:  
`$ docker save <user_name>/<docker_image_name> -o <image_name>.tar`  
	`<image_name` could be different than `<docker_image_name>`  
11. Now, you can share the saved docker image `<image_name>.tar` with others. After sharing, run the following command to load this docker image (for testing, simply delete the image and load the image from the saved .tar file):  
Command to delete the docker image:  
`$ docker rmi -f <IMAGE ID>`  
`<IMAGE ID>` can be obtained by running `$ docker images` command  
Command to load the docker image:  
`$ docker load --input <image_name>.tar`  
12. Now, you can run the docker image by the command provided in step 8 (above)  
  
## Docker - Entrypoint  
In Dockerfiles, and ENTRYPOINT instruction is used to set executables that will always run when the container is initiated. Unlike CMD commands, ENTRYPOINT commands cannot be ignored or overriden, even when the container runs with command line arguments stated.  