FROM maven:3.6-ibmjava-alpine as my_build_stage
COPY . .
RUN mvn verify

FROM openjdk:8u242-jre-slim as my_run_stage
COPY --from=my_build_stage /target atifacts
ENTRYPOINT java -jar atifacts/hello-java.jar
