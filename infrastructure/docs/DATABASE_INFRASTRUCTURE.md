# EdgeCloud Monitor Database Infrastructure

## Overview

EdgeCloud Monitor uses a database-per-service architecture. Each backend microservice owns its own isolated MySQL database.

## Databases

| Service | Container | Database | Port |
|---|---|---|---|
| Authentication Service | edgecloud-auth-mysql | auth_db | 3307 |
| Monitoring Service | edgecloud-monitoring-mysql | monitoring_db | 3308 |
| Device Service | edgecloud-device-mysql | device_db | 3309 |
| Alert Service | edgecloud-alert-mysql | alert_db | 3310 |

## Service Connection Properties

### Authentication Service

```yaml
spring:
  datasource:
    url: jdbc:mysql://auth-mysql:3306/auth_db
    username: auth_user
    password: auth_pass
