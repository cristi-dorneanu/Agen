#!/bin/sh
while ! nc -z rabbitmq 15672;
        do
          echo sleeping;
          sleep 1;
 done;
 
python /app/Runner.py