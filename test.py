import Adafruit_BME280
import time

# Create a BME280 instance using the I2C bus.
sensor = Adafruit_BME280.BME280()

# Read and print temperature, humidity, and pressure values.
while True:
    temperature = sensor.read_temperature()
    humidity = sensor.read_humidity()
    pressure = sensor.read_pressure()
    print('Temperature: {:.1f} C'.format(temperature))
    print('Humidity: {:.1f} %'.format(humidity))
    print('Pressure: {:.1f} hPa'.format(pressure / 100.0))
    time.sleep(1)
