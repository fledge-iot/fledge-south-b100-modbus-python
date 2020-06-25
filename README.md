# fledge-south-b100-modbus-python

This south plugin is specifically for a Dynamic Ratings B100 Electronic Temperature Monitor used for monitoring the condition of electric transformers. It uses Modbus to poll the device. It only polls the LTC Tank and Top Oil temperatures, but it should be easy to add any other registers that are needed.

This plugin should also be a good template for developing other Python-based plugins using Modbus.

More information about the B100 is available here:

https://www.dynamicratings.com/b100-electronic-temperature-monitor/


## Installation

Copy the requirements-b100.txt to /usr/local/fledge/python/
pip3 install requirements-b100.txt

Create a directory called b100 for your plugin  
  
/usr/local/fledge/python/fledge/python/plugins/south/b100

Copy the __init__.py, b100.py, b100modbus.py files to /usr/local/fledge/python/fledge/python/plugins/south/b100