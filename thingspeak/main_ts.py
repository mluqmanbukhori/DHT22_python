from time import time, sleep
import board
import adafruit_dht
from urllib.request import urlopen

dhtDevice = adafruit_dht.DHT22(board.D18)
API = "C9JMA5HJZLTULA2X" # ganti dengan API kalian
URL = "https://api.thingspeak.com/update?api_key={}".format(API)

SensorTimePrev  = 0
SensorInterval  = 2 # 2 detik
ThingSpeakTimePre   = 0
ThingSpeakInterval  = 20 #detik

try:
    while True:
        if time() - SensorTimePrev > SensorInterval:
            SensorTimePrev = time()

            temperature = dhtDevice.temperature
            humidity = dhtDevice.humidity
            print("Temp: {:.1f}*C\tHumidity: {}% ".format(temperature, humidity))

        if time() - ThingSpeakTimePre > ThingSpeakInterval:
            ThingSpeakTimePre = time()

            tsHttp = URL + "&field1={:.2f}&field2={:.2f}".format(temperature, humidity)
            print(tsHttp)

            conn = urlopen(tsHttp)
            print("Response: {}".format(conn.read()))
            conn.close()
            sleep(1)

except KeyboardInterrupt:
    conn.close()
    print("[INFO] quit program...")
