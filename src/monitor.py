import psutil
import time
import logging

logging.basicConfig(
    filename="system_monitor.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def get_system_usage():
    cpu = psutil.cpu_percent(interval=1)
    memory = psutil.virtual_memory().percent
    disk = psutil.disk_usage('/').percent
    return cpu, memory, disk

def log_usage():
    cpu, memory, disk = get_system_usage()
    logging.info(f"CPU: {cpu}%, Memory: {memory}%, Disk: {disk}%")
    print(f"CPU: {cpu}%, Memory: {memory}%, Disk: {disk}%")

if __name__ == "__main__":
    print("Starting system monitoring... (Press Ctrl+C to stop)")
    try:
        while True:
            log_usage()
            time.sleep(5)
    except KeyboardInterrupt:
        print("Monitoring stopped.")
