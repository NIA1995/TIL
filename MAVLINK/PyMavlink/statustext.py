from pymavlink import mavutil
import time

#connection_string = '/dev/ttyTHS1'

#master = mavutil.mavlink_connection(connection_string, 57600)

master = mavutil.mavlink_connection('udpout:192.168.2.1:14550', source_system = 1)
master.wait_heartbeat()

msg = master.recv_match(type="HEARTBEAT", blocking = True)
print(f"Heartbeat received : {msg}")

def send_custom_status_text(text):
    severity = 255

    print(master.mav.statustext_send(severity, text.encode()))
    
try:
    while 1:
        send_custom_status_text('Custom Status Text')

        time.sleep(2)

except KeyboardInterrupt:
    print("Exiting...")

    master.close()