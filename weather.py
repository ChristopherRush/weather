import Adafruit_BMP.BMP085 as BMP085
import Adafruit_DHT

from flask import Flask, render_template

sensor = BMP085.BMP085()
dh22_sensor = Adafruit_DHT.DHT22

pin = 4

#temp = sensor.read_temperature()
#pressure = sensor.read_pressure()
#altitude = sensor.read_altitude()

app = Flask(__name__)

@app.route('/')
def index():
        humidity, temperature = Adafruit_DHT.read_retry(dh22_sensor, pin)
        humidity ='{:.2f}'.format(humidity)
        temperature ='{:.1f}'.format(temperature)
        temp = sensor.read_temperature()
        pressure = sensor.read_pressure()
        altitude = sensor.read_altitude()
        altitude = '{:.2f}'.format(altitude)
        templateData = {
                'temp' : temp,
                'pressure' : pressure,
                'altitude' : altitude,
                'humidity' : humidity,
                'temperature' : temperature
        }
        return render_template('index.html', **templateData)

if __name__ == '__main__':
        app.run(debug=True, host='0.0.0.0')
