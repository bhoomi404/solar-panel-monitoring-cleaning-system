import time
import glob
from datetime import datetime

import joblib
import pandas as pd
import RPi.GPIO as GPIO
import board
import busio

from adafruit_ina219 import INA219
import adafruit_bh1750


# -----------------------------
# Configuration
# -----------------------------
DUST_HIGH = 30
SAMPLE_TIME = 10

MODEL_PATH = "model/dust_model.pkl"

model = joblib.load(MODEL_PATH)


# -----------------------------
# Motor Control
# -----------------------------
class SolarCleanerMotor:
    def __init__(self, in1, in2, in3, in4, ena, enb):

        self.in1 = in1
        self.in2 = in2
        self.in3 = in3
        self.in4 = in4
        self.ena = ena
        self.enb = enb

        GPIO.setmode(GPIO.BCM)

        for pin in [in1, in2, in3, in4, ena, enb]:
            GPIO.setup(pin, GPIO.OUT)

        self.pwmA = GPIO.PWM(self.ena, 100)
        self.pwmB = GPIO.PWM(self.enb, 100)

        self.pwmA.start(0)
        self.pwmB.start(0)

    def forward(self, speed):
        GPIO.output(self.in1, GPIO.HIGH)
        GPIO.output(self.in2, GPIO.LOW)

        GPIO.output(self.in3, GPIO.HIGH)
        GPIO.output(self.in4, GPIO.LOW)

        self.set_speed(speed)

    def reverse(self, speed):
        GPIO.output(self.in1, GPIO.LOW)
        GPIO.output(self.in2, GPIO.HIGH)

        GPIO.output(self.in3, GPIO.LOW)
        GPIO.output(self.in4, GPIO.HIGH)

        self.set_speed(speed)

    def stop(self):
        self.set_speed(0)

        GPIO.output(self.in1, GPIO.LOW)
        GPIO.output(self.in2, GPIO.LOW)
        GPIO.output(self.in3, GPIO.LOW)
        GPIO.output(self.in4, GPIO.LOW)

    def set_speed(self, speed):
        self.pwmA.ChangeDutyCycle(speed)
        self.pwmB.ChangeDutyCycle(speed)

    def cleanup(self):
        self.stop()
        time.sleep(0.2)

        self.pwmA.stop()
        self.pwmB.stop()

        GPIO.cleanup()


# -----------------------------
# Sensors
# -----------------------------
i2c = busio.I2C(board.SCL, board.SDA)

ina = INA219(i2c)
light_sensor = adafruit_bh1750.BH1750(i2c)


def read_temperature():
    base_dir = "/sys/bus/w1/devices/"
    device_folder = glob.glob(base_dir + "28*")

    if not device_folder:
        return 25.0

    device_file = device_folder[0] + "/w1_slave"

    while True:
        with open(device_file, "r") as f:
            lines = f.readlines()

        if lines[0].strip().endswith("YES"):
            break

        time.sleep(0.2)

    temp_string = lines[1].split("t=")[-1]

    return float(temp_string) / 1000.0


# -----------------------------
# Motor Setup
# -----------------------------
motor = SolarCleanerMotor(
    17, 27, 22, 23, 18, 19
)


# -----------------------------
# Dust Detection
# -----------------------------
dust_detected_once = False


try:

    while True:

        time.sleep(SAMPLE_TIME)

        timestamp = datetime.now().strftime(
            "%Y-%m-%d %H:%M:%S"
        )

        # Sensor readings
        voltage = abs(ina.bus_voltage)
        current = abs(ina.current / 1000)
        power = abs(voltage * current)

        intensity = light_sensor.lux
        temperature = read_temperature()

        # Prepare ML input
        sample = pd.DataFrame(
            [[
                voltage,
                current,
                power,
                intensity,
                temperature
            ]],
            columns=[
                "voltage",
                "current",
                "power",
                "intensity",
                "temp"
            ]
        )

        # Predict dust level
        dust = model.predict(sample)[0]

        # -----------------------------
        # Display Sensor Data
        # -----------------------------
        print("\n====================================")
        print("TIMESTAMP:", timestamp)

        print("\nSENSOR SNAPSHOT")
        print("Voltage:", round(voltage, 2), "V")
        print("Current:", round(current, 3), "A")
        print("Power:", round(power, 2), "W")
        print("Light:", round(intensity, 2), "lux")
        print("Temperature:", round(temperature, 2), "°C")

        print("\nDUST LEVEL:", round(dust, 2), "%")


        # -----------------------------
        # Dust Detection Logic
        # -----------------------------
        if dust > DUST_HIGH:

            print("STATUS: DUST DETECTED")

            if not dust_detected_once:

                print("First dust detection stored.")
                dust_detected_once = True

            else:

                print("CONFIRMED DUST")
                print(">>> MOTOR STARTING CLEANING <<<")

                # Forward cleaning movement
                motor.forward(30)
                time.sleep(1.6)

                motor.stop()
                time.sleep(1)

                # Reverse movement
                motor.reverse(40)
                time.sleep(1.5)

                motor.stop()

                print(">>> CLEANING COMPLETED <<<")

                # Reset detection
                dust_detected_once = False

        else:

            print("STATUS: PANEL CLEAN")

            # Reset consecutive detection
            dust_detected_once = False

        print("====================================\n")


finally:

    motor.cleanup()

    print("System stopped safely.")
