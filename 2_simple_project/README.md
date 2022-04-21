# Create a container for a python applications

# 
### WORKDIR


# Create a docker container for flask

while in the flask directory

`docker build -t jkonovsky/simpleflask .`

`docker run jkonovsky/simpleflask`

port is still not configured so you won't be able to access the app from your browser

`docker run -p 8000:5000 jkonovsky/simpleflask`

* 8000:5000 -> map port 8000 from the local host to port 5000 in the running container


### Specifying a working directory
* it is nice to have a working directory where all application files live to keep 
them separate from system files
* also don't want to overwrite any existing files in the root project directory


### Minimizing Rebuilds
* put files that will change often toward the end of the docker file
* if a single file changes, docker will rebuild every resource after that file
in Dockerfile
* also important to point out that if any changes made in app.py will not be reflected in the
built container, must rebuild the container for it to include any app.py updates (this problem can 
be solved with volumes)


### General 
COPY . . won't include requirements.txt
```
COPY requirements.txt ./requirements.txt
COPY . .
```
