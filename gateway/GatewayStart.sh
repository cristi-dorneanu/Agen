#!/bin/sh
while ! nc -z eureka-server 9091 ; do
    echo "Waiting for the Eureka Server"
    sleep 3
done

while ! nc -z config 8888 ; do
    echo "Waiting for the Config Server"
    sleep 3
done


java -jar /app/gateway-0.0.1-SNAPSHOT.jar