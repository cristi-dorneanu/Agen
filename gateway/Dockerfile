FROM openjdk:10

ADD ./target/gateway-0.0.1-SNAPSHOT.jar /app/

ADD ./GatewayStart.sh /app

RUN apt-get update && \
 apt-get install -y netcat;

RUN chmod 755 /app/GatewayStart.sh

EXPOSE 9092