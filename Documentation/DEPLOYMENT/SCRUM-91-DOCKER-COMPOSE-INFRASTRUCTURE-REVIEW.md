# SCRUM-91 — Docker Compose Infrastructure Review and Optimisation

## Overview

This document records the review and optimisation of the EdgeCloud Monitor Docker Compose infrastructure.

The objective was to improve startup reliability, container recovery behaviour, configuration maintainability, and deployment consistency without changing backend application functionality.

## Infrastructure Reviewed

The Docker Compose environment contains:

- Discovery Service
- API Gateway
- Authentication Service
- Monitoring Service
- Device Service
- Alert Service
- Authentication MySQL database
- Monitoring MySQL database
- Device MySQL database
- Alert MySQL database
- Shared Docker bridge network
- Persistent MySQL volumes

## Configuration Review

The following areas were reviewed:

- service definitions
- container naming
- environment variables
- exposed ports
- Docker networking
- health checks
- startup dependencies
- restart behaviour
- persistent storage
- Eureka registration
- Docker logs

## Container Naming

Container names follow the consistent `edgecloud-*` convention.

Examples include:

- edgecloud-discovery-service
- edgecloud-api-gateway
- edgecloud-auth-service
- edgecloud-monitoring-service
- edgecloud-device-service
- edgecloud-alert-service

Result: Passed

## Environment Variables

Database credentials, database ports, service discovery URLs, and Gateway configuration are externalised through the Docker environment file.

The environment file is excluded from Git and is used only for local development and deployment.

Result: Passed

## Docker Networking

All application services and databases communicate through the shared `edgecloud-network` bridge network.

Internal communication uses Compose service names such as:

- auth-mysql
- monitoring-mysql
- device-mysql
- alert-mysql
- discovery-service

Result: Passed

## Health Checks

Health checks are configured for:

- Discovery Service
- API Gateway
- Authentication Service
- Monitoring Service
- Device Service
- Alert Service
- all MySQL database containers

Application health checks use Spring Boot Actuator endpoints.

Database health checks use `mysqladmin ping`.

Result: Passed

## Startup Dependency Optimisation

The Compose configuration was updated so application services wait for healthy dependencies rather than only waiting for container creation.

The following improvements were applied:

- Authentication Service waits for healthy Discovery and Authentication MySQL.
- Monitoring Service waits for healthy Discovery and Monitoring MySQL.
- Device Service waits for healthy Discovery and Device MySQL.
- Alert Service waits for healthy Discovery and Alert MySQL.
- API Gateway waits for healthy Discovery Service.

This reduces startup race conditions and improves deployment reliability.

Result: Passed

## Restart Policy Optimisation

The following application containers now use:

```yaml
restart: unless-stopped
* Discovery Service
* API Gateway
* Authentication Service
* Monitoring Service
* Device Service
* Alert Service

This improves automatic recovery after unexpected container termination or Docker daemon restart.

Result: Passed

Deployment Validation

The full Compose environment was stopped and restarted after the configuration changes.

Validation confirmed:

* all containers started successfully
* all health checks passed
* all backend services registered with Eureka
* every registered service reported an UP state
* the React dashboard loaded successfully
* telemetry data remained accessible
* persisted database records remained intact
* no fatal startup errors were observed

Result: Passed

Log Review

Docker logs confirmed:

* successful application startup
* successful Eureka discovery requests
* Eureka registration responses with status 204
* Spring Boot services started on the expected ports
* MySQL databases reached ready-for-connections state

Standard MySQL development warnings were observed relating to self-signed certificates, deprecated host-cache syntax, and pid-file location. These warnings did not prevent successful startup or operation.

Result: Passed

Evidence Collected

Evidence includes:

* Docker Compose service status
* Eureka service registration screenshot
* React Telemetry dashboard screenshot
* Docker startup logs
* Compose configuration diff
* successful configuration validation

Validation Summary
Review Area

Result

Compose structure

Passed

Environment variables

Passed

Container naming

Passed

Docker networking

Passed

Health checks

Passed

Startup dependencies

Passed

Restart policies

Passed

Eureka registration

Passed

Dashboard operation

Passed

Database persistence

Passed

Log review

Passed
Conclusion

The Docker Compose infrastructure was successfully reviewed and improved.

The updated configuration provides more reliable startup ordering, consistent restart behaviour, clear service ownership, shared networking, persistent storage, and health-based dependency management.

No backend application functionality, API contracts, database schemas, service ports, or container names were changed.

The EdgeCloud Monitor deployment remains stable and is better prepared for future platform development and demonstration workflows.
