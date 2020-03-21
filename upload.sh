#!/bin/bash

host=10.1.1.95
dest=886e8000

mosquitto_pub -h $host -t $dest/sys/file -m app/main.py &&\
sleep 1 &&\
mosquitto_pub -h $host -t $dest/sys/write -f src/main.py &&\
sleep 1 &&\
mosquitto_pub -h $host -t $dest/sys/file -m app/motor.py &&\
sleep 1 &&\
mosquitto_pub -h $host -t $dest/sys/write -f src/motor.py &&\
sleep 1 &&\
mosquitto_pub -h $host -t $dest/sys/reboot -m ""
