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
import Adafruit_BMP.BMP085 as BMP085 #Works for both the BMP085 and BMP180 sensors
import Adafruit_DHT # this library works for DHT11 DHT22 and AM2302 sensors
import bme680 # import bme680 library
import time

sensor = bme680.BME680() #create bme680 object

sensor.set_humidity_oversample(bme680.OS_2X)
sensor.set_pressure_oversample(bme680.OS_4X)
sensor.set_temperature_oversample(bme680.OS_8X)
sensor.set_filter(bme680.FILTER_SIZE_3)
sensor.set_gas_status(bme680.ENABLE_GAS_MEAS)

sensor.set_gas_heater_temperature(320)
sensor.set_gas_heater_duration(150)
sensor.select_gas_heater_profile(0)

start_time = time.time()
curr_time = time.time()
burn_in_time = 60

run = 0

burn_in_data = []

bus = smbus.SMBus(1)

bmp_device = 119 #i2c address in decimal

from flask import Flask, render_template

print run
    # Collect gas resistance burn-in values, then use the average
    # of the last 50 values to set the upper limit for calculating
    # gas_baseline.
if run == 0:
    print("Collecting gas resistance burn-in data for 5 mins\n")
    while curr_time - start_time < burn_in_time:
        curr_time = time.time()
        if sensor.get_sensor_data() and sensor.data.heat_stable:
            gas = sensor.data.gas_resistance
            burn_in_data.append(gas)
            print("Gas: {0} Ohms".format(gas))
            time.sleep(1)

            gas_baseline = sum(burn_in_data[-50:]) / 50.0

    # Set the humidity baseline to 40%, an optimal indoor humidity.
    hum_baseline = 40.0

    # This sets the balance between humidity and gas reading in the
    # calculation of air_quality_score (25:75, humidity:gas)
    hum_weighting = 0.25

    print("Gas baseline: {0} Ohms, humidity baseline: {1:.2f} %RH\n".format(gas_baseline, hum_baseline))


run = 1
print run

try: #check to see if the device is connected

    bus.read_byte(bmp_device) #if i2c device is connected create device object '''
    bmp_sensor = BMP085.BMP085()
    print "here"
except: #do nothing if sensor is not connected
    print "thrid"
    pass


dh22_sensor = Adafruit_DHT.DHT22


pin = 4 #DHT22 data pin on the raspberry pi

#temp = sensor.read_temperature()
#pressure = sensor.read_pressure()
#altitude = sensor.read_altitude()
while True:
    sensor.get_sensor_data()
    print "data"


app = Flask(__name__)

@app.route('/') # this tells the program what url triggers the function when a request is made
def index():
    try:

            gas = sensor.data.gas_resistance
            gas_offset = gas_baseline - gas

            hum = sensor.data.humidity
            hum_offset = hum - hum_baseline

            # Calculate hum_score as the distance from the hum_baseline.
            if hum_offset > 0:
                hum_score = '{:.2f}'.format(100 - hum_baseline - hum_offset) / (100 - hum_baseline) * (hum_weighting * 100)

            else:
                hum_score = (hum_baseline + hum_offset) / hum_baseline * (hum_weighting * 100)

            # Calculate gas_score as the distance from the gas_baseline.
            if gas_offset > 0:
                gas_score = '{:.2f}'.format(gas / gas_baseline) * (100 - (hum_weighting * 100))

            else:
                gas_score = 100 - (hum_weighting * 100)

            # Calculate air_quality_score.
            air_quality_score = '{:.2f}'.format(hum_score + gas_score)

            temp_score = sensor.data.temperature
            press_score = sensor.data.pressure
    except:
            hum_score = 0
            gas_score = 0
            air_quality_score = 0
            temp_score = 0
            press_score = 0
            pass


    try: #check to see if the DHT sensor is connected
        humidity, temperature = Adafruit_DHT.read(dh22_sensor, pin) #get the values from the sensor
        humidity ='{:.2f}'.format(humidity) #convert value to two decimal places
        temperature ='{:.1f}'.format(temperature) #convert value to one decimal place

    except: # If the sensor is not connected send null values
        humidity = 0
        temperature = 0
        pass



    try:
        #if bus.read_byte(0x77): #check to see if the BMP sensor is attached decimal 119 hex 0x77 address

        temp = bmp_sensor.read_temperature() #read the temperature from the BMP sensor in celcius
        pressure = bmp_sensor.read_pressure() #read the pressure from the BMP sensor
        altitude = bmp_sensor.read_altitude() #read teh altitude value from the BMP sensor in meters
        altitude = '{:.2f}'.format(altitude) #convert the altitude value to two decimal places

    except: #if the device is not connected send null values
        temp = 0
        pressure = 0
        altitude = 0
        pass


    #variables to pass through to the web page
    templateData = {
            'temp' : temp,
            'pressure' : pressure,
            'altitude' : altitude,
            'humidity' : humidity,
            'temperature' : temperature,
            'hum_score' : hum_score,
            'temp_score' : temp_score,
            'air_quality_score' : air_quality_score,
            'press_score' : press_score

    }
    return render_template('index.html', **templateData) #when a html request has been made return these values

if __name__ == '__main__':
        app.run(debug=True, host='0.0.0.0')
        #app.config['SERVER_NAME'] = 'myapp.local'
        #app.run(host=app.config['SERVER_NAME'], port=5000, debug=True)
