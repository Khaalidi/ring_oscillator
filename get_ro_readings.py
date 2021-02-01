import serial
import time
import json
import sys

def parse(raw_string):
    if raw_string:
        parsed_data = raw_string.decode()
        parsed_data = parsed_data.split('+')
        parsed_data = [int(i) for i in parsed_data] 
        return parsed_data
    return 0

def read_uart():
    ser = serial.Serial(
        port='COM5',
        baudrate=115200,
        timeout=1,
        parity=serial.PARITY_ODD,
        stopbits=serial.STOPBITS_TWO,
        bytesize=serial.SEVENBITS
    )
    ser.isOpen()
    # Reading the data from the serial port. This will be running in an infinite loop.
    print("Waiting...")
    readings = []


    while True :
        buffer = b''
        line = ser.readline()
        if line:
            parsed_data = parse(line)
            print("RAW: {}".format(line))
            print(parsed_data)
            readings.append(parsed_data)

            DataFile = open(sys.argv[1], "w")
            DataFile.write(json.dumps(readings, indent=4, sort_keys=True))
            DataFile.close()         

read_uart()