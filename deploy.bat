set list ='calculation-api-service' 'calculation-core-service' 'config' 'eureka-server' 'gateway'

for %a in (%list) do (
   cd %a
   mvn clean install -DskipTests
   docker build -t cristidorneanu/agen-%%a
   cd ..
)