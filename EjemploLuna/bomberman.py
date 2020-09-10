class Bomberman:
    def __init__(self, nombre, pos=[0,0]):
        self.posicion_actual = pos
        self.nombre= nombre
        self.step_size = 4 # velocidad

    def mover(self,direccion, es_valida): #es_valida es 0 o 1. Si es valida, es 1
        print('es_valida',es_valida)
        for index,item in enumerate(self.posicion_actual):
            self.posicion_actual[index] = item+es_valida*self.step_size*direccion[index]

    def get_stepsize(self):
        return self.step_size
    
    def get_nueva_posicion_tentativa(self, direccion):
        print('direccion',direccion)
        lista_aux = []
        for index,item in enumerate(self.posicion_actual):
            lista_aux.append(item+self.step_size*direccion[index])
        return lista_aux

    def get_posicion(self):
        return self.posicion_actual