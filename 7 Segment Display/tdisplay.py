#7 pin display for raspberry pi
#16 pins not 12
# all the tears

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

segments = (2, 3, 4, 17, 27, 22, 10)

digits = (14, 15, 18, 23)


print("in digit loop")
GPIO.setup(14, GPIO.OUT)
GPIO.output(14, 1)
GPIO.setup(15, GPIO.OUT)
GPIO.output(15, 1)
GPIO.setup(18, GPIO.OUT)
GPIO.output(18, 1)
GPIO.setup(23, GPIO.OUT)
GPIO.output(23, 1)

print("setting up segments")
GPIO.setup(2, GPIO.OUT)
GPIO.output(2, 0)
GPIO.setup(3, GPIO.OUT)
GPIO.output(3, 0)
GPIO.setup(4, GPIO.OUT)
GPIO.output(4, 0)
GPIO.setup(17, GPIO.OUT)
GPIO.output(17, 0)
GPIO.setup(27, GPIO.OUT)
GPIO.output(27, 0)
GPIO.setup(22, GPIO.OUT)
GPIO.output(22, 0)
GPIO.setup(10, GPIO.OUT)
GPIO.output(10, 0)

print("setting up the buttons")
GPIO.setup(9, GPIO.IN)
GPIO.setup(11, GPIO.IN)


        
def zero():
    #pins 2, 3, 4, 27, 10, 22 should be activated
    print("i should be 0")
    GPIO.output(2, 0)
    GPIO.output(3, 0)
    GPIO.output(4, 0)
    GPIO.output(17, 1)
    GPIO.output(27, 0)
    GPIO.output(10, 0)
    GPIO.output(22, 0)

def one():
    #pins 4, 22 should be activated
    GPIO.output(2, 1)
    GPIO.output(3, 1)
    GPIO.output(4, 0)
    GPIO.output(17, 1)
    GPIO.output(27, 1)
    GPIO.output(10, 1)
    GPIO.output(22, 0)

def two():
    #pins 2, 3, 17, 4, 27 should be activated
    GPIO.output(2, 0)
    GPIO.output(3, 0)
    GPIO.output(4, 0)
    GPIO.output(17, 0)
    GPIO.output(27, 0)
    GPIO.output(10, 1)
    GPIO.output(22, 1)

def three():
    #pins 2, 4, 17, 22, 27 should be activated
    GPIO.output(2, 0)
    GPIO.output(3, 1)
    GPIO.output(4, 0)
    GPIO.output(17, 0)
    GPIO.output(27, 0)
    GPIO.output(10, 1)
    GPIO.output(22, 0)

def four():
    #pins 4, 10, 17, 22 should be activated
    GPIO.output(2, 1)
    GPIO.output(3, 1)
    GPIO.output(4, 0)
    GPIO.output(17, 0)
    GPIO.output(27, 1)
    GPIO.output(10, 0)
    GPIO.output(22, 0)

def five():
    #2, 17, 22, 10, 27
    GPIO.output(2, 0)
    GPIO.output(3, 1)
    GPIO.output(4, 1)
    GPIO.output(17, 0)
    GPIO.output(27, 0)
    GPIO.output(10, 0)
    GPIO.output(22, 0)

def six():
    #10, 17, 22, 3, 2
    GPIO.output(2, 0)
    GPIO.output(3, 0)
    GPIO.output(4, 1)
    GPIO.output(17, 0)
    GPIO.output(27, 1)
    GPIO.output(10, 0)
    GPIO.output(22, 0)

def seven():
    #27, 4, 22
    GPIO.output(2, 1)
    GPIO.output(3, 1)
    GPIO.output(4, 0)
    GPIO.output(17, 1)
    GPIO.output(27, 0)
    GPIO.output(10, 1)
    GPIO.output(22, 0)

def eight():
    #all pins
    GPIO.output(2, 0)
    GPIO.output(3, 0)
    GPIO.output(4, 0)
    GPIO.output(17, 0)
    GPIO.output(27, 0)
    GPIO.output(10, 0)
    GPIO.output(22, 0)

def nine():
    #all but 3
    GPIO.output(2, 0)
    GPIO.output(3, 1)
    GPIO.output(4, 0)
    GPIO.output(17, 0)
    GPIO.output(27, 0)
    GPIO.output(10, 0)
    GPIO.output(22, 0)
            
try:
    m = 0
    while True:
        btnChangeInputState = GPIO.input(9)
        btnSelectInputState = GPIO.input(11)
        
        if btnChangeInputState == True:
            #if btnChangeInput
            GPIO.output(digits[m], 0)
            m = m + 1
        n = 0 #counter for the bus index.
        if n == 0:
            zero()
            time.sleep(1)
            print("should be a 0")
            n = 1
        if n == 1:
            one()
            time.sleep(1)
            print("should be a 1")
            n = 2
        if n == 2:
            two()
            time.sleep(1)
            print("should be a 2")
            n = 3
            
        if n == 3:
            three()
            time.sleep(1)
            print("should be a 3")
            n = 4

        if n == 4:
            four()
            time.sleep(1)
            print("should be a 4")
            n = 5

        if n == 5:
            five()
            time.sleep(1)
            print("should be a 5")
            n = 6

        if n == 6:
            six()
            time.sleep(1)
            print("should be a 6")
            n = 7
            
        if n == 7:
            seven()
            time.sleep(1)
            print("should be a 7")
            n = 8

        if n == 8:
            eight()
            time.sleep(1)
            print("should be a 8")
            n = 9
            
        if n == 9:
            nine()
            time.sleep(1)
            print("should be a 9")
            
        
        
finally:
        GPIO.cleanup()

