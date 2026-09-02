# Smart Solar Energy Management System

An IoT-based solar panel monitoring and automatic cleaning system using Raspberry Pi, sensors, machine learning, and a motorized cleaning mechanism.

## Overview

The system monitors solar panel voltage, current, power, light intensity, and temperature in real time. A machine learning model estimates the dust level and triggers the cleaning mechanism when dust is detected in consecutive readings.

## Hardware Components

- Raspberry Pi
- INA219 Voltage/Current Sensor
- BH1750 Light Intensity Sensor
- DS18B20 Temperature Sensor
- L298N Motor Driver
- DC Motors
- Solar Panel
- Belt/Roller Cleaning Mechanism

## Machine Learning

A Random Forest Classifier is used for dust detection.

### Input Features

- Temperature
- Light intensity
- Voltage
- Current

The trained model is deployed on the Raspberry Pi for real-time prediction.

## System Workflow

```text
Sensor Data
     ↓
Raspberry Pi
     ↓
Data Processing
     ↓
Random Forest Model
     ↓
Dust Prediction
     ↓
Cleaning Decision
     ↓
Motor Driver
     ↓
DC Motors
     ↓
Belt/Roller Cleaning Mechanism
