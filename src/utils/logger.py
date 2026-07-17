import time

def log_event(message):
    with open('logs/nocbox.log', "a") as logs:
        timestamp = time.time()
        timestamp = time.ctime(timestamp)
        logs.write(f"{timestamp} | {message}\n")
