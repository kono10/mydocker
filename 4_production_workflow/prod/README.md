## How to build and run app locally

```
❯ docker-compose build
Building myapp
[+] Building 4.0s (10/10) FINISHED                                                                            
 => [internal] load build definition from Dockerfile                                                     0.0s
 => => transferring dockerfile: 37B                                                                      0.0s
 => [internal] load .dockerignore                                                                        0.0s
 => => transferring context: 2B                                                                          0.0s
 => [internal] load metadata for docker.io/library/python:3.8                                            0.7s
 => [internal] load build context                                                                        0.0s
 => => transferring context: 25.47kB                                                                     0.0s
 => [1/5] FROM docker.io/library/python:3.8@sha256:f732d55571549b427e12edb89d0951372e7b73c67f717ad0645b  0.0s
 => CACHED [2/5] RUN apt-get update                                                                      0.0s
 => CACHED [3/5] WORKDIR /app                                                                            0.0s
 => [4/5] COPY . .                                                                                       0.0s
 => [5/5] RUN pip3 install -r requirements.txt                                                           3.0s
 => exporting to image                                                                                   0.2s
 => => exporting layers                                                                                  0.1s
 => => writing image sha256:034b95fc0afd43a7a7c373feeebd8ca2128de1387d3865ddc299be2ec1204e50             0.0s 
 => => naming to docker.io/library/prod_myapp                                                            0.0s 
                                                                                                              
Use 'docker scan' to run Snyk tests against images to find vulnerabilities and learn how to fix them          
Successfully built 034b95fc0afd43a7a7c373feeebd8ca2128de1387d3865ddc299be2ec1204e50
Building nginx
[+] Building 0.7s (8/8) FINISHED                                                                              
 => [internal] load build definition from Dockerfile                                                     0.0s
 => => transferring dockerfile: 36B                                                                      0.0s
 => [internal] load .dockerignore                                                                        0.0s
 => => transferring context: 2B                                                                          0.0s
 => [internal] load metadata for docker.io/library/nginx:1.15.2                                          0.6s
 => [1/3] FROM docker.io/library/nginx:1.15.2@sha256:d85914d547a6c92faa39ce7058bd7529baacab7e0cd4255442  0.0s
 => [internal] load build context                                                                        0.0s
 => => transferring context: 32B                                                                         0.0s
 => CACHED [2/3] RUN rm /etc/nginx/nginx.conf                                                            0.0s
 => CACHED [3/3] COPY nginx.conf /etc/nginx/                                                             0.0s
 => exporting to image                                                                                   0.0s
 => => exporting layers                                                                                  0.0s
 => => writing image sha256:a71315721021acd8ea2214f208bf3ca3b16b87a7ecd86832646e5f2cc013c020             0.0s
 => => naming to docker.io/library/prod_nginx                                                            0.0s

Use 'docker scan' to run Snyk tests against images to find vulnerabilities and learn how to fix them
Successfully built a71315721021acd8ea2214f208bf3ca3b16b87a7ecd86832646e5f2cc013c020
Use 'docker scan' to run Snyk tests against images to find vulnerabilities and learn how to fix them
❯ docker-compose up
Docker Compose is now in the Docker CLI, try `docker compose up`

WARNING: Found orphan containers (prod_web_1, flask_api) for this project. If you removed or renamed this serv
ice in your compose file, you can run this command with the --remove-orphans flag to clean it up.
Recreating flask_app ... done
Starting nginx       ... done
Attaching to nginx, flask_app
flask_app | [2022-04-28 01:03:49 +0000] [1] [INFO] Starting gunicorn 20.1.0
flask_app | [2022-04-28 01:03:49 +0000] [1] [INFO] Listening at: http://0.0.0.0:5000 (1)
flask_app | [2022-04-28 01:03:49 +0000] [1] [INFO] Using worker: sync
flask_app | [2022-04-28 01:03:49 +0000] [9] [INFO] Booting worker with pid: 9
flask_app | [2022-04-28 01:03:49 +0000] [10] [INFO] Booting worker with pid: 10
flask_app | [2022-04-28 01:03:49 +0000] [11] [INFO] Booting worker with pid: 11
/
```
