import pygame
pygame.init()
window = pygame.display.set_mode((850, 600))
window.fill((246, 215, 176))

font = pygame.font.SysFont("Impact", 100)
renderedText = font.render("W", True, (223, 31, 45))
window.blit(renderedText, (30, 0))

font = pygame.font.SysFont("Trebuchet MS", 100)
renderedText = font.render("i", True, (43, 55, 132))
window.blit(renderedText, (120, 15))


font = pygame.font.SysFont("Georgia", 100)
renderedText = font.render("t", True, (177, 19, 19))
rotated_text=pygame.transform.rotate(renderedText, 20)
window.blit(rotated_text, (135, 10))

font2=pygame.font.Font("/Users/ronnie/Documents/GitHub/Labs/Fonts/Red.ttf",90)
renderedText = font2.render("H", True, (68, 123, 190))
window.blit(renderedText, (195, 25))


font = pygame.font.SysFont("Verdana", 100)
renderedText = font.render("G", True, (177, 19, 19))
rotated_text=pygame.transform.rotate(renderedText, -20)
window.blit(rotated_text, (275, 0))

font = pygame.font.SysFont("Courier New", 100)
renderedText = font.render("R", True, (43, 55, 132))
window.blit(renderedText, (370, 20))

font = pygame.font.SysFont("Times New Roman", 100)
renderedText = font.render("e", True, (223, 31, 45))
window.blit(renderedText, (430, 16))

font=pygame.font.Font("/Users/ronnie/Documents/GitHub/Labs/Fonts/Red.ttf",75)
renderedText = font.render("A", True, (177, 19, 19))
rotated_text=pygame.transform.rotate(renderedText, 10)
window.blit(rotated_text, (465, 45))

font = pygame.font.SysFont("Impact", 100)
renderedText = font.render("t", True, (43, 55, 132))
window.blit(renderedText, (540, 16))

font=pygame.font.Font("/Users/ronnie/Documents/GitHub/Labs/Fonts/Academy Engraved LET Fonts.ttf",110)
renderedText = font.render("P", True, (177, 19, 19))
rotated_text=pygame.transform.rotate(renderedText, 10)
window.blit(rotated_text, (45, 190))

font=pygame.font.Font("/Users/ronnie/Documents/GitHub/Labs/Fonts/Super.ttf",110)
renderedText = font.render("o", True, (223, 31, 45))
window.blit(renderedText, (110, 180))

font = pygame.font.SysFont("Verdana", 85)
renderedText = font.render("W", True, (177, 19, 19))
window.blit(renderedText, (165, 180))

font = pygame.font.SysFont("Trebuchet MS", 100)
renderedText = font.render("e", True, (43, 55, 132))
window.blit(renderedText, (240, 160))

font=pygame.font.Font("/Users/ronnie/Documents/GitHub/Labs/Fonts/Red.ttf",75)
renderedText = font.render("r", True, (177, 19, 19))
rotated_text=pygame.transform.rotate(renderedText, 20)
window.blit(rotated_text, (285, 205))

font=pygame.font.Font("/Users/ronnie/Documents/GitHub/Labs/Fonts/Red.ttf",100)
renderedText = font.render("C", True, (177, 19, 19))
window.blit(renderedText, (380, 200))

font = pygame.font.SysFont("Courier New", 100)
renderedText = font.render("o", True, (177, 19, 19))
window.blit(renderedText, (450, 190))

font = pygame.font.SysFont("Impact", 90)
renderedText = font.render("M", True, (177, 19, 19))
window.blit(renderedText, (505, 190))

font = pygame.font.SysFont("Times New Roman", 100)
renderedText = font.render("e", True, (177, 19, 19))
rotated_text=pygame.transform.rotate(renderedText, -20)
window.blit(rotated_text, (555, 190))

font2=pygame.font.Font("/Users/ronnie/Documents/GitHub/Labs/Fonts/Red.ttf",90)
renderedText = font2.render("s", True, (68, 123, 190))
window.blit(renderedText, (610, 215))

