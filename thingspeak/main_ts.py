from time import time, sleep
import board
import adafruit_dht
from urllib.request import urlopen

dhtDevice = adafruit_dht.DHT22(board.D18)
API_KEY = "H7O3MY7QV2RRMZ29"
URL = "https://api.thingspeak.com/update?api_key={}".format(API_KEY)

interval = 20 # 20 detik
SensorTime = 0
TsTime = 0

try:
    while True:
        if time() - SensorTime > interval:
            SensorTime = time()
            temperature = dhtDevice.temperature
            humidity = dhtDevice.humidity
            print("Temp: {:.1f}*C\tHumidity: {}% ".format(temperature, humidity))
        
        if time() - TsTime > interval:
            TsTime = time()
            
            tsHttp = URL + "&field1={:.2f}&field2={:.2f}".format(temperature,humidity)
            print(tsHttp)
            conn = urlopen(tsHttp)
            print("Response: {}".format(conn.read()))
            print("tunggu time release: {} detik".format(interval))
            conn.close()
        
except KeyboardInterrupt:
    conn.close()
    print("[INFO] quit program...")
