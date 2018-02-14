![pi-supply-logo1](https://www.pi-supply.com/wp-content/uploads/2015/11/pi-supply-logo1.png)


# Pi Supply Weather Station


This project uses the Adafruit BMP180 pressure sensor and also the DHT22 temperature/humidity sensor to create a basic weather station using the Raspberry Pi. The front end of the weather station uses a web server provided by Flask and programmed in Python.

## Hardware setup

![weather station](https://www.pi-supply.com/wp-content/uploads/2018/02/fritz_bb.png)


## Software Installation

This project runs on the latest version of Raspbian OS for the Raspberry Pi. Make sure you run `sudo apt-get update` before installing the following libraries. You will need to run the following commands in the terminal window to install the libraries for the weather sensors.

### Auto Installation

Just run the following line in the terminal to automatically install all the libraries and project files to the Raspberyr Pi.

```bash
# Run this line and the weather station will be setup and installed
curl -sSL https://raw.githubusercontent.com/ChristopherRush/weather/master/install.sh | sudo bash
```

### Adafruit BMP180

```
git clone https://github.com/adafruit/Adafruit_Python_BMP.git
cd Adafruit_Python_BMP
sudo python setup.py install
```

### Adafruit DHT22

```
git clone https://github.com/adafruit/Adafruit_Python_DHT.git
cd Adafruit_Python_BMP
sudo python setup.py install
```

### Flask

Flask is a lightweight web framework that runs using Python programming language. We will be using Flask to create a web server that can host a web page locally on the Raspberry Pi and then can be accessible over the network from any other device on that same network.

By default Flask is already installed on the latest version of Raspbian OS, however if the package is not there then you can type the following in the terminal window to install Flask:
```
sudo apt-get install python3-flask
```

Flask had a specific file structure that needs to be met in order for all the files to be located for the web server. Here is the file structure in its simplest terms:

- app.py
- config.py
- requirements.txt
  - static/
    - css/
      - style.css
  - templates
    - index.html

For further information visit http://exploreflask.com/en/latest/organizing.html



### Weather Station Project install

To download the weather station project files to your Raspberry Pi type the following in the terminal window:

```
git clone https://github.com/ChristopherRush/weather.git

```

To run the Flask web server:

```
cd weather
sudo python weather.py
```

To view the webpage you will need to go to the Raspberry Pi's IP address on your local network such as http://192.168.0.23 yours may differ. You can find your IP address from the terminal window on the Raspberry Pi by typing in the following command:

```
#Wi-Fi connection
ifconfig wlan0

#Ethernet
ifconfig eth0
```

![ipaddress](https://www.pi-supply.com/wp-content/uploads/2018/02/Screen-Shot-2018-02-14-at-11.11.06.png)


## Troubleshooting
