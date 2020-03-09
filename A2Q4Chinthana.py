#import required libraries
import pygame
import sys
import pygame as pg
from pygame.locals import *
from random import randint

def draw_grass(percent, colour, h, n): #creating a function to draw grass
    for i in range(0, n): #so only a set amount of grass will be drawn
        x = randint(0, 800) #grass will be distributed randomly along the x axis
        yoffset = randint(0, percent * 600) #offset the y axis to give the grass dept
        pygame.draw.line(screen, colour, (x, 600-yoffset), (x,600-yoffset-h), 3) #draw the grass

imageDir = input("Enter the directory location, or just leave blank and press enter") #since the images were stored on the usb and not easily uploadable to github,the images will have to be downloaded and the directory must be entere
if not imageDir: #if no directory is entered it will default to F:\\Projects
    imageDir = 'F:\\Projects'

pygame.init() #initialize pygame

# URLs for images #to give credit to the images used
#picnic_url = 'https://www.alexander-rose.co.uk/wp-content/uploads/2016/12/310C.png'
#cloud_url = "https://data2.polantis.com/image1000/data/699/26323/White%20Cloud%207_3D_p.png"
#gazebo_url = "https://lh3.googleusercontent.com/proxy/mutzucoxeFs_dNk-03QWh4f5mTKN8cxCucTqRx04WQnFt9b1Q6c2GgITtAUjIeRX7vkyzun8vl0PV8V1TPPog5aGJVTHngSE4hz6UxI"
#sun_url = "https://lh3.googleusercontent.com/proxy/gG1oWhYct-5M2iTpmDHGnJMPWS4Ab-DE7YCIdyRaNbdGHAjV8KCCskF0sCMpdFTNoOe8cYX-pPclCP3DZWVB_GgeYdGM2hU60y8e0ZmI6hfkybhlYytFyLP1Fm-WbpOPnoEdOWXqGj8iYonPPHrgauCElax7"
#tree_url = "https://www.planetpaper.com/wp-content/uploads/2017/08/corrugated_company_usa_canada_manufacturing_company-1236x1336.png?x38052"

screen = pygame.display.set_mode((800, 600)) #sets the size of the display pygame can run in
running = True # for the while loop later

picnic = pygame.image.load(imageDir + '\\310C.PNG') # location of 'picnic' image
cloud = pygame.image.load(imageDir + '\\cloud.PNG') #location of 'cloud' image
sun = pygame.image.load(imageDir + '\\sun.PNG') #location of 'sun' images
gazebo = pygame.image.load(imageDir + '\\gazebo.PNG') #location of 'gazebo' image
tree = pygame.image.load(imageDir + '\\tree.PNG') #location of 'tree' image

screen.fill((0, 0, 255)) #make the background blue
draw_grass(0.2, (0,255,0),50, 2000) #call the function to draw grass in the lower 20% of the screen
screen.blit(pygame.transform.scale(sun, (150, 150)), (600, 0)) #place the sun image on screen
screen.blit(pygame.transform.scale(cloud, (200, 100)), (400, randint(80, 140))) #place the cloud image on screen in a random location on the top half of the screen to create a new landscape every time the program is started
screen.blit(pygame.transform.scale(cloud, (200, 100)), (600, randint(120, 200))) #place the second cloud image on screen in a random location on the top half of the screen to create a new landscape every time the program is started
screen.blit(pygame.transform.scale(cloud, (200, 100)), (200, randint(60, 100))) #place the third cloud image on screen in a random location on the top half of the screen to create a new landscape every time the program is started
screen.blit(pygame.transform.scale(tree, (300, 300)), (-100, 200)) #place a tree image on screen
screen.blit(pygame.transform.scale(gazebo, (400, 400)), (350, 150)) #place a gazebo image on screen
screen.blit(pygame.transform.scale(picnic, (250, 250)), (100, 350)) #place a picnic table image on screen

pygame.display.flip() #allows part of the screen to be updated

while running: #while loop to keep pygane running
    for event in pygame.event.get(): # removes messages from the queue
        if event.type == pygame.QUIT: #if statement for when pygame closes
            running = False #will cause the program to stop since the loop will end

pygame.quit() #quits pygame