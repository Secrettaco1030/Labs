import pygame
pygame.init()
window = pygame.display.set_mode((800, 600))
window.fill((186, 217, 181))

font = pygame.font.SysFont("Arial", 20)
renderedText = font.render("Hello World!", True, (89, 0, 0))
window.blit(renderedText, (50, 50))

pygame.display.flip()

