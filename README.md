# Baca sensor DHT22 di Raspberry Pi 4 model B

## buat virtualenv
<pre>
pi@raspberrypi:~ $ python3 -m venv <nama-virtual>
</pre>

## jalankan virtualenv yg telah dibuat
<pre>
pi@raspberrypi:~ $ source <nama-virtual>/bin/activate
</pre>
  
## install library adafruit DHT
<pre>
(oscar) pi@raspberrypi:~ $ pip3 install adafruit-circuitpython-dht
</pre>

## cek library Adafruit
<pre>
(oscar) pi@raspberrypi:~ $ pip list
Package                    Version
-------------------------- -------
Adafruit-Blinka            7.2.0  
adafruit-circuitpython-dht 3.7.2  
Adafruit-PlatformDetect    3.22.1 
Adafruit-PureIO            1.1.9  
pip                        18.1   
pkg-resources              0.0.0  
pyftdi                     0.54.0 
pyserial                   3.5    
pyusb                      1.2.1  
rpi-ws281x                 4.3.4  
RPi.GPIO                   0.7.1  
setuptools                 40.8.0 
sysv-ipc                   1.1.0  
</pre>

## jalankan `main.py`
<pre>
(oscar) pi@raspberrypi:~ $ python main.py 
</pre>

## jika error seperti ini
<pre>
  Traceback (most recent call last):
  File "main.py", line 8, in <module>
    dhtDevice = adafruit_dht.DHT22(board.D4)
  File "/home/pi/oscar/lib/python3.7/site-packages/adafruit_dht.py", line 305, in __init__
    super().__init__(False, pin, 1000, use_pulseio)
  File "/home/pi/oscar/lib/python3.7/site-packages/adafruit_dht.py", line 86, in __init__
    self.pulse_in = PulseIn(self._pin, maxlen=self._max_pulses, idle_state=True)
  File "/home/pi/oscar/lib/python3.7/site-packages/adafruit_blinka/microcontroller/bcm283x/pulseio/PulseIn.py", line 77, in __init__
    self._process = subprocess.Popen(cmd)  # pylint: disable=consider-using-with
  File "/usr/lib/python3.7/subprocess.py", line 775, in __init__
    restore_signals, start_new_session)
  File "/usr/lib/python3.7/subprocess.py", line 1522, in _execute_child
    raise child_exception_type(errno_num, err_msg, err_filename)
PermissionError: [Errno 13] Permission denied: '/home/pi/oscar/lib/python3.7/site-packages/adafruit_blinka/microcontroller/bcm283x/pulseio/libgpiod_pulsein'
</pre>

## atur permission
<pre>
(oscar) pi@raspberrypi:~ $ sudo chmod 4775 /home/pi/oscar/lib/python3.7/site-packages/adafruit_blinka/microcontroller/bcm283x/pulseio/libgpiod_pulsein
</pre>

## jalankan `main.py` kembali
<pre>
(oscar) pi@raspberrypi:~ $ python main.py 
Temp: 84.4 F / 29.1 C    Humidity: 69.9% 
Temp: 84.2 F / 29.0 C    Humidity: 71.3% 
Temp: 84.2 F / 29.0 C    Humidity: 71.0% 
Temp: 84.4 F / 29.1 C    Humidity: 71.0% 
Temp: 84.4 F / 29.1 C    Humidity: 73.7% 
Temp: 84.4 F / 29.1 C    Humidity: 76.2% 
Temp: 84.6 F / 29.2 C    Humidity: 78.0% 
</pre>
