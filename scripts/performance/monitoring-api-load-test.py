import requests
import time


URL = "http://localhost:8082/services"

REQUESTS = 100

success = 0
failed = 0

start = time.time()

for i in range(REQUESTS):

    try:
        response = requests.get(URL)

        if response.status_code == 200:
            success += 1
        else:
            failed += 1

    except Exception:
        failed += 1


end = time.time()

duration = end - start

print("Monitoring API Load Test")
print("------------------------")
print(f"Requests: {REQUESTS}")
print(f"Successful: {success}")
print(f"Failed: {failed}")
print(f"Total time: {duration:.2f}s")
print(f"Average response: {(duration / REQUESTS) * 1000:.2f} ms")
