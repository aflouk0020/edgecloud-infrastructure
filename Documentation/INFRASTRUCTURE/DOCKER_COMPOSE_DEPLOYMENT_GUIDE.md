# EdgeCloud Monitor Docker Compose Deployment Guide
## Purpose
This document describes the Docker Compose deployment architecture used by the EdgeCloud Monitor platform.
The guide provides instructions for deployment, service startup, health validation, troubleshooting, container networking, environment configuration, and evidence collection.
The objective is to ensure that the platform can be deployed consistently across development and testing environments.
---
## Architecture Overview
EdgeCloud Monitor uses a Docker Compose based deployment architecture.
The platform consists of:
- Discovery Service
- API Gateway
- Authentication Service
- Monitoring Service
- Device Service
- Alert Service
Supporting infrastructure:
- Authentication MySQL Database
- Monitoring MySQL Database
- Device MySQL Database
- Alert MySQL Database
All containers communicate through the shared Docker network defined by Docker Compose.
---
## Docker Compose Services
| Service | Port |
|---|---|
| Discovery Service | 8761 |
| API Gateway | 8080 |
| Authentication Service | 8081 |
| Monitoring Service | 8082 |
| Device Service | 8083 |
| Alert Service | 8084 |
| Auth MySQL | 3307 |
| Monitoring MySQL | 3308 |
| Device MySQL | 3309 |
| Alert MySQL | 3310 |
---
## Environment Variables
The platform supports externalised configuration through environment variables.
Examples include:
- SERVER_PORT
- SPRING_DATASOURCE_URL
- SPRING_DATASOURCE_USERNAME
- SPRING_DATASOURCE_PASSWORD
- EUREKA_SERVER_URL
- EUREKA_CLIENT_SERVICEURL_DEFAULTZONE
This approach allows the same container images to be deployed across multiple environments without code changes.
---
## Database Container Architecture
Each backend service owns its own database.
Database ownership follows the database-per-service pattern.
| Service | Database |
|---|---|
| Authentication Service | auth_db |
| Monitoring Service | monitoring_db |
| Device Service | device_db |
| Alert Service | alert_db |
No service directly accesses another service database.
---
## Service Communication
Service communication is performed through Spring Cloud Eureka and REST APIs.
Communication path:
```text
Client → API Gateway → Backend Service

Service discovery path:

Backend Service → Eureka Discovery Server

Docker networking allows containers to communicate using service names rather than IP addresses.

⸻

Health Check Strategy

Spring Boot Actuator is used to provide health monitoring.

Endpoints:

GET /actuator/health
GET /actuator/info

Docker Compose health checks call the health endpoint to determine container readiness.

Validation results confirmed that:

* Discovery Service reported healthy
* API Gateway reported healthy
* Authentication Service reported healthy
* Monitoring Service reported healthy
* Device Service reported healthy
* Alert Service reported healthy
* All MySQL containers reported healthy

⸻

Deployment Procedure

1. Clone all required repositories.
2. Build service applications.
3. Navigate to the Docker Compose folder:

cd infrastructure/docker/compose

4. Start the platform:

docker compose --env-file ../env/.env up --build -d

5. Verify containers:

docker ps

6. Verify health endpoints.

⸻

Startup Procedure

Use:

docker compose --env-file ../env/.env up --build -d

Expected startup order:

1. Databases
2. Discovery Service
3. Backend Services
4. API Gateway

Verify successful startup using:

docker ps

⸻

Shutdown Procedure

Stop containers:

docker compose --env-file ../env/.env down

Remove containers and volumes:

docker compose --env-file ../env/.env down -v

⸻

Troubleshooting Guide

Common issues include:

* Database connection failures
* Eureka registration failures
* Incorrect environment variables
* Docker network configuration errors
* Container build failures
* Health check failures

Recommended checks:

docker logs <container-name>
docker ps
docker compose ps
curl http://localhost:<port>/actuator/health

⸻

Evidence Collection Checklist

Deployment evidence should include:

* Docker Compose startup output
* Container status screenshots
* Eureka dashboard screenshots
* Actuator health responses
* Database container health results
* Successful service registration screenshots
* Docker logs where relevant

⸻

Validation Results

Validation completed successfully.

Observed results:

* All service containers started successfully
* All database containers started successfully
* Docker health checks passed
* Actuator endpoints returned status UP
* Eureka Discovery Server remained operational
* API Gateway remained operational

⸻

Conclusion

The Docker Compose deployment environment provides a repeatable and maintainable deployment mechanism for EdgeCloud Monitor.

The architecture supports service discovery, database isolation, health monitoring, and containerised deployment while maintaining compliance with cloud-native engineering principles.
