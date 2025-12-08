import pygame

pygame.init()

stripe1=(255,238,169)
#light yellow
stripe2=((255,190,120))
#light orange
stripe3=(255,125,41)
#orange
stripe4=(37,57,0)
#brown
width=600
height=400
screen = pygame.display.set_mode((600, 400))
pygame.display.set_caption("Pygame Test Window")
stripe_width=45
gap=80

screen.fill(stripe4)

for x in range(0, width, gap):
    pygame.draw.rect(screen, stripe2, (x,0, stripe_width, height))




running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.blit(screen, (0, 0))
    pygame.display.update()
pygame.quit()



