FROM openjdk:10

ADD ./target/eureka-server-1.0.0-SNAPSHOT.jar /app/

CMD ["java", "-Xmx200m", "-jar", "/app/eureka-server-1.0.0-SNAPSHOT.jar"]

EXPOSE 9091