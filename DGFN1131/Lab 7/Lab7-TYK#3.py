#Name: Michael Boimistruck
#Assignment: Lab 7 TYK#3
#Description: LED looped 6 times with counter.

import RPi.GPIO as GPIO;
import time;

x = 0;

GPIO.setwarnings(False);
GPIO.setmode(GPIO.BCM);
GPIO.setup(35, GPIO.OUT);

while(x < 6):
    GPIO.output(35, GPIO.HIGH);
    print("LED On.");
    time.sleep(0.5);
    GPIO.output(35, GPIO.LOW);
    print("LED Off.");
    time.sleep(0.5);
    x += 1;