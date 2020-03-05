import turtle #import turtle library
from random import randint #import random library

def drawStar(t, foreground, background): #make new function called draw star
    t.color(foreground, background) #set the variables for colour
    t.begin_fill() #to fill in the stars that we will draw with a colour
    for i in range(5): # the number of times the below commands will be repeated
        t.forward(75) #moving the pen forward 75 pixels
        t.right(144) #turning the pen at a 144 degree angle
    t.end_fill() #ending the fill of the star we made

def moveToRandomLocation(t): #making new function to move the pen to a random location after every star is drawn
    t.penup() #lifts the pen off so it will not draw when its being moved to its new location
    t.setpos(randint(-400, 400) , randint(-400, 400) ) #setting the new position the pen will go to randomly using 'randint'
    t.pendown()    #putting the pen back down so it can start drawing again
    return None #the function will return nothing

t = turtle.Turtle() #setting t as the turtle variable so we don't have to rewrite it and we can use 't.' for turtle commands
t.speed(0) #setting the speed to very fast
turtle.bgcolor('mediumpurple') #setting the background of the display to purple
colorList = ['blue','green','red','cyan','magenta','yellow','black','white'] #making a list of colours to make the stars later
while True: #while loop to repeat the below commands
    t.pensize(randint(0, 5))  #setting the pensize to a random size between 0 and 5 using 'randint'
    foreIndex = randint(0, len(colorList)-1) #choosing the colour randomly from 'colorList' for the outline of the star, or foreground
    backIndex = randint(0, len(colorList)-1) #choosing the colour randonly from 'colorList' for the inside of the star, or background
    moveToRandomLocation(t) #using the 'moveToRandomLocation' function to move the pen to a different location
    drawStar(t, colorList[foreIndex], colorList[backIndex]) #using the 'drawStar' command to draw the star, and using the forIndex and backIndex to choose the colour for the star

turtle.mainloop() #so the screen won't close in the middle of the program
