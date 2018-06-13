![pi-supply-logo1](https://www.pi-supply.com/wp-content/uploads/2015/11/pi-supply-logo1.png)


# Pi Supply Weather Station

![weather station gui](https://www.pi-supply.com/wp-content/uploads/2018/02/Screen-Shot-2018-02-14-at-17.10.44.png)

This project uses the Adafruit BMP180, DHT22 or BME680 module to create a basic weather station using the Raspberry Pi and PiJuice HAT. The front end of the weather station uses a web server provided by Flask and programmed in Python. The interface is done using a javascript plugin called [JustGauge](http://justgage.com), which is fully customisable.

## Hardware setup

For this weather station project you will require the following parts:

- Raspberry Pi computer
- Wi-Fi or Ethernet network ability
- 8GB microSD card with Raspbian OS
- DHT22 Temperature & Humidity sensor
  - 4.7k resistor
- Adafruit BMP180 Pressure sensor (discontinued)
- PiJuice
- PiJuice Solar Panel

All sensors can be Plug 'n' Play as the program is running (Not recommended).

![weather station](https://www.pi-supply.com/wp-content/uploads/2018/02/fritz_bb.png)


## Software Installation

This project runs on the latest version of [Raspbian OS](https://www.raspberrypi.org/downloads/) for the Raspberry Pi. Make sure you run `sudo apt-get update` before installing the following libraries. You will need to run the following commands in the terminal window to install the libraries for the weather sensors.

### Auto Installation

Just run the following line in the terminal to automatically install all the libraries and project files to the Raspberry Pi.

Raspbian OS Install Script:
```bash
# Run this line and the weather station will be setup and installed
curl -sSL https://raw.githubusercontent.com/ChristopherRush/weather/master/install.sh | sudo bash
```
Raspbian Lite Install script:
```bash
curl -sSL https://raw.githubusercontent.com/ChristopherRush/weather/master/install_lite.sh | sudo bash
```


### Adafruit BMP180 Library

```bash
git clone https://github.com/adafruit/Adafruit_Python_BMP.git
cd Adafruit_Python_BMP
sudo python setup.py install
```

### Adafruit DHT22 Library

```bash
git clone https://github.com/adafruit/Adafruit_Python_DHT.git
cd Adafruit_Python_DHT
sudo python setup.py install
```

### Pimoroni BME680 Library

Library install for Python 3:
```bash
sudo pip3 install bme680
```
Library Install for Python 2:
```bash
sudo pip2 install bme680
```

### Flask

[Flask](http://flask.pocoo.org) is a lightweight web framework that runs using Python programming language. We will be using Flask to create a web server that can host a web page locally on the Raspberry Pi and then can be accessible over the network from any other device on that same network.

By default Flask is already installed on the latest version of [Raspbian OS](https://www.raspberrypi.org/downloads/), however if the package is not there then you can type the following in the terminal window to install Flask:
```bash
sudo apt-get install python3-flask
```

Flask had a specific file structure that needs to be met in order for all the files to be located for the web server. Here is the file structure in its simplest terms:

- app.py
- config.py
- requirements.txt
  - static/
    - css/
      - style.css
    - javascript/
  - templates
    - index.html

For further information visit http://exploreflask.com/en/latest/organizing.html

running 'debug=True' causes the server to run with the reloader, therfore the app is restarted in a new process by the reloader process.

### Weather Station Project install

To download the weather station project files to your Raspberry Pi type the following in the terminal window:

```bash
git clone https://github.com/ChristopherRush/weather.git

```

To run the Flask web server:

```bash
cd weather
sudo python weather.py
```

To view the webpage you will need to go to the Raspberry Pi's IP address on your local network such as http://192.168.0.23 yours may differ. You can find your IP address from the terminal window on the Raspberry Pi by typing in the following command:

```bash
#Wi-Fi connection
ifconfig wlan0

#Ethernet
ifconfig eth0
```

![ipaddress](https://www.pi-supply.com/wp-content/uploads/2018/02/Screen-Shot-2018-02-14-at-11.11.06.png)

## Changing web page refresh rate

By default this project has the ability to refresh the web page every 5 seconds to get the latest update value from the sensors. You can change the refresh rate in the index.html page by changing the content value in the following line:

```html
<meta http-equiv="refresh" content="5">
```
## JustGauge Javascript Plugin

[Justgauge](http://justgage.com/) is a handy JavaScript plugin for generating and animating nice & clean gauges. It is based on Raphaël library for vector drawing, so it’s completely resolution independent and self-adjusting. This plugin is a nice clean way to display the values from our weather station in its simplest form.

The JavaScript files have already been added to the project files in static/javascript/ . To add JavaScript to the index.html file you must do so in the following format not the regular html format:

```html
<script src="{{url_for('static', filename='javascript/justgage.js')}}"></script>
<script src="{{url_for('static', filename='javascript/raphael-2.1.4.min.js')}}"></script>
```
To add a new gauge you will need to create a new div with id and class.

```html
<div id="gauge" class="gauge">
```

Add the following to the css file to style each gauge element. The id element will change the individual gauge block and as such will require a unique id where as the class will style all gauge elements the same. Note: currently the id is not used in this project.

```css
.gauge {
     width: 300px;
     height: 300px;
     display: inline-block;
     margin: 5px;
 }
 ```
Finally add these parameters changing the value to the variable that gets passed through from the Python script.

```html
<script>
var gauge = new JustGage({
  id: "gauge",
  value: {{temp}},
  symbol: '\u2103', #can be added as plain text or hex code
  levelColors: ['#1B94FF', '#FDDC00', '#FF9E00', '#FF3F00'],
  min: 0, #minimum range value
  decimals: 1, #decimal places
  max: 50, #maximum range value
  title: "Temperature" #text to be displayed above the gauge
});
</script>
```


JustGuage plugin is licensed under the MIT license

When setting the Wakeup alarm for a repeated wakeup, after the initial reboot the Wakeup enabled capability is disabled due to the Raspbian RTC clock initialisation resetting the bit in the PiJuice firmware. To overcome this you will need to run a script to re-enable the wakeup-enable capability. The script is located in PiJuice > Software > Test > wakeup_enable.py

```bash
import pijuice
pj = pijuice.PiJuice(1, 0x14)

pj.rtcAlarm.SetWakeupEnabled(True)
```

To run the script every time the Raspberry Pi reboots you will need to add it to the cron table. From the command line run `crontab -e` to edit the cron table.

The first time you run `crontab` you will be prompted to select an editor; if you are not sure which one to use, choose `nano` by pressing Enter.

Add the following to the cron table:

```bash
@reboot /usr/bin/python /home/pi/PiJuice/Software/Test/wakeup_enable.py
```
