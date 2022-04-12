import time
import board
import adafruit_dht

dhtDevice = adafruit_dht.DHT22(board.D18)
 
while True:
    temperature = dhtDevice.temperature
    humidity = dhtDevice.humidity
    print("Temp: {:.1f} C    Humidity: {}% ".format(temperature, humidity))
    time.sleep(1) 
