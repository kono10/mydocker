# General Summary
* alpine is code for "the smallest version of the image possible", i.e. node:alpine
* image is an instance of a container

# Commands

## Docker Cli
```docker run hello-world```

run docker in the background

`docker run -d  --rm hello-world`

-d stands for detached state
--rm will remove the container once it is done running

busy box has more functionality than hello-world

```docker run busybox ls```

```docker run busybox echo hello```


docker run == docker create + docker start

`docker create busybox`

`docker start <id>`

list running containers

`docker ps`

list all containers

`docker ps --all`

restart a container 

```
docker ps --all
docker start <container id>
```
container id is the first column of the data from docker ps

remove all containers 

`docker system prune`

`docker logs <id>`

`docker stop <id>`

`docker kill <id>`

execute commands inside a container

`docker run -it <id|tag> sh`

execute commands inside a already running image

```
docker exec -it <id> <command>
❯ docker ps
CONTAINER ID   IMAGE                                  COMMAND                  CREATED         STATUS         PORTS                    NAMES
117ede224c0d   djangoelasticbeanstalktemplate_nginx   "/docker-entrypoint.…"   3 minutes ago   Up 3 minutes   0.0.0.0:80->80/tcp     djangoelasticbeanstalktemplate_nginx_1
cd2dc9b2f967   djangoelasticbeanstalktemplate_web     "gunicorn --bind ' 0…"   3 minutes ago   Up 3 minutes   0.0.0.0:8001->8000/tcp   djangoelasticbeanstalktemplate_web_1

❯ docker exec -it djangoelasticbeanstalktemplate_nginx_1 sh
# cd static
# pwd
/static
# ls
admin  background.jpeg	favicon.jpeg  style.css

```


push image to docker hub
```
docker login
docker tag <id> <dockerhub_username>/<image_name>:<version>
docker push <dockerhub_username>/<image_name>

```

kill all running docker containeres

`docker kill $(docker ps -q)`

### Dockerfile Commands
```
docker build .
docker build -t <dockerid>/<name>:<version> .
docker run <id>
docker run <tag>
```
run an image and map a port

`docker run -p 8000:5000 <tag>`

