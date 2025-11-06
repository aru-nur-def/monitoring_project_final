#  Monitoring Project — Prometheus + Grafana (AITU, IT-2306)

### Student: Aruzhan Saparkhankyzy

---

## DASHBOARDS OVERVIEW

###  Database Exporter (MySQL)
**Purpose:** Monitors database activity and connection statistics.

**Metrics used:**
- `mysql_global_status_connections`
- `mysql_global_status_threads_connected`
- `mysql_global_status_queries`
- `mysql_global_status_slow_queries`

**Grafana panels:**
- Total connections
- Query rate
- Threads running
- Uptime

 **Target:** `mysql_exporter :9104`  
 **Status:** UP 

---

### 2️ Node Exporter (Windows System Monitoring)
**Purpose:** Tracks CPU, memory, and disk utilization on the local machine.

**Metrics used:**
- `windows_cpu_time_total`
- `windows_cs_physical_memory_bytes`
- `windows_logical_disk_free_bytes`
- `windows_system_threads`

**Grafana panels:**
- CPU Usage %
- Memory Usage %
- Disk Free Space %
- System Threads
- Network Bytes Total

 **Target:** `windows_exporter :9182`  
 **Status:** UP �

---

###  Custom Exporter (Python)
**Purpose:** Simulates environmental metrics (temperature & humidity).  
Runs locally on port `:8000`.

**File:** `custom_exporter.py`

```python
from prometheus_client import start_http_server, Gauge
import random, time

temperature = Gauge('custom_temperature_celsius', 'Random temperature in Celsius')
humidity = Gauge('custom_humidity_percent', 'Random humidity in percent')

if __name__ == "__main__":
    start_http_server(8000)
    print("✅ Custom exporter running at http://localhost:8000/metrics")
    while True:
        temperature.set(random.uniform(15.0, 30.0))
        humidity.set(random.uniform(40.0, 80.0))
        time.sleep(5)
```

**Grafana panels:**
-  Temperature (°C)
-  Humidity (%)

 **Target:** `custom_exporter :8000`  
 **Status:** UP 

---

##  ALERT RULES

| Alert Name | Condition | Duration | Message |
|-------------|------------|-----------|----------|
|  **High Temperature Alert** | `avg(custom_temperature_celsius) > 30` | For 1m | “Temperature exceeded 30°C on Custom Exporter” |
|  **High Humidity Alert** | `avg(custom_humidity_percent) > 70` | For 1m | “Humidity exceeded 70% on Custom Exporter” |

Alerts automatically switch to **“Firing”** in Grafana if thresholds are exceeded.

---

##  COMPONENTS USED

| Component | Role |
|------------|------|
| **Prometheus** | Data collection and time-series storage |
| **Grafana** | Visualization, dashboards, alerting |
| **Windows Exporter** | System metrics |
| **MySQL Exporter** | Database metrics |
| **Custom Exporter** | User-defined Python metrics |

---

##  PROJECT STRUCTURE

```
monitoring_project/
│
├── prometheus.yml
├── docker-compose.yml
├── custom_exporter.py
├── custom_exporter_dashboard.json
├── mysql_dashboard.json
└── README.md
```

---

##  HOW TO RUN

### Step 1. Start Prometheus
```bash
prometheus.exe --config.file=prometheus.yml
```

### Step 2. Start Exporters
```bash
windows_exporter.exe
mysqld_exporter.exe
python custom_exporter.py
```

### Step 3. Open Grafana
Go to → [http://localhost:3000](http://localhost:3000)  
Login → admin / admin  

Import dashboards:
- `mysql_dashboard.json`
- `custom_exporter_dashboard.json`

---

##  RESULTS
- 3 dashboards working in real-time  
- 5 exporters monitored (Prometheus + 3 custom targets + Grafana itself)  
- 2 alert rules successfully tested (temperature & humidity)  
- All metrics visualized and verified via `localhost:9090/targets`  

 **All systems operational**

---

##  GITHUB REPOSITORY
Link: *to be added after upload*  
Folder: `monitoring_project_final`




