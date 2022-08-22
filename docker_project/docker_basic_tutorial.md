# Docker - Basic Tutorial  
  
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