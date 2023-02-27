import psutil
import time
import sys
from ISStreamer.Streamer import Streamer

BUCKET_NAME = 'RoomTemp'
BUCKET_KEY = 'qs2258'
ACCESS_KEY = 'ist_EZQ88UaSgCZxVhqbIYDpH835k8gMR3oc'
PROCESS_NAME = '/home/qs2258/bme280project1/tempsensor.py'
MINUTES_DELAY = 1

def main():
    found_ntpd = False
    cnt = 0

    while found_ntpd == False:
        for proc in psutil.process_iter():
            if proc.name() == 'ntpd':
                found_ntpd = True
        cnt += 1
        if cnt == 60:
            found_ntpd=True
        time.sleep(1)
    
    time.sleep(60*MINUTES_DELAY)
    streamer = Streamer(bucket_name=BUCKET_NAME, bucket_key=BUCKET_KEY, access_key=ACCESS_KEY)
    streamer.log(PROCESS_NAME, "Exited")
    streamer.flush()

if __name__ == "__main__":
    main()