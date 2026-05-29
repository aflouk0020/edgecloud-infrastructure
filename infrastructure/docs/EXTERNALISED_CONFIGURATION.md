# Externalised Configuration

## Purpose

This document defines the environment variables used by the EdgeCloud Monitor platform.

The platform uses externalised configuration so that services can run consistently across local development, Docker Compose, and future cloud deployment environments.

---

## Configuration Principles

- Service configuration must not be hardcoded in application code.
- Runtime values are supplied using environment variables.
- Local development defaults are provided in `application.yml`.
- Docker Compose uses an environment file for container configuration.
- Sensitive values should be stored in local `.env` files and excluded from Git.
- Example values are documented in `.env.example`.

---

## Shared Variables

| Variable | Purpose | Example |
|---|---|---|
| SERVER_PORT | Defines the runtime port for a Spring Boot service | 8081 |
| EUREKA_SERVER_URL | Defines the Eureka service registry URL | http://localhost:8761/eureka/ |
| EUREKA_CLIENT_SERVICEURL_DEFAULTZONE | Defines the API Gateway Eureka client registry URL | http://localhost:8761/eureka/ |

---

## Database Variables

| Variable | Purpose | Example |
|---|---|---|
| SPRING_DATASOURCE_URL | JDBC database connection URL | jdbc:mysql://localhost:3307/auth_db |
| SPRING_DATASOURCE_USERNAME | Database username | auth_user |
| SPRING_DATASOURCE_PASSWORD | Database password | auth_pass |
| SPRING_JPA_HIBERNATE_DDL_AUTO | Hibernate schema update mode | update |
| SPRING_JPA_SHOW_SQL | Enables or disables SQL logging | true |

---

## Docker Compose Environment Variables

| Variable | Purpose | Example |
|---|---|---|
| DISCOVERY_PORT | Host port for Discovery Service | 8761 |
| GATEWAY_PORT | Host port for API Gateway | 8080 |
| AUTH_DB_NAME | Authentication database name | auth_db |
| AUTH_DB_USER | Authentication database user | auth_user |
| AUTH_DB_PASSWORD | Authentication database password | auth_pass |
| AUTH_DB_ROOT_PASSWORD | Authentication database root password | root |
| AUTH_DB_PORT | Authentication database host port | 3307 |
| MONITORING_DB_NAME | Monitoring database name | monitoring_db |
| MONITORING_DB_USER | Monitoring database user | monitoring_user |
| MONITORING_DB_PASSWORD | Monitoring database password | monitoring_pass |
| MONITORING_DB_ROOT_PASSWORD | Monitoring database root password | root |
| MONITORING_DB_PORT | Monitoring database host port | 3308 |
| DEVICE_DB_NAME | Device database name | device_db |
| DEVICE_DB_USER | Device database user | device_user |
| DEVICE_DB_PASSWORD | Device database password | device_pass |
| DEVICE_DB_ROOT_PASSWORD | Device database root password | root |
| DEVICE_DB_PORT | Device database host port | 3309 |
| ALERT_DB_NAME | Alert database name | alert_db |
| ALERT_DB_USER | Alert database user | alert_user |
| ALERT_DB_PASSWORD | Alert database password | alert_pass |
| ALERT_DB_ROOT_PASSWORD | Alert database root password | root |
| ALERT_DB_PORT | Alert database host port | 3310 |

---

## Local Development

Each service includes fallback values in its application configuration.

Example:

```yaml
spring:
  datasource:
    url: ${SPRING_DATASOURCE_URL:jdbc:mysql://localhost:3307/auth_db}
    username: ${SPRING_DATASOURCE_USERNAME:auth_user}
    password: ${SPRING_DATASOURCE_PASSWORD:auth_pass}
