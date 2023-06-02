
# Multi Route Container to test `FastAPI`

`docker compose up`

## push the image to be used by `k8s`

https://hub.docker.com/repository/docker/miriha/multi-route/

`docker compose push`

## Different Routes

http://localhost:8090/
http://localhost:8090/integer/foo
http://localhost:8090/integer/3
http://localhost:8090/integer/4.2

http://localhost:8090/docs
http://localhost:8090/redoc

http://localhost:8090/models/user
http://localhost:8090/models/bonus
http://localhost:8090/models/group

http://localhost:8090/file/path/assets/file.txt -> show path
http://localhost:8090/file/assets/file.txt -> show file content

http://localhost:8090/home/
