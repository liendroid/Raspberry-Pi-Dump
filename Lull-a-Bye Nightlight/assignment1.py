import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

mc = 262
c1s = 277
d1 = 294
d1s = 311
e1 = 329
f1 = 349
f1s = 370
g1 = 392
g1s = 415
a1 = 440
a1sp = 455
b1f = 470
b1 = 493
b1s = 505
c2 = 523
c2s = 540
d2 = 578
d2s = 590
e2 = 620
e2s = 645
f2 = 678
fs2 = 690
g2 = 705
g2s = 720
a2 = 735
a2s = 755
b2 = 760
b2s = 771

redLED = 15
yellowLED = 18
blueLED = 14
#helper function to setup the buttons
def setupButtons():
    GPIO.setup(2, GPIO.IN)
    GPIO.setup(3, GPIO.IN)

#helper function to setup the buzzer
def setupBuzzer():
    GPIO.setup(4, GPIO.IN)
    GPIO.setup(4, GPIO.OUT)

#helper function to setup the LEDS
def setupLEDs():
    GPIO.setup(redLED, GPIO.OUT)
    GPIO.setup(yellowLED, GPIO.OUT)
    GPIO.setup(blueLED, GPIO.OUT)
    #make sure the leds are off
    GPIO.output(redLED, GPIO.LOW)
    GPIO.output(yellowLED, GPIO.LOW)
    GPIO.output(blueLED, GPIO.LOW)
    

#this code was modified from the source at http://www.linuxcircle.com/2015/04/12/how-to-play-piezo-buzzer-tunes-on-raspberry-pi-gpio-with-pwm/    
def buzz(pitch, duration):   #create the function “buzz” and feed it the pitch and duration)
  if(pitch==0):
   time.sleep(duration)
   return
  period = 1.0 / pitch     #in physics, the period (sec/cyc) is the inverse of the frequency (cyc/sec)
  delay = period / 2     #calcuate the time for half of the wave  
  cycles = int(duration * pitch)   #the number of waves to produce is the duration times the frequency

  for i in range(cycles):    #start a loop from 0 to the variable “cycles” calculated above
   GPIO.output(4, True)   #set pin 4 to high
   time.sleep(delay)    #wait with pin 4 high
   GPIO.output(4, False)    #set pin 4 to low
   time.sleep(delay)    #wait with pin 4 low
    
def playSong1():
    print("Wandering Path") #A song created by a friend. 
    quarterNote = 0.39
    wholeNote = 0.9
    
    #green
    GPIO.output(blueLED, GPIO.HIGH)
    buzz(g1, quarterNote)
    time.sleep(0.1)
    buzz(b1f, quarterNote)
    time.sleep(0.1)
    buzz(d2, quarterNote)
    time.sleep(0.1)

    
    buzz(g1, quarterNote)
    time.sleep(0.1)
    buzz(b1f, quarterNote)
    time.sleep(0.1)
    buzz(d2, quarterNote)
    time.sleep(0.1)

    GPIO.output(yellowLED, GPIO.LOW)
    buzz(f1, quarterNote)
    time.sleep(0.1)
    buzz(a1, quarterNote)
    time.sleep(0.1)
    buzz(c2, quarterNote)
    time.sleep(0.1)

    
    GPIO.output(redLED, GPIO.HIGH)
    buzz(f1, quarterNote)
    time.sleep(0.1)
    buzz(a1, quarterNote)
    time.sleep(0.1)
    buzz(c2, quarterNote)
    time.sleep(0.1)

    
    buzz(g1, quarterNote)
    time.sleep(0.1)
    buzz(b1f, quarterNote)
    time.sleep(0.1)
    buzz(d2, quarterNote)
    time.sleep(0.1)

    GPIO.output(blueLED, GPIO.LOW)
    buzz(g1, quarterNote)
    time.sleep(0.1)
    buzz(b1f, quarterNote)
    time.sleep(0.1)
    buzz(g2, quarterNote)
    time.sleep(0.1)


    buzz(a2s, quarterNote)
    time.sleep(0.1)
    buzz(a2, quarterNote)
    time.sleep(0.1)
    buzz(g1, quarterNote)
    time.sleep(0.1)

    GPIO.output(yellowLED, GPIO.HIGH)
    buzz(f2, quarterNote)
    time.sleep(0.1)
    buzz(d2, quarterNote)
    time.sleep(0.1)
    buzz(a1, quarterNote)
    time.sleep(0.1)

    buzz(g1, quarterNote)
    time.sleep(0.1)
    buzz(b1f, quarterNote)
    time.sleep(0.1)
    buzz(d2, quarterNote)
    time.sleep(0.1)

    GPIO.output(redLED, GPIO.LOW)
    buzz(g1, quarterNote)
    time.sleep(0.1)
    buzz(b1f, quarterNote)
    time.sleep(0.1)
    buzz(d2, quarterNote)
    time.sleep(0.1)

    buzz(f1, quarterNote)
    time.sleep(0.1)
    buzz(a2, quarterNote)
    time.sleep(0.1)
    buzz(c2, quarterNote)
    time.sleep(0.1)

    GPIO.output(blueLED, GPIO.HIGH)
    buzz(f1, quarterNote)
    time.sleep(0.1)
    buzz(a1, quarterNote)
    time.sleep(0.1)
    buzz(c2, quarterNote)
    time.sleep(0.1)

    buzz(g1, quarterNote)
    time.sleep(0.1)
    buzz(b1f, quarterNote)
    time.sleep(0.1)
    buzz(d2, quarterNote)
    time.sleep(0.1)

    GPIO.output(yellowLED, GPIO.LOW)
    buzz(b1f, quarterNote)
    time.sleep(0.1)
    buzz(d2, quarterNote)
    time.sleep(0.1)
    buzz(g2, quarterNote)
    time.sleep(0.1)


    buzz(d2, quarterNote)
    time.sleep(0.1)
    buzz(g2, quarterNote)
    time.sleep(0.1)
    buzz(a2s, quarterNote)
    time.sleep(0.1)
    GPIO.output(blueLED, GPIO.LOW)

    buzz(g1, wholeNote)
    time.sleep(0.1)
    return

