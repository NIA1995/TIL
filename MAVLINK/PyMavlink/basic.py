import serial
import time
from pymavlink import mavutil

import pymavlink.dialects.v20.all as dialect

serial_port = '/dev/ttyTHS1'
baud_rate = 57600

connection = mavutil.mavlink_connection(serial_port, baud = baud_rate)

while True:
    msg = connection.recv_msg()

    #if msg:
    print(msg)
    time.sleep(1.0)
    connection.mav.statustext_send(mavutil.mavlink.MAV_SEVERITY_ERROR, "QGC will read this".encode('utf8'))

    message = dialect.MAVLink_statustext_message(severity=dialect.MAV_SEVERITY_INFO, text = "GRANADO ESPADA".encode("utf-8"))

    connection.mav.send(message)
