import psutil
import time
import google.cloud.logging
import logging
from google.cloud.logging.handlers import CloudLoggingHandler
from google.cloud.logging_v2.resource import Resource

client = google.cloud.logging.Client()
resource = Resource(type="global", labels={})
cloud_handler = CloudLoggingHandler(client, resource=resource)
cloud_logger = logging.getLogger("system-monitor")
cloud_logger.setLevel(logging.INFO)
cloud_logger.addHandler(cloud_handler)

def get_system_usage():
    cpu = psutil.cpu_percent(interval=1)
    memory = psutil.virtual_memory().percent
    disk = psutil.disk_usage('/').percent
    return cpu, memory, disk

def log_usage():
    cpu, memory, disk = get_system_usage()
    msg = f"CPU: {cpu}%, Memory: {memory}%, Disk: {disk}%"
    cloud_logger.info(msg)
    print(msg)

if __name__ == "__main__":
    print("Starting Cloud Monitoring... (Press Ctrl+C to stop)")
    try:
        while True:
            log_usage()
            time.sleep(5)
    except KeyboardInterrupt:
        print("Monitoring stopped.")
