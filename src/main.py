import utime
import machine
from app.motor import FET

mqtt = None

def run(mqtt_obj, parameters):
    print("got to run")
    #Make mqtt object global, so it can be called from interrupts
    global mqtt 
    mqtt = mqtt_obj
    m = FET()
    
    #Set project name as prefix so we can easily filter topics
    #Final topic will be in form:
    #UID/prefix/user_topic
    mqtt.set_prefix("hopper")

    mqtt.sub("move", m.drive)

    #Main loop
    mqtt.pub("status", "ready")
    while True:
        #Call periodicaly to check if we have recived new messages. 
        mqtt.check_msg()

        utime.sleep(0.1)
