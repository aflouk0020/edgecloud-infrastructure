# SCRUM-103 Performance and Load Observation Testing

## 1. Overview

This document records the lightweight performance and load observation testing performed for EdgeCloud Monitor.

The objective of this testing was to evaluate basic scalability awareness, API responsiveness, telemetry ingestion behaviour, alert workflow stability, dashboard responsiveness, and Docker container behaviour under increased system activity.

This testing was designed as an operational observation exercise rather than enterprise-scale benchmarking.

---

# 2. Test Environment

## Platform

EdgeCloud Monitor cloud-native monitoring platform.

## Architecture Components Tested

- Spring Boot microservices
- Monitoring Service
- Alert Service
- React Dashboard
- Docker Compose deployment
- MySQL service databases
- REST API communication

## Execution Environment

Hardware:
- Apple MacBook Air

Deployment:
- Local Docker Compose environment

Testing tools:
- Python request scripts
- curl
- Docker stats
- Browser developer tools

---

# 3. Monitoring API Load Test

## Objective

Evaluate whether the Monitoring Service continues responding correctly when repeated monitoring requests are executed.

## Endpoint Tested

GET http://localhost:8082/services

## Method

A Python-based request script generated 100 repeated API requests.

## Results

| Metric | Result |
|---|---|
| Total Requests | 100 |
| Successful Requests | 100 |
| Failed Requests | 0 |
| Total Duration | 0.97 seconds |
| Average Response Time | 9.71 ms |

## Observation

The Monitoring Service successfully processed all requests without failures.

The response latency remained low during repeated access, demonstrating stable behaviour under lightweight request activity.

Status:

PASS

---

# 4. Telemetry Submission Load Test

## Objective

Evaluate telemetry ingestion behaviour when multiple telemetry submissions are received.

## Endpoint Tested

POST http://localhost:8082/telemetry

## Test Payload

Example telemetry data:

```json
{
  "deviceId": "load-test-device",
  "cpuUsage": 45.5,
  "memoryUsage": 60.0,
  "temperature": 40.0
}
Method
A Python script submitted 100 telemetry requests sequentially.
Results
Metric	Result
Total Requests	100
Successful Requests	100
Failed Requests	0
Total Duration	0.94 seconds
Average Response Time	9.44 ms

Verification
Telemetry records were retrieved successfully after testing.
Verified fields:
device identifier
CPU usage
memory usage
temperature
heartbeat status
recorded timestamp
Observation
The Monitoring Service continued storing telemetry successfully without request failures.
Status:
PASS
5. Alert Workflow Stability Test
Objective
Evaluate alert generation and retrieval behaviour when multiple monitoring events occur.
Method
20 simulated SERVICE_DOWN alerts were generated.
Example:
{
  "alertType": "SERVICE_DOWN",
  "severity": "HIGH",
  "message": "Load test alert",
  "sourceService": "load-test-service"
}
Results
All alert requests were accepted successfully.
The generated alerts contained:
alert type
severity
source service
active status
root cause suggestion
Notification retrieval was verified using:
GET http://localhost:8084/notifications/count
Observation
The Alert Service remained functional during increased alert activity.
Status:
PASS
6. Docker Resource Observation
Objective
Observe container stability and resource usage during increased activity.
Method
Docker container resources were monitored using:
docker stats
Observations
Example resource usage:
Container	CPU	Memory
Monitoring Service	Low usage	~532 MB
Alert Service	Low usage	~500 MB
API Gateway	Low usage	~432 MB
Device Service	Low usage	~502 MB

Observation
No container crashes, restarts, or abnormal resource consumption were observed.
The Docker Compose environment remained stable throughout testing.
Status:
PASS
7. Dashboard Responsiveness Observation
Objective
Evaluate dashboard usability while backend monitoring activity increased.
Method
The React dashboard was refreshed during backend load activity.
Observed:
dashboard remained accessible
API requests continued responding
interface remained usable
Observation
No visible performance degradation was observed during lightweight backend load testing.
Status:
PASS
8. Evidence Collected
Evidence stored in:
documentation/testing/SCRUM-103/screenshots
Evidence includes:
Monitoring API test results
Telemetry submission results
Alert workflow results
Docker resource observations
Dashboard responsiveness screenshots
9. Conclusion
The SCRUM-103 performance and load observation testing demonstrated that EdgeCloud Monitor maintains stable behaviour under lightweight increased activity.
The Monitoring Service successfully processed repeated API requests, telemetry ingestion remained reliable, alert workflows continued functioning, and Docker containers remained stable.
The results demonstrate basic scalability awareness and operational monitoring capability.
Future improvements could include:
concurrent load generation
automated performance pipelines
Prometheus metrics collection
Grafana dashboard monitoring
larger-scale benchmarking environments

