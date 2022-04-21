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
COPY . . won't include requirements.txt in the below example
```
COPY requirements.txt ./requirements.txt
COPY . .
```

### Examples

Inspect the properties of a docker hub container, in this case I checked to see that the container had pip installed
```
jkonovsky@rcwld-jkonovsk1:~/mydocker/2_simple_project/flask$ sudo docker run -it python:3.9 sh
Unable to find image 'python:3.9' locally
3.9: Pulling from library/python
6aefca2dc61d: Pull complete 
967757d56527: Pull complete 
c357e2c68cb3: Pull complete 
c766e27afb21: Pull complete 
32a180f5cf85: Pull complete 
1535e3c1181a: Pull complete 
6de7cb7bdc8f: Pull complete 
26787c68cf0c: Pull complete 
9952b1051ada: Pull complete 
Digest: sha256:087b8a1635ec8e47e4e90557fa41bf6a1c482f939eb5784ecc028ad140341870
Status: Downloaded newer image for python:3.9
# python
Python 3.9.12 (main, Apr 20 2022, 18:40:34) 
[GCC 10.2.1 20210110] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> 
KeyboardInterrupt
>>> 
# pip install django
Collecting django
  Downloading Django-4.0.4-py3-none-any.whl (8.0 MB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 8.0/8.0 MB 10.6 MB/s eta 0:00:00
Collecting asgiref<4,>=3.4.1
  Downloading asgiref-3.5.0-py3-none-any.whl (22 kB)
Collecting sqlparse>=0.2.2
  Downloading sqlparse-0.4.2-py3-none-any.whl (42 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 42.3/42.3 KB 7.7 MB/s eta 0:00:00
Installing collected packages: sqlparse, asgiref, django
Successfully installed asgiref-3.5.0 django-4.0.4 sqlparse-0.4.2
WARNING: Running pip as the 'root' user can result in broken permissions and conflicting behaviour with the system package manager. It is recommended to use a virtual environment instead: https://pip.pypa.io/warnings/venv

```
