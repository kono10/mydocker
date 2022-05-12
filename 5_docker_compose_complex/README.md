# A More Complcated multi container app with 3+ containers

## Setup
* Client will serve info to the user and make request to the server

### Server
* make calculations and store data, serves as an api for database and redis

### Client
* handle basic interaction and make requests to the server

### Redis
* keep a running count of the number of visits

### Postgres
* keep track of the date and time those visits occurred
