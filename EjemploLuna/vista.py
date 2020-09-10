import pygame
from pygame.locals import *
import bomberman # La vista conoce al modelo, pero el modelo no a la vista. Vista sólo puede "consultar" al modelo, no debe hacer que ejecute acciones.


class Vista():

    def __init__(self, dimensiones, juego):
        """Esto debería ser implementado como un Singleton.
        Por ahora, ignoramos eso."""
        pygame.init()  # Inicializo.
        self.juego = juego
        self.dimensiones = dimensiones
        self.fondo = None
        self.screen = pygame.display.set_mode(dimensiones)
        self.bomberman = None

        pygame.key.set_repeat(20) # para que procese eventos cuando se mantiene una tecla apretada



    def carga_imagen_fondo(self, direccion_fondo):
        self.fondo = pygame.image.load(direccion_fondo)
        self.screen.blit(self.fondo, [0,0])
    
    def recargar_fondo(self):
        self.screen.blit(self.fondo, [0,0])

    def cargar_imagen_bomberman(self, sprite, pos):
        self.bomberman = pygame.image.load(sprite)
        self.pos_bomberman = pos
        self.screen.blit(self.bomberman, pos)

    def recargar_bomberman(self):
        self.screen.blit(self.bomberman, self.juego.get_posicion_bomberman())