# Base Spring Boot Microservice Template
## EdgeCloud Monitor Backend Standard
### Purpose
This document defines the standard Spring Boot microservice template for the EdgeCloud Monitor platform.
The purpose of this template is to ensure that every backend service follows a consistent structure, dependency setup, configuration approach, naming convention, and build process.
---
# Standard Package Structure
Each backend microservice should follow this package structure:
```text
com.edgecloud.<service>
├── controller
├── service
├── service.impl
├── repository
├── entity
├── dto
├── config
├── exception
└── <ServiceName>Application.java

Package Responsibilities

Package	Responsibility
controller	REST API endpoints
service	Service interfaces and business contracts
service.impl	Business logic implementations
repository	Spring Data JPA repositories
entity	JPA database entities
dto	Request and response objects
config	Service configuration classes
exception	Custom exceptions and global error handling

⸻

Common Maven Dependency Standard

Each backend service must include only the dependencies required for its role. However, most EdgeCloud Monitor backend services share a common technical baseline.

Standard Dependencies

Dependency	Purpose
Spring Web	REST API development
Spring Data JPA	Database access using repositories and entities
Spring Validation	Request validation and input constraints
Spring Boot Actuator	Health and monitoring endpoints
MySQL Driver	MySQL database connectivity
Eureka Client	Service discovery registration
Spring Boot Test	Unit and integration testing

Dependency Rules

* Each microservice must remain independently buildable.
* Dependencies must be added only when required by the service role.
* Database-owning services should include Spring Data JPA and MySQL Driver.
* Services registered with Eureka should include Eureka Client.
* All backend services should include Actuator for health visibility.
* Test dependencies should remain scoped to test execution.

⸻

Application Configuration Standard

All backend services must support externalised configuration through application.yml or application.yaml files and environment variables.

Required Configuration Areas

Service Identity

spring:
  application:
    name: edgecloud-service-name

Server Configuration

server:
  port: ${SERVER_PORT:8080}

Eureka Registration

eureka:
  client:
    service-url:
      defaultZone: ${EUREKA_SERVER_URL:http://localhost:8761/eureka/}

Database Configuration

spring:
  datasource:
    url: ${SPRING_DATASOURCE_URL:jdbc:mysql://localhost:3306/service_db}
    username: ${SPRING_DATASOURCE_USERNAME:service_user}
    password: ${SPRING_DATASOURCE_PASSWORD:service_pass}
    driver-class-name: com.mysql.cj.jdbc.Driver

JPA Configuration

spring:
  jpa:
    hibernate:
      ddl-auto: ${SPRING_JPA_HIBERNATE_DDL_AUTO:update}
    show-sql: ${SPRING_JPA_SHOW_SQL:true}
    properties:
      hibernate:
        dialect: org.hibernate.dialect.MySQLDialect

Actuator Configuration

management:
  endpoints:
    web:
      exposure:
        include: health,info
  endpoint:
    health:
      show-details: always

Configuration Principles

* Configuration must not be hardcoded inside application code.
* Environment variables should be used for deployment-specific values.
* Services must support Docker Compose execution.
* Services must support local development execution.
* Service names must remain unique across Eureka.
* Sensitive values such as passwords and secrets must not be committed as production credentials.

⸻

Health and Monitoring Standard

All backend services must expose Spring Boot Actuator endpoints.

Required Endpoints

/actuator/health
/actuator/info

Purpose

These endpoints support:

* Service health validation
* Docker deployment validation
* Eureka troubleshooting
* Monitoring integration
* Future dashboard integration

Validation

The following endpoint should return UP:

http://localhost:<port>/actuator/health

Example expected response:

{
  "status": "UP"
}

⸻

Service Naming Standard

Each service must use a clear and consistent Spring application name.

Naming Format

edgecloud-<domain>-service

Current Service Names

Service	Spring Application Name
API Gateway	edgecloud-api-gateway
Discovery Service	edgecloud-discovery-service
Auth Service	edgecloud-auth-service
Monitoring Service	edgecloud-monitoring-service
Device Service	edgecloud-device-service
Alert Service	edgecloud-alert-service

Naming Rules

* Service names must be lowercase.
* Service names must be unique.
* Service names must clearly describe the service responsibility.
* Eureka service registration must use the configured Spring application name.

⸻

Error Handling Standard

Each backend service should use a consistent exception-handling structure.

Recommended Classes

exception
├── GlobalExceptionHandler.java
├── ResourceNotFoundException.java
├── BadRequestException.java
└── ErrorResponse.java

Error Response Format

{
  "timestamp": "2026-05-29T12:00:00",
  "status": 404,
  "error": "Not Found",
  "message": "Requested resource was not found",
  "path": "/api/v1/example"
}

Error Handling Principles

* Controllers should not contain repeated try/catch logic.
* Business validation should be handled in the service layer.
* Common API errors should return consistent JSON responses.
* Error messages should be clear enough for debugging without exposing sensitive information.
* Future services should use @ControllerAdvice for global exception handling.

⸻

Baseline Dockerfile Standard

Each Spring Boot microservice should include a Dockerfile for container builds.

Standard Dockerfile

FROM eclipse-temurin:21-jdk AS build
WORKDIR /app
COPY . .
RUN ./mvnw clean package -DskipTests
FROM eclipse-temurin:21-jre
WORKDIR /app
COPY --from=build /app/target/*.jar app.jar
EXPOSE 8080
ENTRYPOINT ["java", "-jar", "app.jar"]

Dockerfile Rules

* Use Java 21 images.
* Build the application inside the container.
* Run from a lightweight Java runtime image.
* Expose the correct service port.
* Do not copy unnecessary IDE or build files into the final image.

⸻

Maven Build Standard

Each service must be independently buildable using Maven.

Required Build Command

./mvnw clean package -DskipTests

or, where Maven is installed locally:

mvn clean package -DskipTests

Build Validation

A successful build must produce a JAR file inside:

target/

Example:

target/edgecloud-auth-service-0.0.1-SNAPSHOT.jar

⸻

Reference Microservice Standard

The Auth Service is currently used as the initial reference service for the base Spring Boot microservice template.

It includes:

* Maven project structure
* Java 21 configuration
* Spring Boot main application class
* Externalised application configuration
* Dockerfile support
* Eureka client registration
* MySQL datasource configuration
* Actuator health endpoint support

This reference structure should be reused when creating or correcting future backend services.

⸻

Engineering Rules

Each EdgeCloud Monitor backend service must remain:

* independently buildable
* independently deployable
* independently testable
* independently configurable
* registered with Eureka where required
* connected only to its assigned database
* aligned with the shared package and dependency standard

⸻

Definition of Done Checklist

A backend service follows the base template when:

* Standard package structure exists
* Maven build succeeds
* Required dependencies are included
* Application configuration is externalised
* Dockerfile exists
* Actuator health endpoint is available
* Eureka registration works where required
* Database configuration uses environment variables
* Service name follows naming convention
* Error handling structure is planned or implemented
* Documentation is updated
---
# Build Validation Standard
All EdgeCloud Monitor backend services must be independently buildable.
## Standard Build Commands
Using Maven Wrapper:
```bash
./mvnw clean package -DskipTests

Using local Maven:

mvn clean package -DskipTests

Validation Requirements

The build process must:

* complete successfully
* generate a runnable JAR file
* resolve all dependencies
* pass configuration validation
* support Docker image creation

Expected Output

BUILD SUCCESS

Example output artifact:

target/<service-name>-0.0.1-SNAPSHOT.jar

Current Validation Status

The following services have been successfully built:

* edgecloud-auth-service
* edgecloud-monitoring-service
* edgecloud-device-service
* edgecloud-alert-service
* edgecloud-api-gateway
* edgecloud-discovery-service
