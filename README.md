
# Smart Solar Energy Management & Automatic Cleaning System

An IoT-based solar panel monitoring and automatic cleaning system that
combines real-time sensor monitoring, machine learning-based dust detection,
and a motorized cleaning mechanism.

---

## Overview

Dust accumulation on solar panels can reduce their efficiency, while manual
cleaning is labor-intensive, costly, and irregular.

This project develops an automated system that monitors solar panel
parameters, estimates dust accumulation using machine learning, and activates
a motorized cleaning mechanism when cleaning is required.

The system integrates:

- Real-time solar panel monitoring
- Sensor-based data collection
- Machine learning-based dust prediction
- Raspberry Pi processing and control
- Automated motorized cleaning
- Hardware-software integration

---

## Problem Statement

Solar panels can experience significant performance losses due to dust
accumulation. Manual cleaning requires regular human intervention and may not
be performed consistently.

The proposed system aims to automate the monitoring and cleaning process by
using sensor data and an intelligent cleaning trigger.

---

## Proposed Solution

The system collects electrical and environmental parameters from the solar
panel using multiple sensors.

The collected data is processed by a machine learning model running on the
Raspberry Pi. The model estimates the dust condition and determines when the
cleaning mechanism should be activated.

Once the dust condition is confirmed, the Raspberry Pi controls the motor
driver to operate the belt/roller-based cleaning mechanism.

---

## System Architecture

```text
                         SOLAR PANEL
                              │
              ┌───────────────┼───────────────┐
              │               │               │
           INA219           BH1750          DS18B20
       Voltage/Current    Light Intensity   Temperature
              │               │               │
              └───────────────┼───────────────┘
                              │
                              ▼
                       RASPBERRY PI
                              │
                       Sensor Readings
                              │
                              ▼
                   MACHINE LEARNING MODEL
                       Random Forest
                              │
                              ▼
                      DUST PREDICTION
                              │
                              ▼
                    CLEANING DECISION
                              │
                              ▼
                       MOTOR DRIVER
                              │
                              ▼
                         DC MOTORS
                              │
                              ▼
                    BELT / ROLLER SYSTEM
                              │
                              ▼
                     PANEL CLEANING
````

---

## Hardware Components

| Component                  | Function                           |
| -------------------------- | ---------------------------------- |
| Raspberry Pi               | Main processing and control unit   |
| INA219 Current Sensor      | Voltage and current measurement    |
| BH1750 Light Sensor        | Light intensity measurement        |
| DS18B20 Temperature Sensor | Temperature measurement            |
| L298N Motor Driver         | Motor direction and speed control  |
| DC Motors                  | Drive the cleaning mechanism       |
| Solar Panel                | Energy source and test panel       |
| Belt/Roller Mechanism      | Mechanical dust-cleaning mechanism |

The project hardware architecture and component integration are documented
in the project presentation. 

---

## Machine Learning

The machine learning model acts as the intelligence layer of the system.

### Data Collection

Sensor readings are collected through the Raspberry Pi, including:

* Temperature
* Light intensity
* Voltage
* Current

The project also considers limit-switch position and motor-driver feedback
for system operation. 

### Data Processing

The collected sensor values are cleaned and processed.

Dust conditions are categorized using changes in light intensity and voltage
patterns.

### Model

A **Random Forest Classifier** was trained using the collected dataset.

### Input Features

```text
Temperature
Light Intensity
Voltage
Current
```

### Prediction

The model is used to estimate the dust condition and determine whether the
cleaning mechanism should be triggered.

The trained model is loaded on the Raspberry Pi for real-time prediction.


---

## Embedded Software

The monitoring and cleaning system is implemented in Python on Raspberry Pi.

The program performs the following operations:

1. Reads voltage and current using the INA219 sensor.
2. Reads light intensity using the BH1750 sensor.
3. Reads temperature using the DS18B20 sensor.
4. Calculates solar panel power.
5. Creates a sensor-data input for the ML model.
6. Predicts the dust level.
7. Checks the dust condition.
8. Confirms consecutive dust detections.
9. Activates the motor driver.
10. Runs the cleaning mechanism.
11. Stops the motor after the cleaning cycle.

---

## Sensor Monitoring

The system continuously monitors:

```text
Voltage
Current
Power
Light Intensity
Temperature
Dust Level
```

Power is calculated from the measured voltage and current:

```text
Power = Voltage × Current
```

The sensor readings and predicted dust level are displayed with a timestamp
during system operation.

---

## Dust Detection Logic

To reduce false activation, the cleaning mechanism is triggered only after
the dust condition is confirmed through consecutive detections.

```text
             Sensor Data
                  │
                  ▼
          ML Dust Prediction
                  │
                  ▼
        Dust Above Threshold?
             /          \
           No            Yes
           │              │
       Panel Clean   First Detection
                          │
                          ▼
                   Next Measurement
                          │
                          ▼
                  Dust Still Detected?
                       /       \
                     No         Yes
                     │           │
                 Reset Flag   Confirm Dust
                                 │
                                 ▼
                          Start Cleaning
