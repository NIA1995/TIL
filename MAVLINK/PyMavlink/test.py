from pymavlink import mavutil
from openpyxl import Workbook
import time

wb = Workbook()

ws = wb.create_sheet('GPS Data')

ws.append(["lat", "lon", "alt", "time_usec"])

new_filename = '/home/astrox/Desktop/PyMavlink/test.xlsx'

the_connection = mavutil.mavlink_connection("/dev/ttyTHS1", baud = 57600)

the_connection.wait_heartbeat()

print("Heartbeat from system (system %u, component %u)" %
(the_connection.target_system, the_connection.target_component))

global isArmd 
isArmd = False

def check_arming_state():

    global isArmd

    while not isArmd:
        msg = the_connection.recv_match(type='HEARTBEAT', blocking = True)

        if msg is not None:
            arming_state = msg.base_mode & mavutil.mavlink.MAV_MODE_FLAG_SAFETY_ARMED
            print(arming_state)
            if arming_state == mavutil.mavlink.MAV_MODE_FLAG_SAFETY_ARMED:
                isArmd = True
                print(arming_state)
            

connected = False

while not connected:
    try:
        msg = the_connection.recv_match(type = 'HEARTBEAT', blocking = True)

        if msg is not None:
            connected = True

            print("Vehicle is connected !")
            
    except KeyboardInterrupt:
        break

print(isArmd)

#heck_arming_state()

print(isArmd)

while connected:
    msg = the_connection.recv_match(type = 'GPS_RAW_INT')

    if not msg:
        continue

    if msg.get_type() == "GPS_RAW_INT":
        print("\nAs dictionary : %s" % msg.to_dict())

        print("\nlat : %s " % msg.lat)
        print("\nlat : %s " % msg.lon)
        print("\nlat : %s " % msg.alt)    

        ws.append([msg.lat, msg.lon, msg.alt, msg.time_usec])


    msg = the_connection.recv_match(type = 'HEARTBEAT', blocking = True, timeout = 2.0)

    if msg is None:
        connected = False

        print("Connection lost. Exiting.")
        break   


wb.save(new_filename)