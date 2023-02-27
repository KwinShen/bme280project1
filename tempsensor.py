import bme280
from ISStreamer.Streamer import Streamer
import time
import smbus2

port = 1
address = 0x77
bus = smbus2.SMBus(port)

bme280.load_calibration_param(bus, address)

streamer = Streamer(bucket_name=BUCKET_NAME, bucket_key=BUCKET_KEY, access_key=ACCESS_KEY)

while True:
    bme280_data = bme280.sample(bus, address)
    pressure = bme280_data.pressure
    humidity = bme280_data.humidity
    temp_c = bme280_data.temperature
    if METRIC_UNITS:
        streamer.log(SENSOR_LOCATION_NAME + " Temperature(C)", temp_c)
    else:
        temp_f = format(temp_c * 9.0 / 5.0 +32.0, ".2f")
        streamer.log(SENSOR_LOCATION_NAME + " Temperature(F)", temp_f)
    humidity = format(humidity, ".2f")
    streamer.log(SENSOR_LOCATION_NAME + " Humidity(%)", humidity)
    streamer.flush()
    time.sleep(60*MINUTES_BETWEEN_READS)