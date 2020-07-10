================================
fledge-south-b100-modbus-python
================================

This south plugin is specifically for a Dynamic Ratings B100 Electronic Temperature Monitor used for monitoring the condition of electric transformers. It uses Modbus to poll the device. It only polls the LTC Tank and Top Oil temperatures, but it should be easy to add any other registers that are needed.

This plugin should also be a good template for developing other Python-based plugins using Modbus.

More information about the B100 is available here:

https://www.dynamicratings.com/b100-electronic-temperature-monitor/


Installation
------------

1. Copy the python/fledge/plugins/south/b100 directory to /usr/local/fledge/python/fledge/python/plugins/south/

2. pip3 install -Ir python/requirements-b100.txt
