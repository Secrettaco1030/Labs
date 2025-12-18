import pygame
pygame.init()

screen = pygame.display.set_mode((800,600))
clock=pygame.time.Clock()

gameState="Menu"
font=pygame.font.SysFont("Times New Roman", 30)

White=(255,255,255)
Black=(0,0,0)
Grey=(200,200,200)
Dark_Grey=(100,100,100)
Blue=(0,0,255)
Green=(0,255,0)
Pink=(255,0,255)
green_button=pygame.Rect(150,150,200,50)
pink_button=pygame.Rect(150,230,200,50)
black_button=pygame.Rect(150,300,200,50)
back_button=pygame.Rect(510,500,270,50)


running=True
while running:
    mousepressed=False
    mouseX, mouseY = pygame.mouse.get_pos()
    for ev in pygame.event.get():
        if ev.type == pygame.QUIT:
            running = False
        if ev.type == pygame.MOUSEBUTTONUP:
            mousepressed=True


    if gameState=="Menu":
        screen.fill(Blue)
        green_colour= Dark_Grey if green_button.collidepoint(mouseX,mouseY) else Green
        pink_colour= Dark_Grey if pink_button.collidepoint(mouseX,mouseY) else Pink
        black_colour= Dark_Grey if black_button.collidepoint(mouseX,mouseY) else Black
        pygame.draw.rect(screen,pink_colour,pink_button)
        pygame.draw.rect(screen,green_colour,green_button)
        pygame.draw.rect(screen,black_colour,black_button)
        screen.blit(font.render("Main Menu", True, Black),(120,50))
        screen.blit(font.render("Credits", True, Black),(160,160))
        screen.blit(font.render("Settings", True, Black),(160,240))
        screen.blit(font.render("About", True, White),(160,310))

        if mousepressed:
            if green_button.collidepoint(mouseX,mouseY):
                gameState="Credits"
            elif pink_button.collidepoint(mouseX,mouseY):
                gameState="Settings"
            elif black_button.collidepoint(mouseX,mouseY):
                gameState="About"
    elif gameState=="Credits":
        screen.fill(Green)
        back_colour= Dark_Grey if back_button.collidepoint(mouseX,mouseY) else Grey
        pygame.draw.rect(screen,back_colour,back_button)
        screen.blit(font.render("Back to Main Menu", True, Black),(525,510))
        if mousepressed and back_button.collidepoint(mouseX,mouseY):
            gameState="Menu"
    elif gameState=="Settings":
        screen.fill(Pink)
        back_colour= Dark_Grey if back_button.collidepoint(mouseX,mouseY) else Grey
        pygame.draw.rect(screen,back_colour,back_button)
        screen.blit(font.render("Back to Main Menu", True, Black),(525,510))
        if mousepressed and back_button.collidepoint(mouseX,mouseY):
            gameState="Menu"
    elif gameState=="About":
        screen.fill(Black)
        back_colour= Dark_Grey if back_button.collidepoint(mouseX,mouseY) else Grey
        pygame.draw.rect(screen,back_colour,back_button)
        screen.blit(font.render("Back to Main Menu", True, White),(525,510))
        if mousepressed and back_button.collidepoint(mouseX,mouseY):
            gameState="Menu"





    pygame.display.flip()
    clock.tick(60)
pygame.quit()