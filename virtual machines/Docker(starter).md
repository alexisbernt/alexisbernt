# Docker 
Docker is a virtual machine. It can help you run a database locally. You can create APIs with Docker. 

Use Docker Hub. 

### Class Tutorial
___________________________________________________________________
Use a docker-compose.yml file to determine 
You pick an image. (Ex: mysql:latest)
Determine the ports in which you want to select mysql

If you don't want your data to be lost:
Save it to 
volumes:
- db_persdata:/var/lib/mysql
volumes:

Docker --> able to determine the port 
