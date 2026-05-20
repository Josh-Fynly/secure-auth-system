from time import time

requests = {}

LIMIT = 5
WINDOW = 60

def is_rate_limited(ip):
    now = time()

    if ip not in requests:
        requests[ip] = []

    requests[ip] = [
        t for t in requests[ip]
        if now - t < WINDOW
    ]

    if len(requests[ip]) >= LIMIT:
        return True

    requests[ip].append(now)

    return False
