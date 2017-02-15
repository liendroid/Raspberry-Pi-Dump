# this class was referenced from the dice game
# mentioned in the documentation
import pygame, time
from pygame.locals import *
import RPi.GPIO as GPIO

from sys import exit
import os

import Adafruit_GPIO.SPI as SPI
import Adafruit_MCP3008

# Mode Constants
NORMAL = 0
MERUP = 1

# Button Constants
COCO = 0
DANI = 1
FIFI = 2
GABBY = 3
APPA = 4

# GPIO Pins
CLK  = 11
MISO = 9
MOSI = 10
CS   = 8

# Canvas Offset via pixels
OFFSET = 20

mcp = Adafruit_MCP3008.MCP3008(clk=CLK, cs=CS, miso=MISO, mosi=MOSI)

# Sensor Values
cValue = 0
dValue = 0
fValue = 0
gValue = 0
aValue = 0

# happy images
COCO_IMG_HAPPY = "img/coco-happy.png"
DANI_IMG_HAPPY = "img/dani-happy.png"
FIFI_IMG_HAPPY = "img/fifi-happy.png"
GABBY_IMG_HAPPY = "img/gabby-happy.png"
APPA_IMG_HAPPY = "img/appa-happy.png"

# crying images
COCO_IMG_CRYING  = "img/coco-crying.png"
DANI_IMG_CRYING  = "img/dani-crying.png"
FIFI_IMG_CRYING  = "img/fifi-crying.png"
GABBY_IMG_CRYING  = "img/gabby-crying.png"
APPA_IMG_CRYING  = "img/appa-crying.png"

# abused images. </3
COCO_IMG_ABUSED  = "img/coco-abused.png"
DANI_IMG_ABUSED  = "img/dani-abused.png"
FIFI_IMG_ABUSED  = "img/fifi-abused.png"
GABBY_IMG_ABUSED  = "img/gabby-abused.png"
APPA_IMG_ABUSED  = "img/appa-abused.png"

pygame.mixer.init(48000, 16, 5, 1024)

# load in the piano sounds
C5 = pygame.mixer.Sound("C5.wav")
D5 = pygame.mixer.Sound("D5.wav")
F5 = pygame.mixer.Sound("F5.wav")
G5 = pygame.mixer.Sound("G5.wav")
A5 = pygame.mixer.Sound("A5.wav")

C6 = pygame.mixer.Sound("C6.wav")
D6 = pygame.mixer.Sound("D6.wav")
F6 = pygame.mixer.Sound("F6.wav")
G6 = pygame.mixer.Sound("G6.wav")
A6 = pygame.mixer.Sound("A6.wav")

# shh. load in the merup!
C9 = pygame.mixer.Sound("C9.wav")
D9 = pygame.mixer.Sound("D9.wav")
F9 = pygame.mixer.Sound("F9.wav")
G9 = pygame.mixer.Sound("G9.wav")
A9 = pygame.mixer.Sound("A9.wav")

# Assign Channels
cocoChannel = pygame.mixer.Channel(1)
daniChannel = pygame.mixer.Channel(2)
fifiChannel = pygame.mixer.Channel(3)
gabbyChannel = pygame.mixer.Channel(4)
appaChannel = pygame.mixer.Channel(5)

# modeChangeBuffer keeps track of the six most recent notes played
# When modeChangeBuffer matches one of the first two lists, the
# mode is changed to the corresponding one.
merupBuffer = ["D5", "F5", "D6", "D5", "F5", "D6"]
normalBuffer = ["A9", "D9", "A9", "F9", "D9", "C9"]
modeChangeBuffer = [0,0,0,0,0,0]

