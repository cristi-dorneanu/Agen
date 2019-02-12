#!/bin/sh
cd "$(dirname "$0")"
declare -a arr=('calculation-api-service' 'config' 'eureka-server' 'gateway')

for a in "${arr[@]}"
do
   cd "$a"
   mvn clean install -DskipTests
   cd ..
done

declare -a arr1=('calculation-api-service' 'calculation-core-service' 'config' 'eureka-server' 'gateway')
for a in "${arr1[@]}"
do
   cd "$a"
   docker build -t "cristidorneanu/agen-"$a"" .
   cd ..
done

docker-compose up