font2=pygame.font.Font("/Users/ronnie/Documents/GitHub/Labs/Fonts/Racing.ttf",150)
renderedText = font2.render("G", True, (68, 123, 190))
window.blit(renderedText, (15, 350))

font=pygame.font.Font("/Users/ronnie/Documents/GitHub/Labs/Fonts/Red.ttf",75)
renderedText = font.render("r", True, (177, 19, 19))
rotated_text=pygame.transform.rotate(renderedText, 20)
window.blit(rotated_text, (85, 380))

font = pygame.font.SysFont("Impact", 100)
renderedText = font.render("e", True, (223, 31, 45))
window.blit(renderedText, (130, 360))

font=pygame.font.Font("/Users/ronnie/Documents/GitHub/Labs/Fonts/Super.ttf",100)
renderedText = font.render("A", True, (177, 19, 19))
window.blit(renderedText, (190, 370))

font=pygame.font.Font("/Users/ronnie/Documents/GitHub/Labs/Fonts/Academy Engraved LET Fonts.ttf",110)
renderedText = font.render("T", True, (68, 123, 190))
window.blit(renderedText, (240, 380))

font = pygame.font.SysFont("Arial", 120)
renderedText = font.render("R", True, (177, 19, 19))
window.blit(renderedText, (200, 470))

font = pygame.font.SysFont("Times New Roman", 100)
renderedText = font.render("e", True, (177, 19, 19))
window.blit(renderedText, (285, 490))

font2=pygame.font.Font("/Users/ronnie/Documents/GitHub/Labs/Fonts/Red.ttf",90)
renderedText = font2.render("s", True, (68, 123, 190))
window.blit(renderedText, (325, 510))

font=pygame.font.Font("/Users/ronnie/Documents/GitHub/Labs/Fonts/Academy Engraved LET Fonts.ttf",110)
renderedText = font.render("P", True, (177, 19, 19))
window.blit(renderedText, (370, 500))

font2=pygame.font.Font("/Users/ronnie/Documents/GitHub/Labs/Fonts/Racing.ttf",70)
renderedText = font2.render("o", True, (68, 123, 190))
window.blit(renderedText, (430, 525))

font = pygame.font.SysFont("Arial", 100)
renderedText = font.render("n", True, (177, 19, 19))
window.blit(renderedText, (470, 490))

font = pygame.font.SysFont("Courier New", 100)
renderedText = font.render("s", True, (177, 19, 19))
window.blit(renderedText, (515, 495))

font = pygame.font.SysFont("Trebuchet MS", 80)
renderedText = font.render("i", True, (43, 55, 132))
window.blit(renderedText, (565, 510))

font2=pygame.font.Font("/Users/ronnie/Documents/GitHub/Labs/Fonts/Red.ttf",80)
renderedText = font2.render("b", True, (68, 123, 190))
window.blit(renderedText, (587, 520))

font = pygame.font.SysFont("Impact", 80)
renderedText = font.render("i", True, (177, 19, 19))
window.blit(renderedText, (642, 510))

font = pygame.font.SysFont("Times New Roman", 95)
renderedText = font.render("L", True, (177, 19, 19))
window.blit(renderedText, (665, 500))

font2=pygame.font.Font("/Users/ronnie/Documents/GitHub/Labs/Fonts/Red.ttf",80)
renderedText = font2.render("i", True, (68, 123, 190))
window.blit(renderedText, (720, 520))

font2=pygame.font.Font("/Users/ronnie/Documents/GitHub/Labs/Fonts/Racing.ttf",70)
renderedText = font2.render("t", True, (68, 123, 190))
window.blit(renderedText, (745, 530))

font=pygame.font.Font("/Users/ronnie/Documents/GitHub/Labs/Fonts/Academy Engraved LET Fonts.ttf",110)
renderedText = font.render("Y", True, (177, 19, 19))
window.blit(renderedText, (765, 510))

pygame.display.flip()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False