#    Copyright (C) 2018  Chris Rush
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <https://www.gnu.org/licenses/>.
import smbus
import Adafruit_DHT # this library works for DHT11 DHT22 and AM2302 sensors
import time
import spidev

from flask import Flask, render_template

# Open SPI bus
spi = spidev.SpiDev()
spi.open(0,0)
spi.max_speed_hz=1000000

dh22_sensor = Adafruit_DHT.DHT22

pin = 4 #DHT22 data pin on the raspberry pi

# Define sensor channels
light_channel = 0

def ReadChannel(channel):
  adc = spi.xfer2([1,(8+channel)<<4,0])
  data = ((adc[1]&3) << 8) + adc[2]
  return data



app = Flask(__name__)

@app.route('/') # this tells the program what url triggers the function when a request is made
def index():

    try: #check to see if the DHT sensor is connected
        humidity, temperature = Adafruit_DHT.read(dh22_sensor, pin) #get the values from the sensor
        humidity ='{:.2f}'.format(humidity) #convert value to two decimal places
        temperature ='{:.1f}'.format(temperature) #convert value to one decimal place

    except: # If the sensor is not connected send null values
        humidity = 0
        temperature = 0
        pass

    try:
          # Read the light sensor data
          light_level = ReadChannel(light_channel)



    #variables to pass through to the web page
    templateData = {
            'humidity' : humidity,
            'temperature' : temperature,
            'light' : light_level
    }
    return render_template('index.html', **templateData) #when a html request has been made return these values


if __name__ == '__main__':
        app.run(debug=False, host='0.0.0.0', port=5000)


        #app.config['SERVER_NAME'] = 'myapp.local'
        #app.run(host=app.config['SERVER_NAME'], port=5000, debug=True)
