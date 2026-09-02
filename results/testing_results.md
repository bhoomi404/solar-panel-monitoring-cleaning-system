# Testing Results

## Objective

To verify the operation of the solar panel monitoring system and the automatic dust-cleaning mechanism.

## Testing Procedure

1. Sensor readings were collected from the solar panel using the Raspberry Pi.
2. Voltage, current, power, light intensity, and temperature were monitored.
3. Dust was manually applied to the solar panel for testing.
4. The machine learning model estimated the dust level from the sensor readings.
5. The system monitored consecutive dust detections.
6. After confirmed dust detection, the Raspberry Pi activated the motor driver.
7. The motorized belt/roller mechanism moved across the panel to remove the dust.
8. The panel condition was observed before and after cleaning.

## Observations

- The system successfully collected real-time sensor readings.
- Dust detection was performed using the trained machine learning model.
- Consecutive dust detection was used to confirm the cleaning condition.
- The motor driver was activated automatically after confirmed dust detection.
- The belt/roller mechanism performed the cleaning operation.
- The panel was observed before and after the cleaning operation.

## Testing Evidence

### Before Dust Detection

Add the image showing the clean panel and sensor readings.

### After Dust Detection

Add the image showing the dusty panel and the detected dust condition.

### Cleaning Mechanism

Add the testing video demonstrating the motorized cleaning operation.

## Conclusion

The prototype successfully demonstrated real-time solar panel monitoring, dust detection, and automatic activation of the mechanical cleaning mechanism.
