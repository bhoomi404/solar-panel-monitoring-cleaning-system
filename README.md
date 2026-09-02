# Solar Panel Monitoring and Automatic Cleaning System

An IoT-based solar panel monitoring and automatic cleaning system developed using Raspberry Pi.

The system monitors the solar panel's electrical and environmental parameters and uses a machine learning model to estimate the dust level. When dust is detected in two consecutive measurements, the system automatically activates a motorized cleaning mechanism.

## Features

- Real-time voltage and current monitoring
- Solar panel power calculation
- Light intensity measurement
- Temperature monitoring
- Machine learning-based dust estimation
- Automatic cleaning mechanism
- Motor control using Raspberry Pi GPIO
- I2C-based sensor communication

## System Components

- Raspberry Pi
- INA219 Voltage/Current Sensor
- BH1750 Light Sensor
- DS18B20 Temperature Sensor
- DC Motors
- Motor Driver
- Solar Panel

## System Workflow

Solar Panel Sensors  
↓  
Raspberry Pi  
↓  
Voltage / Current / Light / Temperature Data  
↓  
Machine Learning Dust Prediction  
↓  
Dust Threshold Detection  
↓  
Two Consecutive Dust Detections  
↓  
Motor Activated  
↓  
Automatic Panel Cleaning

## Technologies

- Python
- Raspberry Pi
- GPIO
- I2C
- Pandas
- Joblib
- Machine Learning

## Project Structure

```text
solar-panel-monitoring-cleaning-system/
│
├── README.md
├── requirements.txt
│
└── src/
    └── solar_monitor.py
