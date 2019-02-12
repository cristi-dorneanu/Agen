FROM openjdk:10

ADD ./target/eureka-server-1.0.0-SNAPSHOT.jar /app/

CMD ["java", "-Xmx200m", "-jar", "/app/eureka-server-1.0.0-SNAPSHOT.jar"]

HEALTHCHECK --interval=30s --timeout=30s CMD curl -f http://localhost:9091/actuator/health || exit 1

EXPOSE 9091