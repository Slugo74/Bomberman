class Character:
    def __init__(self, pos=[60, 50]):
        self.actualPos = pos  # Pos del Bomberman.
        self.sprite = None  # Imagen del bomberman.
        self.Hitbox = None  # Hitbox

    # Getters and Setters

    def getSteps(self):
        return self.steps

    def getActuaPos(self):
        return self.actualPos

    def getBombs(self):
        return self.bombs

    def setHitbox(self, aux):
        self.Hitbox = aux

    def getHitbox(self):
        return self.Hitbox

    def getBombs(self):
        return self.bombs

    def setHitboxTentativa(self, aux):
        self.HitboxTentativa = aux

    def getHitboxTentativa(self):
        return self.HitboxTentativa

    def setHitCounter(self, time):
        self.hitCounter = time

    def getHitCounter(self):
        return self.hitCounter

    def setSprite(self, image):
        self.sprite = image

    def getSprite(self):
        return self.sprite

    def getUsATenInLuna(self):
        """Metodo Supremo. Es el creador de
        todo lo que existió, existe y existira"""
        # return ¿True?


class Enemy(Character):
    def __init__(self, pos):
        super().__init__(pos)


class Bomberman(Character):
    def __init__(self, pos):
        self.actualPos = pos  # Pos del Bomberman.
        self.oldPos = None
        
        self.health = 100  # Vida del bomberman.
        self.bombs = 2  # Capacidad de bombas
        self.steps = 2  # Velocidad.
        self.x = self.actualPos[0]
        self.y = self.actualPos[1]
        self.width = 38
        self.length = 35
        self.Hitbox = None  # Hitbox
        self.hitCounter = 0
    
    def move(self, direction, valid):  # valid es 0 o 1. Si es valid, es 1.
        """Recibe la direccion hacia donde el bomberman se va a mover y un 0 o un 1.
        Si es 0, el bomberman no se mueve.
        Si es uno se mueve hacia la direccion recibida"""
        print('es_valida', valid)
        for index, item in enumerate(self.actualPos):
            self.actualPos[index] = item+valid*self.steps*direction[index]
        self.x = self.actualPos[0]
        self.y = self.actualPos[1]

    def reduceLife(self, time):
        """Recibe el tiempo transcurrido del juego.
        Si pasaron mas de dos segundos desde que el bomberman recibio daño,
        reduce la vida del bomberman. Si su vida llega a cero,
        se muere y devuelve un True. En caso contrario devuelve un False"""
        if time - self.getHitCounter() >= 2:
            self.health = self.health - 50
            print(self.health)
            if self.health <= 0:
                print('verdad')
                self.setHitCounter(time)
                return True
            else:
                print('mentira')
                self.setHitCounter(time)
                return False

    def newPossiblePosition(self, direction):
        """En base a la direccion que tome, devuelve
        la posicion a la que el bomberman se moveria"""
        print('direccion', direction)
        lista_aux = []
        for index, item in enumerate(self.actualPos):
            lista_aux.append(item+self.steps*direction[index])
        self.setHitboxTentativa(lista_aux)
        print(lista_aux)
        return lista_aux

    def changeSpeed(self, cond):
        """Recibe un boolean. En caso de que sea True
        cambia la velocidad del bomberman.
        Cambia la velocidad de movimiento del bomberman"""
        if cond is not False:
            speed = self.getSteps()
            self.steps = speed + 1.5
        return None

    def changeStorage(self, cond):
        """Recibe un boolean. En caso de que sea True
        cambia la capacidad de bombas del bomberman."""
        if cond is not False:
            bombs = self.getBombs()
            self.bombs = bombs + 1
        return None
