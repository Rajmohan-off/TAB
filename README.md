Transformer Analyzer Bot (TAB)
IoT + Cloud + Machine Learning based Transformer Monitoring and Energy Optimization System
**Overview
**
The Transformer Analyzer Bot (TAB) is an intelligent monitoring system designed to detect faults, analyze transformer performance, and optimize power usage using IoT, Cloud Computing, and Machine Learning.

It integrates sensors, a microcontroller (ESP8266/ESP32), and a cloud-hosted Python backend (Flask + SQLite) to collect and analyze real-time data from transformers. Using machine-learning-based anomaly detection, TAB identifies abnormal voltage/current behavior and suggests power-saving strategies.

** Key Features
**
- Real-time Monitoring: Captures voltage and current data from transformers via IoT sensors.

- Cloud Connectivity: Data is continuously uploaded to a Flask web server and stored in a database.

- Machine Learning Analysis: Detects faults using an Isolation Forest model trained on historical data.

- Smart Alerts: Triggers alerts (console or email) when anomalies are detected.

- Web Dashboard: Visualizes live and historical sensor data using Chart.js.

- Power Optimization Insight: Identifies excessive load or idle energy losses.

- Simulation Mode: Includes a Python data simulator to mimic multiple ESP devices for testing.
