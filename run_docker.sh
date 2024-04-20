docker rm --force demo-app-1
docker build -t demo-app-1 .
# docker run -d --name demo-app-1 --network="host" -p 3000:3000 demo-app-1
# docker run -d --name demo-app-1 -p 3000:3000 demo-app-1
docker run -d --name demo-app-1 -p 3000:3000 --net app-network demo-app-1