```

---

## Motor Control

The Raspberry Pi controls the L298N motor driver through GPIO pins.

The cleaning cycle consists of:

```text
Forward Movement
       ↓
      Stop
       ↓
Reverse Movement
       ↓
      Stop
```

PWM control is used to control the motor speed.

The belt/roller mechanism transfers the motor rotation into physical
movement across the solar panel.

---

## Hardware Prototype

The physical prototype consists of:

* Solar panel
* Cardboard structural frame
* DC motors
* Wheels
* Belt/track mechanism
* Roller-based cleaning mechanism
* Raspberry Pi
* Motor driver
* Sensors

The solar panel was positioned centrally on the prototype frame, while the
motors and belt mechanism were integrated to provide movement and cleaning.


---

## Cleaning Mechanism

The cleaning mechanism uses DC motors connected to a motor driver.

The Raspberry Pi sends control signals to the motor driver, which controls the
direction and speed of the motors.

A belt/roller mechanism attached to the motor shaft moves across the panel
surface and removes dust.

For testing, dust was manually applied to the solar panel and the cleaning
operation was observed before and after activation. 

---

## Testing

The system was tested under dusty conditions to verify:

* Sensor data acquisition
* Dust detection
* Cleaning-trigger logic
* Motor control
* Mechanical cleaning operation

During testing, dust was manually applied to the solar panel. The Raspberry
Pi ran the monitoring and cleaning program, and the motor driver was
activated when the cleaning condition was detected.

The belt/roller mechanism then moved across the panel to remove the dust.


### Testing Evidence

#### Circuit Diagram

![Circuit Diagram](hardware/circuit_diagram.png)

#### Prototype

![Prototype](images/prototype.jpg)

#### Before Cleaning

![Before Cleaning](results/before_cleaning.jpg)

#### After Cleaning

![After Cleaning](results/after_cleaning.jpg)

#### Cleaning Test Video

Add the prototype testing video demonstrating the automatic cleaning
mechanism.

---

## Challenges Faced

During development, the following challenges were encountered:

* **Motor Powering:** Ensuring reliable power delivery to the motors.
* **False Detection:** Preventing cleaning activation from incorrect dust
  predictions.
* **Cleaning Mechanism:** Finding an effective method for removing dust.
* **Sensor Failure:** Troubleshooting light-intensity sensor failure after
  soldering.
* **ML Model Selection:** Selecting a suitable machine learning model for
  dust detection.

These challenges involved both hardware debugging and software/model
development. 

---

## Technologies Used

### Programming

* Python

### Embedded Systems

* Raspberry Pi
* GPIO
* I2C
* PWM

### Sensors

* INA219
* BH1750
* DS18B20

### Machine Learning

* Random Forest
* Pandas
* Joblib

### Hardware

* L298N Motor Driver
* DC Motors
* Solar Panel
* Belt/Roller Cleaning Mechanism

---

## Project Structure

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
│   ├── before_cleaning.jpg
│   ├── after_cleaning.jpg
│   └── testing_results.md
│
└── images/
    └── prototype.jpg
```

---

## Future Scope

The system can be further developed toward:

1. Greater system automation
2. Commercial-scale deployment
3. Infrastructure development
4. Cost optimization
5. Predictive maintenance
6. Energy storage enhancement
7. Battery health monitoring
8. Energy optimization

These areas are identified as future development directions in the project
presentation. 

---

## Project Outcome

The project demonstrates the integration of:

```text
Sensor Interfacing
       +
Embedded Control
       +
Machine Learning
       +
Motor Control
       +
Mechanical Automation
```

The prototype demonstrates real-time solar panel monitoring, ML-based dust
detection, and automatic activation of a mechanical cleaning mechanism.

---



