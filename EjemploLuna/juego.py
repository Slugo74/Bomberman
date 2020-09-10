import controlador
import bomberman


class Juego():
    def __init__(self, nombre_jugador, dimensiones):
        self.nombre = nombre_jugador
        self.dimensiones = dimensiones
        self.bomberman = bomberman.Bomberman(self.nombre)
    
    def es_posicion_valida(self, direccion):
        nueva_pos = self.bomberman.get_nueva_posicion_tentativa(direccion)
        print('nueva_pos', nueva_pos)

        comparacion = [val<self.dimensiones[i] for i,val in enumerate(nueva_pos)]

        print(comparacion[0],comparacion[1],nueva_pos[0]>0,nueva_pos[1]>0)
        return comparacion[0]*comparacion[1]*(nueva_pos[0]>=0)*(nueva_pos[1]>=0)

    def mover_bm(self, direccion):
        self.bomberman.mover(direccion, self.es_posicion_valida(direccion))

    def get_posicion_bomberman(self):
        return self.bomberman.get_posicion()