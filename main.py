import time
import board
import adafruit_dht

dhtDevice = adafruit_dht.DHT22(board.D18)

try:
    while True:
        temperature = dhtDevice.temperature
        humidity = dhtDevice.humidity
        print("Temp: {:.1f}*C\tHumidity: {}% ".format(temperature, humidity))
        time.sleep(2)
        
except KeyboardInterrupt:
    print("[INFO] quit program...")
