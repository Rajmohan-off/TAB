# ⚡ Transformer Analyzer Bot (TAB)
 Smart IoT- and AI-Powered Transformer Fault Detection & Power Optimization System  

---

## 🧭 Project Overview  

The Transformer Analyzer Bot (TAB) is an innovative system designed to monitor, analyze, and optimize electrical transformers** using **IoT, Cloud Computing, and Machine Learning.  

Developed as part of an academic and applied research initiative, TAB focuses on **fault detection** and **energy efficiency** in power transmission networks — helping prevent outages, minimize losses, and support sustainable grid management.  

---

## 👨‍💻 My Role  

**Rajmohan P — Project Lead & System Architect**  
- Led a **6-member cross-disciplinary team** (EEE & CSE) through end-to-end project delivery.  
- Designed the **project architecture**, integrated **IoT data flow with a Flask cloud backend**, and implemented **ML-based fault detection**.  
- Oversaw code development, version control, and testing pipelines.  
- Presented results demonstrating **~32% energy savings** through optimized load balancing.  

---

## 🚀 Key Highlights  

✅ **IoT-Enabled Monitoring** – Continuous collection of voltage and current data via ESP8266 sensors.  
✅ **Cloud-Based Storage** – Real-time data pushed to a Flask API and stored in SQLite for analytics.  
✅ **Machine Learning Analytics** – Isolation Forest model detects transformer anomalies automatically.  
✅ **Energy Optimization** – Suggests ideal supply levels to reduce wastage (achieving ~32% efficiency gain).  
✅ **Alerting System** – Notifies operators via console or email when abnormalities occur.  
✅ **Simulation-Ready** – Built-in Python simulator to emulate multiple transformer nodes.  

---

## 🧩 Tech Stack  

| Layer | Technologies Used |
|:------|:------------------|
| **IoT Hardware** | ESP8266 / ESP32, Voltage & Current Sensors |
| **Firmware** | MicroPython |
| **Backend** | Flask (Python) |
| **Database** | SQLite + SQLAlchemy ORM |
| **Machine Learning** | scikit-learn (Isolation Forest) |
| **Frontend** | HTML5 + Chart.js Dashboard |
| **Cloud/Automation** | Bolt IoT Cloud, Flask REST API, Docker |

---

## ⚙️ How It Works  

1. **IoT Sensors** measure voltage & current on transformer primary and secondary sides.  
2. Data is transmitted via **ESP8266 Wi-Fi module** to the **Flask cloud server**.  
3. The server stores readings and performs **anomaly detection** using the trained model.  
4. When a fault is detected, an **alert** is triggered with location and cause.  
5. The system continuously analyzes usage patterns and suggests **power-saving strategies**.  

📉 *Result:* Demonstrated up to **32.25% reduction in unnecessary power loss** in simulation scenarios.

---

## 🧪 Local Deployment  

 1️⃣ Clone the Repository
```bash
git clone https://github.com/<your-username>/transformer-analyzer-bot.git
cd transformer-analyzer-bot
2️⃣ Install Dependencies
bash
Copy code
pip install -r server/requirements.txt
3️⃣ Start the Server
bash
Copy code
python server/app.py
4️⃣ Simulate IoT Data
bash
Copy code
python simulator/simulate_esp.py
5️⃣ Train the ML Model
bash
Copy code
python server/model/train_model.py
6️⃣ View Dashboard
Open your browser at http://127.0.0.1:5000


🌐 IoT Device Configuration
MicroPython firmware (see esp/esp_post.py) allows any ESP8266/ESP32 to:

python
Copy code
WIFI_SSID = "your_wifi_name"
WIFI_PASS = "your_wifi_password"
SERVER_URL = "http://<your_pc_ip>:5000/ingest"
The device then automatically posts sensor data every few seconds.

🧠 Machine Learning Pipeline
Model: Isolation Forest
Features: Primary/Secondary Voltage & Current, Voltage and Current Differentials
Training Data: Historical transformer readings
Output: Binary anomaly classification (Normal / Faulty)
Update Cycle: Auto-retraining every 12 hours via background scheduler

🧾 Results
Metric	Traditional System	TAB System	Efficiency Gain
Average Supply (units)	800	542.85	+32.25%

TAB successfully identified periods of energy wastage and adjusted supply dynamically — contributing to smarter grid management.

🧑‍🤝‍🧑 Team
Name	Role
Rajmohan P	Project Lead & System Designer
Rishi Sarvesh U S	Developer (IoT Integration)
Pragathish Ram S	Data Analytics & ML
Santhosh P	Embedded Systems
Naveen R	Testing & Implementation
Syed Moinudeen	Hardware Support
Arun Kumar D	Cloud & Software Engineering
Mr. Ponkumar G	Faculty Guide
