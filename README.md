# ☁️ Cloud-Native PostgreSQL Backup to S3 (MinIO)

## 📌 Project Overview
An automated, infrastructure-agnostic solution for backing up PostgreSQL databases and transferring them to an S3-compatible Object Storage (MinIO). This repo demonstrates cloud engineering basics, including containerization, automated scripting, data compression, and Linux background job scheduling.

## 🏗️ Architecture & Tech Stack
* **Database:** PostgreSQL (Containerized via Docker)
* **Object Storage:** MinIO (Local S3-compatible cloud environment via Docker)
* **Automation Brain:** Python 3 (`subprocess`, `gzip`, `logging`)
* **Data Transfer:** `rclone` (Configured for S3 endpoints)
* **OS & Scheduling:** Linux (Ubuntu via WSL 2) / `cron` daemon

## ✨ Key Features
1. **Automated Dumps:** Executes `pg_dump` directly from the running database container.
2. **Storage Optimization:** Implements `gzip` compression before transfer, saving bandwidth and cloud storage costs.
3. **Secure Transfer:** Uses `rclone` to push artifacts to isolated S3 buckets.
4. **Robust Logging:** Generates detailed `backup_manager.log` files with timestamps and execution status for easy troubleshooting.
5. **Zero-Touch Execution:** Fully integrated with Linux `cron` for daily, unattended executions.

## 🚀 How It Works (The Pipeline)
1. `cron` triggers the `backup_manager.py` script at the scheduled time (e.g., 2:00 AM).
2. Python generates a dynamic timestamped filename.
3. Python calls the Docker API to execute a database dump.
4. The raw `.sql` file is compressed to `.sql.gz`.
5. `rclone` authenticates with the MinIO server and uploads the compressed artifact.
6. The script cleans up local temporary files and logs the success/failure status.

## 💡 Why this project?
I wanted to simulate a Cloud/DevOps task: ensuring data durability without relying on manual operations. It showcases the ability to connect various infrastructure components (Containers, Object Storage, Linux OS) using code.