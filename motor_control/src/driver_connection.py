# -*- coding: utf-8 -*-
"""
@author: Small Brian
@email: dalbobo3122@gmail.com
@date: 2023/02/13
@version: 1.0
@brief: Establish the connection with the driver
"""
import serial
import modbus_tk
import modbus_tk.modbus_rtu as modbus_rtu
class driver_connection():
    def __init__(self, PORT = '/dev/ttyUSB0'):
        self.active = False
        self.master = modbus_rtu.RtuMaster(serial.Serial(port=PORT, baudrate=9600, bytesize=8, parity='N', stopbits=1, xonxoff=0))
        self.master.set_timeout(1.0)
        self.master.set_verbose(True)
        self.active = True
        print("Driver connection establish successfully!")
    def __del__(self):
        driver_connection.driver_close()
    def driver_close(self):
        if (self.master._do_close()):
            self.active = False
            print("Driver connection closed")
