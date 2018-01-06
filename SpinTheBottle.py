#Spin the bottle
#all of the microbit stuff
from microbit import *
#random number generator
import random

#Actions to perform
actions = [' HUGS ', ' HIGH FIVES ', ' SMILES AT ', ' THUMBS UP ', ' TICKLES ', ' COMPLIMENTS ']
#directional arrows
arrows = [Image.ARROW_N, Image.ARROW_NE, Image.ARROW_E, Image.ARROW_SE, Image.ARROW_S, Image.ARROW_SW, Image.ARROW_W, Image.ARROW_NW]


while True:
    #Shows a smiley face when not playing
    display.show(Image.HAPPY)
    if button_a.was_pressed():
        #Need s random number to spin
        timer = random.randint(10,100)
        #random act of kindness
        act = random.randint(0,len(actions) - 1)
        # need to find out out many past full spins to go
        remainder = timer % len(arrows)
        #floor division 
        rt = timer // len(arrows)
        #zero based for loop to iterate through the number of spins
        for i in range(0, rt - 1):
            for j in range(0, len(arrows) - 1):
                display.show(arrows[j])
                sleep(100) 
        #Spin through the remainders
        for i in range(0,remainder -1):
            display.show(arrows[i])
            sleep(100)
        sleep(2000)
        #Display the action
        display.scroll(actions[act], delay = 95, wait = True)
        #do it again for the recipient
        timer = random.randint(10,100)
        act = random.randint(0,4)
        remainder = timer % len(arrows)
        rt = timer // len(arrows)
        sleep(500)
        for i in range(0, rt - 1):
            for j in range(0, len(arrows) - 1):
                display.show(arrows[j])
                sleep(100) 
        for i in range(0,remainder -1):
            display.show(arrows[i])
            sleep(100)
        sleep(5000)
        #Clear the display
        display.clear()