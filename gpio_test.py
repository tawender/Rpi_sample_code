import RPi.GPIO as GPIO
import time

#set the mode to BCM for GPIO numbers
GPIO.setmode(GPIO.BCM)


#set GPIO16,20 as output pins
outlist = [16,20]
GPIO.setup(outlist,GPIO.OUT)


while(1):
    GPIO.output(16,1)
    GPIO.output(20,0)
    time.sleep(0.5)
    GPIO.output(16,0)
    GPIO.output(20,1)
    time.sleep(0.5)



#set channels used to inputs with no pull up/down
GPIO.cleanup()
