import pygame
class Pantall:
     def __init__(self, screen):
          self.screen = screen
          self.cubo1 = pygame.image.load("../imagenes/piso/1.png")
          self.cubo2 = pygame.image.load("../imagenes/piso/2.png")
          self.cubo3 = pygame.image.load("../imagenes/piso/3.png")
          self.direccion = pygame.image.load("../imagenes/objects/Sign_2.png")
          self.fin = pygame.image.load("../imagenes/objects/Sign_1.png")
          self.arboles = pygame.image.load("../imagenes/objects/Tree_1.png")
          self.arboles2 = pygame.image.load("../imagenes/objects/Tree_2.png")
          self.size_cubo = 128
          self.pantalla_ancho = 1800
          self.pantalla_alto = 893

     def inicio(self):
          for x in range(0, 1800, 128):
               if x % 256:
                    self.screen.blit(self.cubo1,[x,893-128])