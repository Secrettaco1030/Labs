import pygame
from pygame.examples.chimp import load_image

pygame.init()
Screen_width = 800
Screen_height = 600
clock=pygame.time.Clock()
screen=pygame.display.set_mode((Screen_width, Screen_height))
layer1 = pygame.image.load("/Users/ronnie/Documents/GitHub/Labs/Images for Layering/sky.png")
layer1=pygame.transform.scale(layer1, (Screen_width, Screen_height))
layer2=pygame.image.load("/Users/ronnie/Documents/GitHub/Labs/Images for Layering/clouds.png")
layer2=pygame.transform.scale(layer2, (Screen_width, Screen_height))

layer3=pygame.image.load("/Users/ronnie/Documents/GitHub/Labs/Images for Layering/far-mountains.png")
layer3=pygame.transform.scale(layer3, (Screen_width, Screen_height))

layer4=pygame.image.load("/Users/ronnie/Documents/GitHub/Labs/Images for Layering/canyon.png")
layer4=pygame.transform.scale(layer4, (Screen_width, Screen_height))

x1_1, x1_2=0, Screen_width
x2_1, x2_2=0, Screen_width
x3_1, x3_2=0, Screen_width
x4_1, x4_2=0, Screen_width

speed1=1
speed2=2
speed3=3
speed4=5

running=True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running=False
    x1_1-=speed1; x1_2-=speed1
    x2_1 -= speed2; x2_2 -= speed2
    x3_1 -= speed3; x3_2 -= speed3
    x4_1 -= speed4; x4_2 -= speed4

    if x1_1 <= -Screen_width: x1_1 = Screen_width
    if x1_2 <= -Screen_width: x1_2 = Screen_width
    if x2_1 <= -Screen_width: x2_1 = Screen_width
    if x2_2 <= -Screen_width: x2_2 = Screen_width
    if x3_1 <= -Screen_width: x3_1 = Screen_width
    if x3_2 <= -Screen_width: x3_2 = Screen_width
    if x4_1 <= -Screen_width: x4_1 = Screen_width
    if x4_2 <= -Screen_width: x4_2 = Screen_width

    screen.blit(layer1, (x1_1, 0))
    screen.blit(layer1, (x1_2, 0))
    screen.blit(layer2, (x2_1,0))
    screen.blit(layer2, (x2_2, 0))
    screen.blit(layer3, (x3_1,0))
    screen.blit(layer3, (x3_2, 0))
    screen.blit(layer4, (x4_1,0))
    screen.blit(layer4, (x4_2, 0))
    pygame.display.update()
    clock.tick(60)
pygame.quit()