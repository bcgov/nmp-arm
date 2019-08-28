#!/bin/bash

container_name=arm-legacy-web

#remove docker container and images
docker stop ${container_name}
docker rm ${container_name}
docker rmi ${container_name}