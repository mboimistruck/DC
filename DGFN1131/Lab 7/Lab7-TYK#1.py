#Name: Michael Boimistruck
#Assignment: Lab 7 TYK#1
#Description: LED on for 1 second, off for 2. Infinite loop.

import RPi.GPIO as GPIO;
import time;

GPIO.setwarnings(False);
GPIO.setmode(GPIO.BCM);
GPIO.setup(26, GPIO.OUT);

while(True)
    GPIO.output(26, GPIO.HIGH);
    print("LED On.");
    time.sleep(1);
    GPIO.output(26, GPIO.LOW);
    print("LED Off.");
    time.sleep(2);