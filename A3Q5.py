import pygame
import os

print("press left arrow to play")
Car = os.path.join('F:\Projects', 'Car.png')
Finish = os.path.join('F:\Projects', 'Flag.png')
class PlaceImages(object):
    def __init__(self):
        self.car = pygame.image.load(Car)
        self.x = 1500
        self.y = 600
        self.flag = pygame.image.load(Finish)
        self.x2 = 50
        self.y2 = 600

    def leftArrow(self):
        key = pygame.key.get_pressed()
        dist = 1
        if key[pygame.K_LEFT]:
            self.x -= dist
    def draw(self, surface):
        surface.blit(self.car, (self.x, self.y))
        surface.blit(self.flag, (self.x2, self.y2))

    def win(self):
        self.x = self.x
        self.x2 = self.x2
        if self.x < self.x2:
            quit("yay you won the race")



pygame.init()
screen = pygame.display.set_mode((1920, 1080))

PlaceImages = PlaceImages()
clock = pygame.time.Clock()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            running = False



    PlaceImages.leftArrow()
    screen.fill((0,255,0))
    PlaceImages.draw(screen)
    PlaceImages.win()
    pygame.display.update()
    clock.tick(1000)