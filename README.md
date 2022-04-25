# General Summary
* alpine is code for "the smallest version of the image possible", i.e. node:alpine

## Commands
```docker run hello-world```

run docker in the background

`docker run -d  hello-world`

-d stands for detached state

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

`docker exec -it <id> <command>`

`docker run -it <id|tag> sh`
