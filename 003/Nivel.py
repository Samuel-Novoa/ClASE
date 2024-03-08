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
          self.arbol = pygame.image.load("../imagenes/objects/Tree_2.png")
          self.size_cubo = 128
          self.pantalla_ancho = 1800
          self.pantalla_alto = 893

     def inicio(self):
          self.screen.blit(self.direccion,[128*0, self.pantalla_alto-self.size_cubo*2+40])
          self.screen.blit(self.cubo1,[128*0, self.pantalla_alto-self.size_cubo])
          self.screen.blit(self.cubo2,[128*1, self.pantalla_alto-self.size_cubo])
          self.screen.blit(self.cubo3,[128*2, self.pantalla_alto-self.size_cubo])

          self.screen.blit(self.cubo1,[128*5, self.pantalla_alto-self.size_cubo])
          self.screen.blit(self.cubo2,[128*6, self.pantalla_alto-self.size_cubo])
          self.screen.blit(self.cubo2,[128*7, self.pantalla_alto-self.size_cubo])
          self.screen.blit(self.arboles,[128*7-60, self.pantalla_alto-self.size_cubo*3])
          self.screen.blit(self.cubo3,[128*8, self.pantalla_alto-self.size_cubo])

          self.screen.blit(self.cubo1,[128*10, self.pantalla_alto-self.size_cubo])
          self.screen.blit(self.arboles,[128*10, self.pantalla_alto-self.size_cubo*3])
          self.screen.blit(self.cubo2,[128*11, self.pantalla_alto-self.size_cubo])
          self.screen.blit(self.cubo2,[128*12, self.pantalla_alto-self.size_cubo])
          self.screen.blit(self.cubo2,[128*13, self.pantalla_alto-self.size_cubo])

          self.screen.blit(self.fin, [128*13, self.pantalla_alto-self.size_cubo*2+40])

          self.screen.blit(self.cubo2,[128*14, self.pantalla_alto-self.size_cubo])