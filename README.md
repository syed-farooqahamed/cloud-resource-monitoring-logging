# 🌐 Cloud Resource Monitoring & Logging System

## 📌 Overview
This project monitors system resources (CPU, Memory, Disk) and logs usage in real-time.  
It works **locally by default** and is also structured for **Google Cloud Logging integration** (optional).  

## ⚡ Features
- Logs CPU, Memory, and Disk usage every 5 seconds.
- Local logging to console and log file (`system_monitor.log`).
- Cloud-ready: Can push logs to **Google Cloud Logging** (requires a billing-enabled GCP account).

## 🛠️ Tech Stack
- **Python 3**
- **psutil** → resource monitoring
- **google-cloud-logging** → cloud integration (optional)
- **Google Cloud SDK (gcloud)** → authentication & API access
