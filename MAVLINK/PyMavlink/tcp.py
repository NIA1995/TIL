from pymavlink import mavutil
from openpyxl import Workbook
import time

connection = mavutil.mavlink_connection('udp:192.168.1.1:5760')

connection.mav.heartbeat_send(6,8,192,0,4,0)

msg = connection.recv_msg()
print(msg)

print("test of test")

connection.wait_heartbeat()

print("Heartbeat from system (system %u, component %u)" %
(connection.target_system, connection.target_component))

