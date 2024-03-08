import pygame

pygame.init()

pantalla_ancho = 1800
pantalla_alto = 893

size = (pantalla_ancho, pantalla_alto)

screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()

bg = pygame.image.load('imagenes/BG.png')

done = False

while not done:
     for event in pygame.event.get():
          if event.type == pygame.QUIT:
               done = True
     screen.blit(bg, (0, 0))
     pygame.display.flip()
     clock.tick(15)
pygame.quit()