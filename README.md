# Python System Monitor

A real-time system monitoring tool built with Python to track system resource usage and simulate basic infrastructure monitoring workflows.

---

## Features

* Live CPU monitoring
* RAM usage tracking
* Disk usage monitoring
* Warning alerts for high resource usage
* Colored terminal interface
* Real-time refresh updates
* Automatic logging for critical events

---

## Technologies Used

* Python
* psutil
* colorama

---

## Project Structure

```text
sys-monitor/
│
├── monitor.py
├── logs.txt
├── requirements.txt
├── README.md
├── Dockerfile
└── screenshots/
```

---

## Installation

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## Run the Project

```bash
python monitor.py
```

---

## Docker Support

Build Docker image:

```bash
docker build -t system-monitor .
```

Run container:

```bash
docker run system-monitor
```

---

## Future Improvements

* Email alert system
* Web dashboard
* Historical analytics
* AWS integration
* Grafana/Prometheus integration
* Cloud deployment

---

## Author

Yadnesh Kulkarni