def squishyGame(window):
    image = pygame.Surface((50,50))
    window.fill((255,255,255))

    #import happy squishies
    cocoHappy = pygame.image.load(COCO_IMG_HAPPY).convert_alpha()
    daniHappy = pygame.image.load(DANI_IMG_HAPPY).convert_alpha()
    fifiHappy = pygame.image.load(FIFI_IMG_HAPPY).convert_alpha()
    gabbyHappy = pygame.image.load(GABBY_IMG_HAPPY).convert_alpha()
    appaHappy = pygame.image.load(APPA_IMG_HAPPY).convert_alpha()
        
    #import crying squishies
    cocoSad = pygame.image.load(COCO_IMG_CRYING).convert_alpha()
    daniSad = pygame.image.load(DANI_IMG_CRYING).convert_alpha()
    fifiSad = pygame.image.load(FIFI_IMG_CRYING).convert_alpha()
    gabbySad = pygame.image.load(GABBY_IMG_CRYING).convert_alpha()
    appaSad = pygame.image.load(APPA_IMG_CRYING).convert_alpha()

    #import abused squishies. for shame. >:C
    cocoAbused = pygame.image.load(COCO_IMG_ABUSED).convert_alpha()
    daniAbused = pygame.image.load(DANI_IMG_ABUSED).convert_alpha()
    fifiAbused = pygame.image.load(FIFI_IMG_ABUSED).convert_alpha()
    gabbyAbused = pygame.image.load(GABBY_IMG_ABUSED).convert_alpha()
    appaAbused = pygame.image.load(APPA_IMG_ABUSED).convert_alpha()

    print("Ready to play!")
    mode = NORMAL
    
    while True:
        window.fill((255,255,255))

        window.blit(cocoHappy, (20,300))
        window.blit(daniHappy, (190,250))
        window.blit(fifiHappy, (340,200))
        window.blit(gabbyHappy, (490,250))
        window.blit(appaHappy, (630,300))

        pygame.display.update()

        # on close event because if this isn't here. Bad things.
        cvalue = mcp.read_adc(0)
        dvalue = mcp.read_adc(1)
        fvalue = mcp.read_adc(2)
        gvalue = mcp.read_adc(3)
        avalue = mcp.read_adc(4)

        try:
            if mode == NORMAL:
                if cvalue > 70:
                    print("pressed coco", cvalue)
                    cocoChannel.play(C6)
                    #clear the window and redraw everything but change
                    #the squishie in question
                    window.fill((255,255,255))

                    window.blit(cocoAbused, (20,300))
                    window.blit(daniHappy, (190,250))
                    window.blit(fifiHappy, (340,200))
                    window.blit(gabbyHappy, (490,250))
                    window.blit(appaHappy, (630,300))

                    pygame.display.update()
                    
                    time.sleep(0.1)
                    
                    modeChangeBuffer[0] = modeChangeBuffer[1]
                    modeChangeBuffer[1] = modeChangeBuffer[2]
                    modeChangeBuffer[2] = modeChangeBuffer[3]
                    modeChangeBuffer[3] = modeChangeBuffer[4]
                    modeChangeBuffer[4] = modeChangeBuffer[5]
                    modeChangeBuffer[5] = "C6"
                    
                elif cvalue > 10:
                    print("pressed coco", cvalue)
                    cocoChannel.play(C5)

                    window.fill((255,255,255))

                    window.blit(cocoSad, (20,300))
                    window.blit(daniHappy, (190,250))
                    window.blit(fifiHappy, (340,200))
                    window.blit(gabbyHappy, (490,250))
                    window.blit(appaHappy, (630,300))

                    pygame.display.update()
                    
                    time.sleep(0.1)
                    
                    modeChangeBuffer[0] = modeChangeBuffer[1]
                    modeChangeBuffer[1] = modeChangeBuffer[2]
                    modeChangeBuffer[2] = modeChangeBuffer[3]
                    modeChangeBuffer[3] = modeChangeBuffer[4]
                    modeChangeBuffer[4] = modeChangeBuffer[5]
                    modeChangeBuffer[5] = "C5"

                if dvalue > 70:
                    print("pressed dani", dvalue)
                    daniChannel.play(D6)
                    
                    window.fill((255,255,255))

                    window.blit(cocoHappy, (20,300))
                    window.blit(daniAbused, (190,250))
                    window.blit(fifiHappy, (340,200))
                    window.blit(gabbyHappy, (490,250))
                    window.blit(appaHappy, (630,300))
                    pygame.display.update()
                    
                    time.sleep(0.1)

                    modeChangeBuffer[0] = modeChangeBuffer[1]
                    modeChangeBuffer[1] = modeChangeBuffer[2]
                    modeChangeBuffer[2] = modeChangeBuffer[3]
                    modeChangeBuffer[3] = modeChangeBuffer[4]
                    modeChangeBuffer[4] = modeChangeBuffer[5]
                    modeChangeBuffer[5] = "D6"

                elif dvalue > 10:
                    print("pressed dani", dvalue)
                    daniChannel.play(D5)
                    
                    window.fill((255,255,255))

                    window.blit(cocoHappy, (20,300))
                    window.blit(daniSad, (190,250))
                    window.blit(fifiHappy, (340,200))
                    window.blit(gabbyHappy, (490,250))
                    window.blit(appaHappy, (630,300))

                    pygame.display.update()
                    

                    time.sleep(0.1)

                    modeChangeBuffer[0] = modeChangeBuffer[1]
                    modeChangeBuffer[1] = modeChangeBuffer[2]
                    modeChangeBuffer[2] = modeChangeBuffer[3]
                    modeChangeBuffer[3] = modeChangeBuffer[4]
                    modeChangeBuffer[4] = modeChangeBuffer[5]
                    modeChangeBuffer[5] = "D5"

                if fvalue > 70:
                    print("pressed fifi", fvalue)
                    fifiChannel.play(F6)

                    window.fill((255,255,255))

                    window.blit(cocoHappy, (20,300))
                    window.blit(daniHappy, (190,250))
                    window.blit(fifiAbused, (340,200))
                    window.blit(gabbyHappy, (490,250))
                    window.blit(appaHappy, (630,300))

                    pygame.display.update()
        
                    time.sleep(0.1)

                    modeChangeBuffer[0] = modeChangeBuffer[1]
                    modeChangeBuffer[1] = modeChangeBuffer[2]
                    modeChangeBuffer[2] = modeChangeBuffer[3]
                    modeChangeBuffer[3] = modeChangeBuffer[4]
                    modeChangeBuffer[4] = modeChangeBuffer[5]
                    modeChangeBuffer[5] = "F6"

                elif fvalue > 10:
                    print("pressed fifi", fvalue)
                    fifiChannel.play(F5)

                    window.fill((255,255,255))
                    
                    window.blit(cocoHappy, (20,300))
                    window.blit(daniHappy, (190,250))
                    window.blit(fifiSad, (340,200))
                    window.blit(gabbyHappy, (490,250))
                    window.blit(appaHappy, (630,300))

                    pygame.display.update()
                    
                    time.sleep(0.1)
                    modeChangeBuffer[0] = modeChangeBuffer[1]
                    modeChangeBuffer[1] = modeChangeBuffer[2]
                    modeChangeBuffer[2] = modeChangeBuffer[3]
                    modeChangeBuffer[3] = modeChangeBuffer[4]
                    modeChangeBuffer[4] = modeChangeBuffer[5]
                    modeChangeBuffer[5] = "F5"

                if gvalue > 70:
                    print("pressed gabby", gvalue)
                    gabbyChannel.play(G6)

                    window.fill((255,255,255))

                    window.blit(cocoHappy, (20,300))
                    window.blit(daniHappy, (190,250))
                    window.blit(fifiHappy, (340,200))
                    window.blit(gabbyAbused, (490,250))
                    window.blit(appaHappy, (630,300))
                    pygame.display.update()

                    time.sleep(0.1)

                    modeChangeBuffer[0] = modeChangeBuffer[1]
                    modeChangeBuffer[1] = modeChangeBuffer[2]
                    modeChangeBuffer[2] = modeChangeBuffer[3]
                    modeChangeBuffer[3] = modeChangeBuffer[4]
                    modeChangeBuffer[4] = modeChangeBuffer[5]
                    modeChangeBuffer[5] = "G6"

                elif gvalue > 10:
                    print("pressed gabby", gvalue)
                    gabbyChannel.play(G5)
                    
                    window.fill((255,255,255))

                    window.blit(cocoHappy, (20,300))
                    window.blit(daniHappy, (190,250))
                    window.blit(fifiHappy, (340,200))
                    window.blit(gabbySad, (490,250))
                    window.blit(appaHappy, (630,300))

                    pygame.display.update()
                    
                    time.sleep(0.1)

                    modeChangeBuffer[0] = modeChangeBuffer[1]
                    modeChangeBuffer[1] = modeChangeBuffer[2]
                    modeChangeBuffer[2] = modeChangeBuffer[3]
                    modeChangeBuffer[3] = modeChangeBuffer[4]
                    modeChangeBuffer[4] = modeChangeBuffer[5]
                    modeChangeBuffer[5] = "G5"

                if avalue > 70:
                    print("pressed appa", avalue)
                    appaChannel.play(A6)

                    window.fill((255,255,255))

                    window.blit(cocoHappy, (20,300))
                    window.blit(daniHappy, (190,250))
                    window.blit(fifiHappy, (340,200))
                    window.blit(gabbyHappy, (490,250))
                    window.blit(appaAbused, (630,300))

                    pygame.display.update()
                    
                    time.sleep(0.1)
                    
                    modeChangeBuffer[0] = modeChangeBuffer[1]
                    modeChangeBuffer[1] = modeChangeBuffer[2]
                    modeChangeBuffer[2] = modeChangeBuffer[3]
                    modeChangeBuffer[3] = modeChangeBuffer[4]
                    modeChangeBuffer[4] = modeChangeBuffer[5]
                    modeChangeBuffer[5] = "A6"
  

                elif avalue > 10:
                    print("pressed appa", avalue)
                    appaChannel.play(A5)

                    window.fill((255,255,255))

                    window.blit(cocoHappy, (20,300))
                    window.blit(daniHappy, (190,250))
                    window.blit(fifiHappy, (340,200))
                    window.blit(gabbyHappy, (490,250))
                    window.blit(appaSad, (630,300))

                    pygame.display.update()
        
                    time.sleep(0.1)

                    modeChangeBuffer[0] = modeChangeBuffer[1]
                    modeChangeBuffer[1] = modeChangeBuffer[2]
                    modeChangeBuffer[2] = modeChangeBuffer[3]
                    modeChangeBuffer[3] = modeChangeBuffer[4]
                    modeChangeBuffer[4] = modeChangeBuffer[5]
                    modeChangeBuffer[5] = "A5"

                if compare(modeChangeBuffer, merupBuffer):
                    mode = MERUP

            elif mode == MERUP:
                if cvalue > 10:
                    print("pressed coco", cvalue)
                    cocoChannel.play(C9)
                    
                    window.fill((255,255,255))
                    
                    window.blit(cocoSad, (20,300))
                    window.blit(daniHappy, (190,250))
                    window.blit(fifiHappy, (340,200))
                    window.blit(gabbyHappy, (490,250))
                    window.blit(appaHappy, (630,300))

                    pygame.display.update()
    
                    time.sleep(0.1)

                    modeChangeBuffer[0] = modeChangeBuffer[1]
                    modeChangeBuffer[1] = modeChangeBuffer[2]
                    modeChangeBuffer[2] = modeChangeBuffer[3]
                    modeChangeBuffer[3] = modeChangeBuffer[4]
                    modeChangeBuffer[4] = modeChangeBuffer[5]
                    modeChangeBuffer[5] = "C9"

                if dvalue > 10:
                    print("pressed dani", dvalue)
                    daniChannel.play(D9)
                    
                    window.fill((255,255,255))

                    window.blit(cocoHappy, (20,300))
                    window.blit(daniSad, (190,250))
                    window.blit(fifiHappy, (340,200))
                    window.blit(gabbyHappy, (490,250))
                    window.blit(appaHappy, (630,300))

                    pygame.display.update()

                    time.sleep(0.1)

                    modeChangeBuffer[0] = modeChangeBuffer[1]
                    modeChangeBuffer[1] = modeChangeBuffer[2]
                    modeChangeBuffer[2] = modeChangeBuffer[3]
                    modeChangeBuffer[3] = modeChangeBuffer[4]
                    modeChangeBuffer[4] = modeChangeBuffer[5]
                    modeChangeBuffer[5] = "D9"

                if fvalue > 10:
                    print("pressed fifi", fvalue)
                    fifiChannel.play(F9)
                    
                    window.fill((255,255,255))

                    window.blit(cocoHappy, (20,300))
                    window.blit(daniHappy, (190,250))
                    window.blit(fifiSad, (340,200))
                    window.blit(gabbyHappy, (490,250))
                    window.blit(appaHappy, (630,300))

                    pygame.display.update()

                    time.sleep(0.1)

                    modeChangeBuffer[0] = modeChangeBuffer[1]
                    modeChangeBuffer[1] = modeChangeBuffer[2]
                    modeChangeBuffer[2] = modeChangeBuffer[3]
                    modeChangeBuffer[3] = modeChangeBuffer[4]
                    modeChangeBuffer[4] = modeChangeBuffer[5]
                    modeChangeBuffer[5] = "F9"

                if gvalue > 10:
                    print("pressed gabby", gvalue)
                    gabbyChannel.play(G9)
                    
                    window.fill((255,255,255))

                    window.blit(cocoHappy, (20,300))
                    window.blit(daniHappy, (190,250))
                    window.blit(fifiHappy, (340,200))
                    window.blit(gabbySad, (490,250))
                    window.blit(appaHappy, (630,300))

                    pygame.display.update()

                    time.sleep(0.1)

                    modeChangeBuffer[0] = modeChangeBuffer[1]
                    modeChangeBuffer[1] = modeChangeBuffer[2]
                    modeChangeBuffer[2] = modeChangeBuffer[3]
                    modeChangeBuffer[3] = modeChangeBuffer[4]
                    modeChangeBuffer[4] = modeChangeBuffer[5]
                    modeChangeBuffer[5] = "G9"

                if avalue > 10:
                    print("pressed appa", avalue)
                    appaChannel.play(A9)

                    window.fill((255,255,255))

                    window.blit(cocoHappy, (20,300))
                    window.blit(daniHappy, (190,250))
                    window.blit(fifiHappy, (340,200))
                    window.blit(gabbyHappy, (490,250))
                    window.blit(appaSad, (630,300))

                    pygame.display.update()
        
                    time.sleep(0.1)

                    modeChangeBuffer[0] = modeChangeBuffer[1]
                    modeChangeBuffer[1] = modeChangeBuffer[2]
                    modeChangeBuffer[2] = modeChangeBuffer[3]
                    modeChangeBuffer[3] = modeChangeBuffer[4]
                    modeChangeBuffer[4] = modeChangeBuffer[5]
                    modeChangeBuffer[5] = "A9"

                if compare(modeChangeBuffer, normalBuffer):
                    mode = NORMAL

        except (KeyboardInterrupt):
            GPIO.cleanup()
            exit()
            
        for event in pygame.event.get():
            if event.type == QUIT:
                    GPIO.cleanup()
                    pygame.quit()
                    break

# Compares the contents of two lists A and B
#   True    if length is the same and A[i] == B[i]
#   False   otherwise

def compare(list1, list2):
    if not len(list1) == len(list2):
        return False
    for i in range(len(list1)):
        if not list1[i] == list2[i]:
            return False
    return True
        
