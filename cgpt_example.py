import time
import board
import busio
import adafruit_bme280

# Initialize the I2C bus.
i2c = busio.I2C(board.SCL, board.SDA)

# Initialize the BME280 sensor.
bme280 = adafruit_bme280.Adafruit_BME280_I2C(i2c)

# Change the default sampling rate for faster measurements.
bme280.mode = adafruit_bme280.MODE_NORMAL
bme280.standby_period = adafruit_bme280.STANDBY_TC_500
bme280.filter_size = adafruit_bme280.FILTER_SIZE_4
bme280.overscan_pressure = adafruit_bme280.OVERSCAN_X16
bme280.overscan_humidity = adafruit_bme280.OVERSCAN_X1
bme280.overscan_temperature = adafruit_bme280.OVERSCAN_X2

# Read the BME280 sensor data and print it to the console.
while True:
    temperature = bme280.temperature
    pressure = bme280.pressure
    humidity = bme280.humidity
    print("Temperature: %0.1f C" % temperature)
    print("Pressure: %0.1f hPa" % pressure)
    print("Humidity: %0.1f %%" % humidity)
    time.sleep(1)
