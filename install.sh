#!/usr/bin/env bash

git clone https://github.com/adafruit/Adafruit_Python_BMP.git
cd Adafruit_Python_BMP
python setup.py install

cd ..

git clone https://github.com/adafruit/Adafruit_Python_DHT.git
cd Adafruit_Python_DHT
python setup.py install

cd ..
sudo apt-get install pijuice-gui -y

curl https://get.pimoroni.com/bme680 | bash

git clone https://github.com/ChristopherRush/weather.git
