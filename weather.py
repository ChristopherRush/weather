import Adafruit_BMP.BMP085 as BMP085 #Works for both the BMP085 and BMP180 sensors
import Adafruit_DHT # this library works for DHT11 DHT22 and AM2302 sensors

from flask import Flask, render_template

bmp_sensor = BMP085.BMP085()
dh22_sensor = Adafruit_DHT.DHT22

pin = 4 #DHT22 data pin on the raspberry pi

#temp = sensor.read_temperature()
#pressure = sensor.read_pressure()
#altitude = sensor.read_altitude()

app = Flask(__name__)

@app.route('/')
def index():
        humidity, temperature = Adafruit_DHT.read_retry(dh22_sensor, pin) #get the values from the sensor
        humidity ='{:.2f}'.format(humidity) #convert value to two decimal places
        temperature ='{:.1f}'.format(temperature) #convert value to one decimal place

        temp = bmp_sensor.read_temperature() #read the temperature from the BMP sensor in celcius
        pressure = bmp_sensor.read_pressure() #read the pressure from the BMP sensor
        altitude = bmp_sensor.read_altitude() #read teh altitude value from the BMP sensor in meters
        altitude = '{:.2f}'.format(altitude) #convert the altitude value to two decimal places

        #variables to pass through to the web page
        templateData = {
                'temp' : temp,
                'pressure' : pressure,
                'altitude' : altitude,
                'humidity' : humidity,
                'temperature' : temperature
        }
        return render_template('index.html', **templateData) #when a html request has been made return these values

if __name__ == '__main__':
        app.run(debug=True, host='0.0.0.0')
