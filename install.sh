#!/usr/bin/env bash

# Install BMP Adafruit library

git clone https://github.com/adafruit/Adafruit_Python_BMP.git
cd Adafruit_Python_BMP
python setup.py install

# Install DHT22 Adafruit library

git clone https://github.com/adafruit/Adafruit_Python_DHT.git
cd Adafruit_Python_BMP
python setup.py install

git clone https://github.com/ChristopherRush/weather.git
