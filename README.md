
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
````

## Sensor Monitoring

The system measures:

* Voltage
* Current
* Power
* Light intensity
* Temperature
* Dust level

Power is calculated using:

```text
Power = Voltage × Current
```

## Dust Detection

The system uses consecutive dust detections to reduce false cleaning triggers.

```text
Sensor Reading
      ↓
Dust Prediction
      ↓
Dust Above Threshold?
   ↓           ↓
  No          Yes
  ↓            ↓
Clean     First Detection
               ↓
          Next Reading
               ↓
       Dust Still Detected?
          ↓          ↓
         No         Yes
         ↓           ↓
       Reset     Confirm Dust
                     ↓
                Start Cleaning
```

## Motor Control

The Raspberry Pi controls the L298N motor driver through GPIO.

The cleaning cycle consists of:

```text
Forward → Stop → Reverse → Stop
```

The motors drive the belt/roller mechanism across the solar panel to remove dust.

## Circuit Diagram

![Circuit Diagram](hardware/circuit_diagram.png)

## Prototype

![Solar Panel Prototype](images/prototype.png)

## Cleaning Mechanism

![Dust Cleaning Mechanism](images/dust_cleaning.png)

## Testing

The system was tested by manually applying dust to the solar panel and observing sensor readings, dust prediction, motor activation, and the cleaning operation.

### Testing Video

[View Testing Video](results/Testing_Results.mp4)

### Testing Results

[View Testing Results](results/testing_results.md)

## Challenges Faced

* Motor powering issue
* False dust detection
* Selection of an effective cleaning mechanism
* Light intensity sensor failure after soldering
* Machine learning model selection

## Technologies Used

* Python
* Raspberry Pi
* GPIO
* I2C
* PWM
* Random Forest
* Pandas
* Joblib

## Repository Structure

```text
solar-panel-monitoring-cleaning-system/
│
├── README.md
├── requirements.txt
├── .gitignore
│
├── src/
│   └── solar_monitor.py
│
├── model/
│   └── dust_model.pkl
│
├── hardware/
│   └── circuit_diagram.png
│
├── results/
│   ├── Testing_Results.mp4
│   └── testing_results.md
│
└── images/
    ├── prototype.png
    └── dust_cleaning.png
```

## Future Scope

* System automation
* Commercial scaling
* Infrastructure development
* Cost optimization
* Predictive maintenance
* Energy storage enhancement
* Battery health monitoring
* Energy optimization


