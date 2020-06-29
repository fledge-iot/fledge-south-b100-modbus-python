# -*- coding: utf-8 -*-

# FLEDGE_BEGIN
# See: http://fledge.readthedocs.io/
# FLEDGE_END


from pymodbus.client.sync import ModbusTcpClient as ModbusClient
from pymodbus.transaction import ModbusRtuFramer as ModbusFramer
from pymodbus.constants import Endian
from pymodbus.payload import BinaryPayloadDecoder

modbus_client = None

LTC_TANK_TEMP_REGISTER = 216
TOP_OIL_TEMP_REGISTER = 268

def convert_to_scaled_signedint(registers,scaling_value):
    """ Converts unsigned int from Modbus device to a signed integer divided by the scaling_value """
    decoder = BinaryPayloadDecoder.fromRegisters(registers, byteorder=Endian.Big, wordorder=Endian.Little)
    number = decoder.decode_32bit_int()
    number = number / scaling_value
    return number

def get_b100_readings(address, port):
    global modbus_client

    if modbus_client is None:
        try:
            modbus_client = ModbusClient(address, port=port, framer=ModbusFramer)
        except:
            raise ValueError

    ltc_tank_temp = None
    top_oil_temp = None

    # read LTC Tank Temperature
    try:
        ltc_tank_temp_read = modbus_client.read_input_registers(LTC_TANK_TEMP_REGISTER,2,unit=1)
        ltc_tank_temp_raw = ltc_tank_temp_read.registers[0]
        ltc_tank_temp = convert_to_scaled_signedint(val,1000)
    except Exception as ex:
        ltc_tank_temp = f'error: {ex}'

    try:
        top_oil_temp_read = modbus_client.read_input_registers(TOP_OIL_TEMP_REGISTER,2,unit=1)
        top_oil_temp_raw = top_oil_temp_read.registers[0]
        top_oil_temp = convert_to_scaled_signedint(ltc_tank_temp_raw,1000)
    except Exception as ex:
        top_oil_temp = f'error: {ex}'

    readings = {
        'ltc_tank_temp': ltc_tank_temp,
        'top_oil_temp': top_oil_temp
        }

    return readings

def close_connection():
    global modbus_client
    try:
        if modbus_client is not None:
            modbus_client.close()
            return('B100 client connection closed.')
    except:
        raise
    else:
        modbus_client = None
        return('B100 plugin shut down.')