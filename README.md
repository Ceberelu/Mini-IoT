# Mini-IoT
Mini web server (on/off buttons) for raspberry pi which controls 433 MHz power plugs. 

# Prerequisites
You should know the 433 MHz codes - you can find them with a 433MHz receiver - see steps in ninjablock link below.

# Dependencies
433 MHz drivers and application: http://shop.ninjablocks.com/blogs/how-to/7506204-adding-433-to-your-raspberry-pi
Flask for the web server; see Instalation and Qick start on the official page: http://flask.pocoo.org/docs/0.11/

# How to run
Make sure you have set the FLASK_APP variable
export FLASK_APP=YOUR_PATH/iotHub.py
flask run --host=0.0.0.0

# Limitations
  - There is no configuration file - 433 MHz codes and the path to 433MHz app is hardcoded
  - sudo priviledges required due to WiringPi implementation
  - minimum error checking on python code
