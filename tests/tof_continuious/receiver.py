""" Receive TOF sensor values on serial"""
import serial

port = 'COM3'
baudrate = 115200
ser = serial.Serial(port=port, baudrate=baudrate)

while True:
    try:
        val = int(ser.readline().decode('utf-8'))
        print(val)

    except KeyboardInterrupt:
        break
