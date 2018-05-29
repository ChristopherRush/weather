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

## PiJuice CLI

For those users who would rather run their Raspberry Pi using a Lite version of Raspbian or has remote access to the Pi via SSH, we have also designed a handy little command line interface tool, which ultimately replicates the Graphical Interface for PiJuice software.

To launch the PiJuice CLI simply open up the Terminal or from the command line type in the following command:

`pijuice_cli.py`

![pijuice cli](https://drive.google.com/uc?id=1bSHhI6uIXOhCBUWUfkAwLAHcVTAm7UbD)

The PiJuice command line interface is an extension of the PiJuice HAT Configuration GUI with the exception that System Task, System Events and User Scripts cannot be configurable from the command line interface. To configure these options you will need to directly modify the JSON file as shown in the next section.

To scroll the menu simply use your arrow keys on your keyboard and press enter to select options or navigate through the menu system.

### Status
This menu shows the current status of the PiJuice including battery levels and charging input method.

![pijuice cli status](https://drive.google.com/uc?id=1vhS2cULuMJNl91DSFq4sGjPAx78uWFKa)

**Note: It is recommended to use a power supply with a current rating of 2.5A such as the official Raspberry Pi power supply.**

**Battery** - This section displays the current battery level as a percentage from 0-100% as well as the battery voltage. Next to this is the current charging status of the battery; NOT_PRESENT battery is not installed, CHARGING_FROM_IN battery is charging from the PiJuice micro USB connector, CHARGING_FROM_5V_IO battery is charging from the GPIO pins via the micro USB connector on the Raspberry Pi, NORMAL battery is not charging but is operating as normal.

**GPIO power input** - This section displays the power state of the GPIO pins as the PiJuice can provide power to the Raspberry Pi through the GPIO pins as well as receive power from the Raspberry Pi if powered through the Raspberry Pi’s micro USB connector. This section display the GPIO voltage(V) and current (A) that the battery either provides to the Pi or receives from the Pi as well as the input status; NOT_PRESENT no power supply is connected to the Raspberry Pi, BAD power supply is connected to the Raspberry Pi but is not providing enough power to the Raspberry Pi and PiJuice, WEAK power is connected to the Raspberry Pi but not enough to power the Raspberry Pi and charge the PiJuice, PRESENT power supply is connected to the Raspberry Pi and is stable.

**USB Micro power input** - This section displays the status of the PiJuice micro USB power supply. NOT_PRESENT no power supply is connected to the PiJuice, BAD power supply is connected but cannot charge the PiJuice or power the Raspberry Pi, WEAK power supply is connected but not providing enough power, PRESENT power supply is connected and is stable.

**Fault** - This section displays any faults with the power system of the PiJuice.

**System switch** - This section is used to configure the VSYS pin on header J3, which is on the underside of the PiJuice board and on header P3. This pin can be used to provide power to external devices such as the PiBot. You can configure the pin to limit its current output; Off VSYS is switched off, 500mA provides a maximum of 500mA output current, 2100mA provides a maximum of 2100mA output current. To change the System Switch state hit enter on Change Power Switch and then select one of the options in the menu.

To get new data from the PiJuice you can select Refresh to update the values.

### General

In the General menu it allows you to configure a lot of the hardware settings for the PiJuice HAT. The only difference with this menu and the GUI is that you cannot change the I2C address for the PiJuice HAT and the built-in RTC.

![pijuice cli general](https://drive.google.com/open?id=10VznlXOPuF5C05hjggRYHniWWyfEiqyM)

**GPIO Input Enabled** enables/disables powering the PiJuice HAT from 5V GPIO Input (Raspberry Pi). Enabled by default.

**EEPROM write unprotect** allows you to reconfigure the EEPROM on the PiJuice HAT. Selecting this option makes it available for you to write EEPROM data.

**Charging enabled** is by default checked and allows the charging of the battery. If you wish to disable this option then you can deselect this option.

**No battery turn on** If enabled, pijuice will automatically power on 5V rail and trigger wake-up as soon as power appears at USB Micro Input and there is no battery. Disabled by default.

The **Run pin** configuration allows you to set whether the pogo pin is installed on the PiJuice. The pogo pin is required for for use with the wakeup function on the Raspberry Pi.

**Inputs precedence** selects which power input will have precedence for charging and supplying VSYS output when both are present, HAT USB Micro Input, GPIO 5V Input (Raspberry Pi). 5V_GPIO is selected by default.

**USB Micro current** limit selects maximum current that the PiJuice HAT can take from USB Micro connected power source. 2.5A selected by default.

**USB Micro IN DPM** Selects minimum voltage at USB Micro power input for Dynamic Power Management Loop. 4.2V set by default.

**Power regulator mode** selects the type of power regulator from POWER_SOURCE_DETECTION, LDO and DCDC. POWER_SOURCE_DETECTION is selected by default.

Don’t forget that when you make changes to any of the hardware settings you must Apply the settings from the menu, otherwise they will not be saved.

### Buttons
There are a total of three, user configurable buttons, that you can program to trigger certain events.

The default button functions are:

- SW1/J5 is power button by default:
  - Single press to power on (release in less than 800 ms)
  - Long press of at least 10 seconds to halt
  - Long press of at least 20 seconds to cut power

- SW2 is user button by default, configured to trigger user scripts:
  - Single press in less than 400ms to invoke “USER_FUNC1”
  - Double press within 600ms to invoke “USER_FUNC2”

- SW3 is user button by default, configured to trigger user scripts:
  - Press will invoke “USER_FUNC3”
  - Release will invoke “USER_FUNC4”

There are a number of preset behaviours for the buttons - startup/shutdown etc and this menu also ties in to the "User Scripts" menu shown, meaning you can actually trigger your own custom scripts and events based on the press of one of these buttons very easily.
The buttons also have some special functions, which help when debugging the PiJuice and to reset the hardware when things don’t go your way:

- Dual long press of SW1 and SW2 for 20 seconds will reset PiJuice HAT configuration to default. This applies to the MCU configuration only.
- Holding pressed SW3 while powering up PiJuice will initiate the bootloader. This is used only in cases when ordinary initiation through I2C does not work because of damaged firmware.

You can even trigger different events for a press, release, single press, double press and two lengths of long press - you can even configure the length of time these long presses would take before triggering the event. As you can see the first button is already configured for system power functionality and we would highly recommend that at least one of the buttons is configured to these settings or you may have issues turning your PiJuice on and off.

![pijuice buttons](https://drive.google.com/open?id=1_zkCQWLH857GTilGG4xHD8KJzcRxyBcJ)

![pijuice cli buttons menu](https://drive.google.com/open?id=1Th3XOR0Pw66iDhc35TnfREcH5rJWRgra)

In order to program one of the buttons, first select which button you would like to use to trigger and event. In the next menu you can program the type of button press you would like to use from the following settings:

![pijuice cli buttons options](https://drive.google.com/open?id=1bHnXgmZCR4CQWyilgxCJwembWNUVcan9)

**PRESS** - Triggered immediately after button is pressed
**RELEASE** - Triggered immediately after button is released
**SINGLE PRESS** - Triggered if button is released in time less than configurable timeout after button press.
**DOUBLE PRESS** - Triggered if button is double pressed in time less than configurable timeout.
**LONG PRESS 1** - Triggered if button is hold pressed hold for configurable time period 1.
**LONG PRESS 2** - Triggered if button is hold pressed hold for configurable time period 2.

In the next menu option if you select one of the above you can change the type of user function that you wish to trigger when the button is pressed.

![pijuice cli buttons functions](https://drive.google.com/open?id=1oYC9A2ibxPGMb9oyvusf_mPTXRWNWYgE)

**NO_FUNC** - Does nothing
**HARD_FUNC_POWER_ON** - Switches on the Raspberry Pi by applying power to the GPIO pins
**HARD_FUNC_POWER_OFF** - Switches off power to the Raspberry Pi by cutting the power to the GPIO pins (Not recommend)
**HARD_FUNC_RESET** - Resets power to the Raspberry Pi forcing a reboot
**SYS_FUNC_HALT** - Halts the system
**SYS_FUNC_HALT_POW_OFF** - Halts the system then power off the 5V power regulator and system switch is set to off
**SYS_FUNC_SYS_OFF_HALT** - System is halted and system switch is set to off and system halts
**SYS_FUNC_REBOOT** - performs a reboot
**USER_EVENT** - Runs a custom script that it not processed by system task
**USER_FUNC1** - Runs a custom user script

**NOTE: SYS_FUNC_HALT_POW_OFF still provides power to the Raspberry Pi for a further 60 seconds after shutdown**

To set the Parameter of the button press simply enter its value in milliseconds to the Parameter field.

### LEDs

Just like the buttons, the LEDS are also configurable on the PiJuice and there are two of them in total. The LEDs are surface mount RGB LEDs and can be configured in a number of different colours aside from the preset primary colours in use.

![pijuice cli leds](https://drive.google.com/open?id=1kzXigQUiuRV_sDB8Ne_N4hdH_Rqqi9YR)

![pijuice cli leds](https://drive.google.com/open?id=1NpqfDmqwxgyX5oPYXBr8isC6DpUDEJBd)

Each LED can be assigned to a predefined function or configured for user software control as User LED. There are two user functions that are available:

**CHARGE STATUS** - LED is configured to signal current charge level of the battery. For level <= 15% red with configurable brightness. For level > 15% and level <=50% mix of red and green with configurable brightness. For level > 50% green with configurable brightness. When battery is charging blinking blue with configurable brightness is added to current charge level color. For full buttery state blue component is steady on. Current D1 LED values:

R: 60/
G: 60/
B: 100

**USER LED** - When LED is configured as User LED it can be directly controlled with User software via command interface. Initial PiJuice power, on User LED state is defined with R, G, and B brightness level parameters.

Example:

To change the values of LED D2, select D2 from the menu. Then select the USER_LED function and then add your own values to RGB.

![pijuice cli rgb](https://drive.google.com/open?id=1QUsGoGr6mXpqiuwgvCXAVINCB2PMaSoc)

Once finished making the changes go Back and then select Apply Settings for the changes to take effect.

![pijuice cli save changes](https://drive.google.com/open?id=18ElbsD_dEIYwJTMORD_QpNSc3gIP0jwy)

### Battery Profile

The Battery profile menu allows you to set up the battery profile, which includes all the battery characteristics such as capacity, voltages and temperature. It is very important that the battery profile is set correctly in order for your battery to operate efficiently and correctly monitor the voltage and battery levels.

There are a number of built-in battery profile presets such as the ones that will come with the PiJuce by default (BP7X) and all of the other ones that will be supplied. These default battery profiles can be set using the hardware DIP switch on the reverse side of the PiJuice board, so no software would be required.

![pijuice battery dip switches](https://user-images.githubusercontent.com/16068311/34769251-25c7c3b6-f5f5-11e7-971f-e93f5d4d3cc0.jpg)

To change the battery profile you will need to select **Profile** option and then select from one of the following battery profiles. If you have connected your own battery to to the PiJuice then you will need to select **Custom** from the profile options.

![pijuice cli battery menu](https://drive.google.com/open?id=1_Ng3PMTIEzNmOCc1pNXN086f-96qmNHD)

Before you can start changing the values of the battery profile you will need to make sure that you select **Custom** from the **Battery Settings** menu, when it is selected you will see a cross in the box.

![pijuice cli battery profile](https://drive.google.com/open?id=18oYuDL09o-kznBYvXoIGUyTlU7YUD_6R)

There is an option at the end of the menu which allows you to set weather your battery had a built-in NTC temperature sensor. An NTC temperature sensor will allow you to monitor the battery temperature for charging and is ultimately there for safety reasons. If your battery does not have an NTC temperature sensor then you can disable this option from the menu **Temperature sense**.

![pijuice cli battery NTC](https://drive.google.com/open?id=1gwg5lclekKJK46J-kUO5_UQzQT2WxKyQ)

Any changes made to the battery profile must be saved using the Apply Settings option.

### IO

The microcontroller on the PiJuice board had a number of available Input/Output pins that we can use in our projects. These pins are populated on a female header P3, which is next to the battery.

![pijuice cli io menu](https://drive.google.com/open?id=1GdMCR7TA3QQ-NxgseGec8wE5MvcBZNDu)

This menu option provides configuration for two IO port pin, IO1 and IO2. You can configure the pins to one of the pre-defined modes below:

- **NOT_USED:** Set IO pin in neutral configuration (passive input).
- **ANALOG_IN:** Set IO pin in analog to digital converter mode. In this mode Value can be read with status function GetIoAnalogInput(). Pull has no effect in this mode.
- **DIGITAL_IN:** Set IO pin in digital input mode. Pull in this mode can be set to NO_PULL,
PULLDOWN or PULLUP. Use status function SetIoDigitalOutput() to read input value dynamically.
- **DIGITAL_OUT_PUSHPULL:** Set IO pin in digital output mode with push-pull driver topology. Pull in this mode should be set to - NO_PULL. Initial value can be set to 0 or 1. Use status function SetIoDigitalOutput() to control output value dynamically.
- **DIGITAL_IO_OPEN_DRAIN:** Set IO pin in digital output mode with open-drain driver topology. Pull in this mode can be set to NO_PULL, PULLDOWN or PULLUP. Initial value can be set to 0 or 1. Use status function SetIoDigitalOutput() to control output value dynamically.
- **PWM_OUT_PUSHPULL:** Set IO pin to PWM output mode with push-pull driver topology. Pull in this mode should be set to NO_PULL. Period [us] box sets period in microseconds in range [2, 131072] with 2us resolution. Set initial duty_circle in range [0, 100]. Use status function SetIoPWM() to control duty cycle dynamically.
- **PWM_OUT_OPEN_DRAIN:** Set IO pin to PWM output mode with open-drain driver topology. Pull in this mode can be set to NO_PULL, PULLDOWN or PULLUP. Period [us] box sets period in microseconds in range [2, 131072] with 2us resolution. Set initial duty_circle in range [0, 100]. Use status function SetIoPWM() to control duty cycle dynamically.

In the menu you can select from two options, **Mode** and **Pull**.

![pijuice cli io options](https://drive.google.com/open?id=1WBEH5y5QO9OrKNGIESZZq2WeJVEMJdFN)

**Mode** provides a list of modes that you can select as mentioned previously above.

![pijuice cli io modes](https://drive.google.com/open?id=1bi8bUnlco-TRuHFQoRGFQrnGkoTyVoR0)

**Pull**, allows you to select the type of resistor pull for that particular pin. A **PULLUP** configuration will always default to 5V and a **PULLDOWN** will always default to GND.

![pijuice cli io pull](https://drive.google.com/open?id=1Y33C4qMWPFYr2Y-gXBOye8zDj2gSInR1)

### Wakeup Alarm

In this menu you can set the Raspberry Pi to automatically wakeup according to a schedule. This menu can be particular useful for remote monitoring application where the Raspberry Pi will wakeup, run a script and then go to sleep again until next time.

![pijuice cli wakeup](https://drive.google.com/open?id=1duvwtM2o7upyW5iuIhloMQDz1M36_w4i)

First thing you will need to do it set the system time, which will synchronise and update the internal clock. This is important to make sure you Raspberry Pi will wakeup at the correct time/day set. Simply select the Set system time option.

Next you can enable/disable the wakeup function by checking the Wakeup enabled box under the current time and date field. When the alarm goes off it will check if this box is enabled and then either wakeup the Raspberry Pi from a power down state or do nothing.

**Note: When the Raspberry Pi wakes up using this method the Wakeup enabled will be disabled by default.**

In the options following this you can set your alarm by entering the Day, Hour, minute, second and also if you wish to wake up the Raspberry Pi on a particular weekday or every day or hour. Once you have made the changes you will then need to make sure that you select the Set alarm option to save the alarm settings.

### Firmware

From time to time we are constantly improving the software and firmware on the PiJuice HAT board. In this menu you can check if there is an Firmware update available and if there is then you can update to the latest version.

![pijuice cli firmware](https://drive.google.com/open?id=16bLZVybUyZ_oXtaNWHDQ8K9UvP5os-kd)
