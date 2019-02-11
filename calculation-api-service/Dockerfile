FROM openjdk:10

ADD ./target/calculation-api-service-1.0.0-SNAPSHOT.jar /app/

CMD ["java", "-Xmx200m", "-jar", "/app/calculation-api-service-1.0.0-SNAPSHOT.jar"]

EXPOSE 8888