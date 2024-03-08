import pygame
import Nivel

pygame.init()

pantalla_ancho = 1800
pantalla_alto = 893

size = (pantalla_ancho, pantalla_alto)

screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()

pantalla = Nivel.Pantall(screen)

bg = pygame.image.load('../imagenes/BG.png').convert()

done = False

while not done:
     for event in pygame.event.get():
          if event.type == pygame.QUIT:
               done = True
     screen.blit(bg, (0, 0))
     pantalla.inicio()
     pygame.display.flip()
     clock.tick(15)
pygame.quit()