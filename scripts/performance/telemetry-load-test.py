import requests
import time


URL = "http://localhost:8082/telemetry"

REQUESTS = 100

success = 0
failed = 0

payload = {
    "deviceId": "load-test-device",
    "cpuUsage": 45.5,
    "memoryUsage": 60.0,
    "temperature": 40.0
}


start = time.time()

for i in range(REQUESTS):

    try:
        response = requests.post(
            URL,
            json=payload
        )

        if response.status_code == 201:
            success += 1
        else:
            failed += 1

    except Exception:
        failed += 1


end = time.time()

duration = end - start

print("Telemetry Submission Load Test")
print("------------------------------")
print(f"Requests: {REQUESTS}")
print(f"Successful: {success}")
print(f"Failed: {failed}")
print(f"Total time: {duration:.2f}s")
print(f"Average response: {(duration / REQUESTS) * 1000:.2f} ms")
