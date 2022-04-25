# Setup a Development Workflow With Travis CI and Docker
* don't have to user docker for this workflow (but will make our lives easier)
* the prod set up follows this tutorial https://www.digitalocean.com/community/tutorials/how-to-build-and-deploy-a-flask-application-using-docker-on-ubuntu-20-04 

## Commands
`Docker build -f Dockerfile.dev -t <username/tagname:version> .`

`docker run -p 8080:5000 <username/tagname:version>`

`docker build Docker.dev .`

### Docker Volumes
* sets up references to files / directories instead of copying them into the container
* volumes will override any files or directories that are `COPY . .` in Dockerfile

`docker run -p 8080:5000 -v $(pwd):/flask_app jake`

### Volume Bookmark
* tells docker to not override directories currently in the container
* if you have a directory app/stuff/stuff.txt but Dockerfile runs a command inside the container 
that installs things in app/stuff/ you may want to put a bookmark on app/stuff so your volume does not override that directory

`docker run -p 8080:5000 -v flask_app/app.py -v $(pwd):/flask_app jake`

### Shorthand with Docker Compose
* can replace the long command above witha docker compose file that just runs a single container

### Do we need COPY in dockerfile
* not really, but could leave it in there just as a reference for what is going on in the future

### Running Tests
`docker run jake pytest tests.py` 

Create another service in docker-compose specifically to run tests
```
    tests:
      build:
        context: .
        dockerfile: Dockerfile.dev
      volumes:
        - .:/flask_app
      command: ["pytest", "tests.py"]
```
* the above just overrides the default command and runs the tests when the services is started


### Multistep Build
* for node `npm build` creates 100s of files but only need two, so create a docker proceess
with a build phase and a run phase, build generates all the files and then run phase takes only the files that we need

```
FROM node:16-alpine as builder
WORKDIR '/app'
COPY package.json .
RUN npm install
COPY . .
RUN npm run build

FROM nginx
# refereces as builder
# app build has all the stuff we care about
COPY --from=builder /app/build /usr/share/nginx/html
```
`docker build .`

`docker run -p 8080:80` <containerId>
