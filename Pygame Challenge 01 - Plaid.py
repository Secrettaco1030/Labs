import pygame

pygame.init()
stripe1=(243,243,243)
#Whtie
stripe2=((37,0,1))
#Mahogany
stripe3=(165,1,4)
#Inferno
stripe4=(252,186,4)
#Amber Flame
stripe5=(115,44,44)

width=600
height=400
screen = pygame.display.set_mode((600, 400))
pygame.display.set_caption("Pygame Test Window")
stripe_width=45
stripe_width2=10
stripe_height=45
stripe_height2=10
gap=80

screen.fill(stripe2)

for x in range(0, width, gap):
    pygame.draw.rect(screen, stripe1, (x,0, stripe_width, height))

for y in range(0, height, gap):
    pygame.draw.rect(screen, stripe4, (0,y, width, stripe_height))
for z in range(0, height, gap):
    pygame.draw.rect(screen, stripe3, (0,z, width, stripe_height2))


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.blit(screen, (0, 0))
    pygame.display.update()
pygame.quit()