def playSong2():
    print("twinkle twinkle litte star")
    wholeNote = 0.9
    halfNote = 0.4
    
    #twinkle twinkle little star
    GPIO.output(yellowLED, GPIO.HIGH)
    buzz(mc, halfNote)
    time.sleep(0.1)
    buzz(mc, halfNote)
    time.sleep(0.1)
    buzz(g1, halfNote)
    time.sleep(0.1)
    buzz(g1, halfNote)
    time.sleep(0.1)
    buzz(a1, halfNote)
    time.sleep(0.1)
    buzz(a1, halfNote)
    time.sleep(0.1)
    buzz(g1, wholeNote)
    time.sleep(0.1)
    
    #how I wonder what you are
    GPIO.output(yellowLED, GPIO.LOW)
    GPIO.output(blueLED, GPIO.HIGH)
    buzz(f1, halfNote)
    time.sleep(0.1)
    buzz(f1, halfNote)
    time.sleep(0.1)
    buzz(e1, halfNote)
    time.sleep(0.1)
    buzz(e1, halfNote)
    time.sleep(0.1)
    buzz(d1, halfNote)
    time.sleep(0.1)
    buzz(d1, halfNote)
    time.sleep(0.1)
    buzz(mc, wholeNote)
    time.sleep(0.1)
    
    #up above the world so high
    GPIO.output(redLED, GPIO.HIGH)
    buzz(g1, halfNote)
    time.sleep(0.1)
    buzz(g1, halfNote)
    time.sleep(0.1)
    buzz(f1, halfNote)
    time.sleep(0.1)
    buzz(f1, halfNote)
    time.sleep(0.1)
    buzz(e1, halfNote)
    time.sleep(0.1)
    buzz(e1, halfNote)
    time.sleep(0.1)
    buzz(d1, wholeNote)
    time.sleep(0.1)

    #like a diamond in the sky
    GPIO.output(blueLED, GPIO.LOW)
    GPIO.output(yellowLED, GPIO.HIGH)
    buzz(g1, halfNote)
    time.sleep(0.1)
    buzz(g1, halfNote)
    time.sleep(0.1)
    buzz(f1, halfNote)
    time.sleep(0.1)
    buzz(f1, halfNote)
    time.sleep(0.1)
    buzz(e1, halfNote)
    time.sleep(0.1)
    buzz(e1, halfNote)
    time.sleep(0.1)
    buzz(d1, wholeNote)
    time.sleep(0.1)
    

    #twinkle twinkle little star
    GPIO.output(yellowLED, GPIO.HIGH)
    buzz(mc, halfNote)
    time.sleep(0.1)
    buzz(mc, halfNote)
    time.sleep(0.1)
    buzz(g1, halfNote)
    time.sleep(0.1)
    buzz(g1, halfNote)
    time.sleep(0.1)
    buzz(a1, halfNote)
    time.sleep(0.1)
    buzz(a1, halfNote)
    time.sleep(0.1)
    buzz(g1, wholeNote)
    time.sleep(0.1)
    
    #how I wonder what you are
    GPIO.output(redLED, GPIO.LOW)
    buzz(f1, halfNote)
    time.sleep(0.1)
    buzz(f1, halfNote)
    time.sleep(0.1)
    buzz(e1, halfNote)
    time.sleep(0.1)
    buzz(e1, halfNote)
    time.sleep(0.1)
    buzz(d1, halfNote)
    time.sleep(0.1)
    buzz(d1, halfNote)
    time.sleep(0.1)
    buzz(mc, wholeNote)
    time.sleep(0.1)
    GPIO.output(yellowLED, GPIO.LOW)
        
    return


try:
    setupButtons()
    setupBuzzer()
    setupLEDs()
    while True:
        #this code was modified from http://razzpisampler.oreilly.com/ch07.html
        btn1_input_state = GPIO.input(2)
        btn2_input_state = GPIO.input(3)
        if btn1_input_state == False:
            print("song 1 selected")
            playSong1()
            time.sleep(0.2)        
        if btn2_input_state == False:
            print("song 2 selected")
            playSong2()
            time.sleep(0.2)
    
finally:
    print("bye! i'm cleaning up now")
    GPIO.cleanup() #gotta clean up your stuff mah. 
