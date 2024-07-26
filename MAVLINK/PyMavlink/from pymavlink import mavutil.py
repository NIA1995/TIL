from pymavlink import mavutil

master = mavutil.mavlink_connection('udpout:localhost:14550', source_system = 1)

master.mav.statustext_send(mavutil.mavlink.MAV_SEVERITY_NOTICE, "GRANADO ESPADA".encode())

while(True):
    user_input = input("Enter q to quit: ")
    if(user_input.lower()) == "q":
        break