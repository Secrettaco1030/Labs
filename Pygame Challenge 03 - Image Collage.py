import pygame
import random
pygame.init()

screen = pygame.display.set_mode((800, 600))
background = pygame.image.load('/Users/ronnie/Documents/GitHub/Labs/images/park.jpg')
background = pygame.transform.scale(background, (800, 600))
screen.blit(background, (0, 0))
pygame.display.update()
car1 = pygame.image.load('/Users/ronnie/Documents/GitHub/Labs/images/car2.png')
car1 = pygame.transform.scale(car1, (400, 340))
screen.blit(car1, (200, 230))
pygame.display.update()
car2=pygame.image.load("/Users/ronnie/Documents/GitHub/Labs/images/car3.png")
car2 = pygame.transform.scale(car2, (350, 340))
screen.blit(car2, (500, 250))
pygame.display.update()
car4=pygame.image.load("/Users/ronnie/Documents/GitHub/Labs/images/car4.png")
car4 = pygame.transform.scale(car4, (330, 340))
screen.blit(car4, (-20, 230))

sun_x=random.randrange(40,650)
sun1=pygame.image.load("/Users/ronnie/Documents/GitHub/Labs/images/sun2.png")
sun1 = pygame.transform.scale(sun1, (150, 150))
screen.blit(sun1, (sun_x, 0))
pygame.display.update()

pygame.display.update()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
pygame.quit()