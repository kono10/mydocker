## Create a docker image from a simple Dockerfile

* create and run a docker image using a Dockerfile
* tag a docker image

### Command summary
```
docker build .
docker build -t <dockerid>/<name>:<version> .
docker run <id>
docker run <tag>

```
* version may be "latest" for the most recent version
* -t add a tag to the image, can use that tag id to docker run <tag id>

## Create docker image
#### When 'Dockerfile' is ready cd into the directory where the file is ...
```
> docker build .
Sending build context to Docker daemon  14.85kB
Step 1/3 : FROM alpine
latest: Pulling from library/alpine
df9b9388f04a: Pull complete 
Digest: sha256:4edbd2beb5f78b1014028f4fbb99f3237d9561100b6881aabbf5acce2c4f9454
Status: Downloaded newer image for alpine:latest
 ---> 0ac33e5f5afa
Step 2/3 : RUN apk add --update redis
 ---> Running in ddc4746153d1
fetch https://dl-cdn.alpinelinux.org/alpine/v3.15/main/x86_64/APKINDEX.tar.gz
fetch https://dl-cdn.alpinelinux.org/alpine/v3.15/community/x86_64/APKINDEX.tar.gz
(1/1) Installing redis (6.2.6-r0)
Executing redis-6.2.6-r0.pre-install
Executing redis-6.2.6-r0.post-install
Executing busybox-1.34.1-r5.trigger
OK: 8 MiB in 15 packages
Removing intermediate container ddc4746153d1
 ---> 94990ccf6d85
Step 3/3 : CMD ["redis-server"]
 ---> Running in a0fd55a5ebb4
Removing intermediate container a0fd55a5ebb4
 ---> f469169f9570
Successfully built f469169f9570

> docker run f469169f9570

1:C 20 Apr 2022 19:44:26.731 # oO0OoO0OoO0Oo Redis is starting oO0OoO0OoO0Oo
1:C 20 Apr 2022 19:44:26.731 # Redis version=6.2.6, bits=64, commit=b39e1241, modified=0, pid=1, just started
1:C 20 Apr 2022 19:44:26.731 # Warning: no config file specified, using the default config. In order to specify a config file use redis-server /path/to/redis.conf
1:M 20 Apr 2022 19:44:26.733 * monotonic clock: POSIX clock_gettime
1:M 20 Apr 2022 19:44:26.735 * Running mode=standalone, port=6379.
1:M 20 Apr 2022 19:44:26.735 # WARNING: The TCP backlog setting of 511 cannot be enforced because /proc/sys/net/core/somaxconn is set to the lower value of 128.
1:M 20 Apr 2022 19:44:26.735 # Server initialized
1:M 20 Apr 2022 19:44:26.735 # WARNING overcommit_memory is set to 0! Background save may fail under low memory condition. To fix this issue add 'vm.overcommit_memory = 1' to /etc/sysctl.conf and then reboot or run the command 'sysctl vm.overcommit_memory=1' for this to take effect.
1:M 20 Apr 2022 19:44:26.735 * Ready to accept connections
^C1:signal-handler (1650483960) Received SIGINT scheduling shutdown...
1:M 20 Apr 2022 19:46:00.952 # User requested shutdown...
1:M 20 Apr 2022 19:46:00.953 * Saving the final RDB snapshot before exiting.
1:M 20 Apr 2022 19:46:00.959 * DB saved on disk
1:M 20 Apr 2022 19:46:00.959 # Redis is now ready to exit, bye bye...

````

## Tag an image
```
➞  sudo docker build -t jkonovsky/redisfun:latest .                                                                                                                                                                                                                                          
[sudo] password for jkonovsky: 
Sending build context to Docker daemon  31.74kB
Step 1/3 : FROM alpine
 ---> 0ac33e5f5afa
Step 2/3 : RUN apk add --update redis
 ---> Using cache
 ---> 94990ccf6d85
Step 3/3 : CMD ["redis-server"]
 ---> Using cache
 ---> f469169f9570
Successfully built f469169f9570
Successfully tagged jkonovsky/redisfun:latest


➞  sudo docker run jkonovsky/redisfun:latest                                                                                                                                                                                                                                                 
1:C 20 Apr 2022 20:18:33.695 # oO0OoO0OoO0Oo Redis is starting oO0OoO0OoO0Oo
1:C 20 Apr 2022 20:18:33.695 # Redis version=6.2.6, bits=64, commit=b39e1241, modified=0, pid=1, just started
1:C 20 Apr 2022 20:18:33.695 # Warning: no config file specified, using the default config. In order to specify a config file use redis-server /path/to/redis.conf
1:M 20 Apr 2022 20:18:33.697 * monotonic clock: POSIX clock_gettime
1:M 20 Apr 2022 20:18:33.699 * Running mode=standalone, port=6379.
1:M 20 Apr 2022 20:18:33.699 # WARNING: The TCP backlog setting of 511 cannot be enforced because /proc/sys/net/core/somaxconn is set to the lower value of 128.
1:M 20 Apr 2022 20:18:33.699 # Server initialized
1:M 20 Apr 2022 20:18:33.699 # WARNING overcommit_memory is set to 0! Background save may fail under low memory condition. To fix this issue add 'vm.overcommit_memory = 1' to /etc/sysctl.conf and then reboot or run the command 'sysctl vm.overcommit_memory=1' for this to take effect.
1:M 20 Apr 2022 20:18:33.700 * Ready to accept connections
^C1:signal-handler (1650485915) Received SIGINT scheduling shutdown...
1:M 20 Apr 2022 20:18:36.008 # User requested shutdown...
1:M 20 Apr 2022 20:18:36.008 * Saving the final RDB snapshot before exiting.
1:M 20 Apr 2022 20:18:36.014 * DB saved on disk
1:M 20 Apr 2022 20:18:36.014 # Redis is now ready to exit, bye bye...
```

## Build Process detail

#### > docker build .
* pass the file off to docker cli
* build -> creates the actual image from the file
* . -> build context

#### Rebuilds with cache
if you were to add the following line to Dockerfile 
```
RUN apk add --update gcc
```
and tried to `docker build .` for the second time, docker will utilize its cache to generate the the image for the commands that were in Dockerfile the first time and will only actually download data for the newly added line


## Things you could do with the image ...

Set a value in the redis db
```
> sudo docker exec -it cafe297b89f sh                                                                                                                                                                                                                                                                                       
/ # redis-cli
127.0.0.1:6379> set myval 5
OK
127.0.0.1:6379> get myval
"5"
127.0.0.1:6379> 
/ # 

```



