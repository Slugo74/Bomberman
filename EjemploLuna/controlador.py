import vista
import juego
import pygame
import sys

CONTROLES = {'273': [0, -1], '274': [0, 1], '275': [1, 0], '276': [-1, 0], }

class Controlador:
    def __init__(self):
        # El controlador inicializa el juego
        # y la vista.
        self.dimensiones = (900, 560)
        self.juego = juego.Juego('Lugogolico', self.dimensiones)
        self.vista = vista.Vista(self.dimensiones, self.juego)

        self.cargar_imagenes()
        self.main_loop()
    
    def main_loop(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT: sys.exit()
                #self.juego.mover_bm(event.tevent_name())
                if event.type==pygame.KEYDOWN: # alguien presionó una tecla
                    print(pygame.event.event_name(event.type))
                    print(event.key)
                    self.juego.mover_bm(CONTROLES[str(event.key)])
                    
                    self.vista.recargar_fondo()

                    self.vista.recargar_bomberman()
                pygame.display.flip()

    def cargar_imagenes(self):
        self.vista.carga_imagen_fondo('/home/ivan/Escritorio/bombermanuranolugosmos/EjemploLuna/grasstexture.jpg')
        self.vista.cargar_imagen_bomberman('/home/ivan/Escritorio/bombermanuranolugosmos/EjemploLuna/bmsprite.png', (2,2))
        return None

if __name__=="__main__":
    controlador = Controlador()
