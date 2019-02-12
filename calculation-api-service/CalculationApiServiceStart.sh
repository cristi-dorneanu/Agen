#!/bin/sh
while ! nc -z eureka-server 9091;
        do
          echo sleeping;
          sleep 1;
 done;

while ! nc -z config 8888;
        do
          echo sleeping;
          sleep 1;
 done;

 while ! nc -z rabbitmq 15672;
        do
          echo sleeping;
          sleep 1;
 done;


java -jar "/app/calculation-api-service-1.0.0-SNAPSHOT.jar"