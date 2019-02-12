FROM openjdk:10

ADD ./target/calculation-api-service-1.0.0-SNAPSHOT.jar /app/

ADD ./CalculationApiServiceStart.sh /app

RUN apt-get update && \
 apt-get install -y netcat;

RUN chmod 755 /app/CalculationApiServiceStart.sh

EXPOSE 8080