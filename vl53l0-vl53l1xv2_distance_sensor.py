import time
import board
import busio
# For VL53L0X, use: import adafruit_vl53l0x
import adafruit_vl53l1x  # Change this for your specific sensor

# Initialize I2C bus and sensor
i2c = busio.I2C(board.SCL, board.SDA)
vl53 = adafruit_vl53l1x.VL53L1X(i2c)

# For VL53L1X specifically, start ranging
vl53.start_ranging()

print("Measuring distance... Press Ctrl+C to stop.")

try:
    while True:
        if vl53.data_ready:
            print(f"Distance: {vl53.distance} cm")
            vl53.clear_interrupt()
        time.sleep(0.1)
except KeyboardInterrupt:
    vl53.stop_ranging()
