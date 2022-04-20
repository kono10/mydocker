# FROM, RUN, CMD -> instructions
# use existing image as a base,
# image pulled from docker hub
FROM alpine
# alpine is a standard base image

# download and install dependencies
RUN apk add --update redis

# tell image what to do when it starts
CMD ["redis-server"]
