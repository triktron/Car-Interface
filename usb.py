import serial
import time

ser = serial.Serial('/dev/ttyUSB0', 115200)

while True:
    if (ser.inWaiting()>0):
        data_str = ser.read(ser.inWaiting()).decode()
        print(data_str)

    ser.write(b'S')
    time.sleep(0.005)
