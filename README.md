![pi-supply-logo1](https://www.pi-supply.com/wp-content/uploads/2015/11/pi-supply-logo1.png)


# Pi Supply Weather Station


This project uses the Adafruit BMP180 pressure sensor and also the DHT22 temperature/humidity sensor to create a basic weather station using the Raspberry Pi.

## Hardware setup

![weather station](https://www.pi-supply.com/wp-content/uploads/2018/02/fritz_bb.png)


## Software Installation

This project runs on the latest version of Raspbian OS for the Raspberry Pi. Make sure you run `sudo apt-get update` before installing the following libraries. You will need to run the following commands in the terminal window to install the libraries for the weather sensors.

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

### Weather Station install

To download the weather station project files to your Raspberry Pi type the following in the terminal window:

```
git clone https://github.com/ChristopherRush/weather.git

```

To run the flash web server:

```
cd weather
sudo python weather.py
```

## Troubleshooting
