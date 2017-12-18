#Name: Michael Boimistruck
#Assignment: Lab 7 TYK#2
#Description: LED looped 6 times.

import RPi.GPIO as GPIO;
import time;

GPIO.setwarnings(False);
GPIO.setmode(GPIO.BCM);
GPIO.setup(35, GPIO.OUT);

for i in range(0, 5)
    GPIO.output(35, GPIO.HIGH);
    print("LED On.");
    time.sleep(0.5);
    GPIO.output(35, GPIO.LOW);
    print("LED Off.");
    time.sleep(0.5);