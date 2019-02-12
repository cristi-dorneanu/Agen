FROM openjdk:10

ADD ./target/config-1.0.0-SNAPSHOT.jar /app/

CMD ["java", "-Xmx200m", "-jar", "/app/config-1.0.0-SNAPSHOT.jar"]

HEALTHCHECK --interval=30s --timeout=30s CMD curl -f http://config:8888/actuator/health || exit 1

EXPOSE 8888