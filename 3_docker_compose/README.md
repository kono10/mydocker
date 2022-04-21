# Create an app that uses docker compose to coordinate two docker containers, one for a flask app, and another for a redis database, that you can run locally
* once docker compose is run

## Docker Compose Summary
```
version: '3'
services: 
    redis-server:
        image: 'redis' 
    flask-app:
            build: .
            ports:
                - "8081:5000"
```

* services: define and name the images that you want docker compose to create and run
* build .: create an image based on a docker file in the current directory
* ports: 8081 is the port you visit in the browser, 5000 is the that the app is on

## Commands

`docker-compose up`

force a rebuild of images

`docker-compose up --build`

start in the backgroun

`docker-compose up -d`

stop containers

`docker-compose down`

print status of containers ran by docker-compose, must run the command from the directory the docker-compose file is in
`docker-compose ps`

### Docker Networking
### Stopping Docker Compose Containers
### Container Maitenance
### Automatic Container Restarts
Restart Policies
* no: if crash don't restart
* always: always attempt to restart
* on-faiure: only restart if container stops with an error code 
* unless-stopped: always restart unless developer forces a restart
