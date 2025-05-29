# FastAPI Daemon Creation and Hosting Endpoint for Language Detection API

**Author:** Abhijeet Thorat  
**Description:** This guide explains how to create a systemd service to host a FastAPI-based language detection API as a background daemon on an Ubuntu system.

---

## 📦 Project Overview

This project provides a RESTful API for detecting the language of input text. The API is built using **FastAPI** and served using **Uvicorn**.

The service is configured to run continuously in the background as a **daemon** using **systemd** on Ubuntu.

---

## 🛠 Environment Setup

1. Clone or copy the FastAPI project to a working directory:

    ```bash
    cd /home/joy/temp_lang_id_service


2. Create and activate a Python virtual environment:

    ```bash

    python3 -m venv /home/joy/test_env
    source /home/joy/test_env/bin/activate

3. Install required dependencies:

   ```bash

    pip install fastapi uvicorn

4. Ensure app.py contains the FastAPI app:

   ```python
   
    from fastapi import FastAPI

    app = FastAPI()

    @app.get("/")
    def read_root():
        return {"message": "Language Detection API is live"}

## ⚙️ systemd Service Configuration

Create a systemd service file to run the FastAPI application as a daemon:

## File Path:

    /etc/systemd/system/fastapi.service

## File Content:

    [Unit]
    Description=FastAPI Language Detection service
    After=network.target

    [Service]
    User=root
    Group=root
    WorkingDirectory=/home/joy/temp_lang_id_service
    ExecStart=/home/joy/test_env/bin/uvicorn app:app --host 0.0.0.0 --port 8000
    Restart=always

    [Install]
    WantedBy=multi-user.target

## 🚀 Enable and Start the Service

Run the following commands to register, enable, and start the FastAPI daemon:

    bash

    sudo systemctl daemon-reexec
    sudo systemctl daemon-reload
    sudo systemctl enable fastapi.service
    sudo systemctl start fastapi.service


## 🔍 Service Monitoring and Logs

Check the status of the FastAPI service:

    sudo systemctl status fastapi.service

## View real-time logs:

    sudo journalctl -u fastapi.service -f

## 🌐 Access the API

### Once the service is running, the API will be accessible on:

    http://<your-server-ip>:8000

### Try accessing:

    http://<your-server-ip>:8000/

### You should receive a response like:

    json
    {
    "message": "Language Detection API is live"
    }


## 🧩 Notes
    Ensure port 8000 is open in your firewall or server configuration.

    Replace User and Group with a non-root user for production environments.

    You can modify the ExecStart command to use Gunicorn for production readiness if needed.