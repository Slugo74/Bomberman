import Master
import character as bMan
import Bomb
import copy
import DestructibleWall
import enemy
import time
import powerUp


class game:
    def __init__(self, proportions):
        self.dimensions = proportions
        self.bomberman = bMan.Bomberman([50, 50])
        self.enemy = bMan.Enemy([651, 50])
        self.moreSpeed = powerUp.PowerUPBoots([661, 200])
        self.moreBombs = powerUp.PowerUPBombs([351, 400])
        self.bombList = []
        self.iWallsList = []
        for b in range(6):
            y = 100 + 100 * b
            for a in range(6):
                x = 100 + 100 * a
                self.iWallsList.append(DestructibleWall.DestructubleWall([x, y],
                                                                         None))

    # Movements

    def validPosition(self, dir):
        """Se fija si la posicion a la que se quiere mover el bomberman
        es valida o no. En caso de no serlo devuelve un 0. En caso de
        si serlo devuelve un 1."""
        newPos = self.bomberman.newPossiblePosition(dir)
        # print('Nueva pos', newPos)
        comparate = [val < self.dimensions[i] for i, val in enumerate(newPos)]
        # print(comparate[0],
        #       comparate[1],
        #       newPos[0] > 50 and newPos[0] < 1160,
        #       newPos[1] > 43 and newPos[1] < 680)
        # print(comparate[0]*comparate[1]*
        #       (newPos[0] >= 50 and newPos[0] <= 1192)*(newPos[1] >= 43))
        return (comparate[0] *
                comparate[1] *
                (newPos[0] >= 35 and newPos[0] <= 660) *
                (newPos[1] >= 42 and newPos[1] <= 660))

    def moveBomberman(self, direction):
        """Recibe la direccion hacia donde se va mover.
        Verifica si se esta chocando con una pared.
        Si no lo hace se mueve normalmente. En caso contrario
        se mueve, pero para el lado contrario.
        Las advertencias han sido debidamente presentadas."""
        # print('Vieja posicion',
        #       self.bomberman.oldPos)
        altDirection = []
        if self.checkCollitions() is False:
            self.bomberman.move(direction, self.validPosition(direction))
            if self.checkCollitionPowerUpBoots() is True:
                print("Hola")
                self.moreSpeed.setExistance(False)
            if self.checkCollitionPowerUpBombs() is True:
                self.moreBombs.setExistance(False)
                print("Chau")
        else:
            for item in (direction):
                altDirection.append(item * -3)
            self.bomberman.move(altDirection, self.validPosition(altDirection))
            time.sleep(0.2)

    # Bomb Methods

    def createBomb(self, timer):
        """Recibe el contador de tiempo. Luego verifica si la cantidad
        de bombas creadas es menor a la cantidad de bomberman puede tener.
        Si es menor, crea una bomba dentro de la lista de bombas
        y pone el contador como argumento."""
        if self.getBombsListLength() < self.getNumberOfBombs():
            self.bombList.append(Bomb.bomb((5, 5), 25, copy.deepcopy(timer),
                                 copy.deepcopy(self.getPositionBomberman())))

    def isBombCreated(self):
        """Verifica que haya bombas creadas en base
        a revisar la logitud de la lista.
        Si las hay, devuelve un True.
        En caso contrario, un False"""
        if len(self.bombList) is not 0:
            return True
        else:
            return False

    def explosion(self, bombNumber, newSeconds):
        """Recibe el numero de la bomba que va a explotar y el tiempo actual de juego.
        Luego llama al metodo de verificar la creacion de bombas.
        Luego, si el contador de la bomba supera o iguala los cinco segundos
        es eliminado de la lista de bombas y devuelve un True.
        En caso contrario devuelve un False"""
        if self.isBombCreated() is True:
            if (newSeconds - self.bombList[bombNumber].getCounter()) >= 5:
                self.bombList.pop(bombNumber)
                return True
            else:
                return False

    # Getters

    def getBombsListLength(self):
        return len(self.bombList)

    def getWallsListLength(self):
        return len(self.iWallsList)

    def getNumberOfBombs(self):
        return self.bomberman.getBombs()

    def getTimeOfBomb(self, bombNumber):
        return self.bombList[bombNumber].getCounter()

    def getPositionBomberman(self):
        return self.bomberman.getActuaPos()

    def getDimensions(self):
        return self.dimensions

    def getHitboxIWalls(self):
        """Crea y devuelve una lista UNICAMENTE
        con la hitbox de las paredesIrrompibles."""
        HitboxList = []
        for i in range(self.getWallsListLength()):
            HitboxList.append(self.iWallsList[i].Hitbox)
        return HitboxList

    # Colisiones

    def checkCollitionEnemy(self, time):
        """Recibe el tiempo transcurrido del juego
        Luego se fija si el bomberman esta en contacto
        con la hitbox del enemigo.En caso de confirmarse,
        devuelve el resultado del metodo 'reduceLife' del
        bomberman. En caso contrario devuelve un None.
        Esta expectante ante los acontecimientos"""
        enemyHitbox = self.enemy.getHitbox()
        if (self.bomberman.getHitbox()).colliderect(enemyHitbox) == 1:
            # print('Choco')
            return self.bomberman.reduceLife(time)
        else:
            return None

    def checkCollitions(self):
        """Se fija si el bomberman esta en contacto
        con una hitbox de una pared, si esto ocurre devuielve un
        true, si no ocurre, devuelve un false"""
        hitboxList = self.getHitboxIWalls()
        for i in range(len(hitboxList)):
            auxHitbox = self.bomberman.getHitbox()
            if auxHitbox.colliderect(hitboxList[i]) == 1:
                return (True)
        return (False)

    def checkContentions(self):
        """Se fija si el bomberman contiene la
        hitbox de una pared, si esto ocurre devuielve un
        true, si no ocurre, devuelve un false"""
        contentionList = self.getHitboxIWalls()
        for i in range(len(contentionList)):
            if self.bomberman.Hitbox.contains(contentionList[i]) == 1:
                return (True)
        return (False)

    def checkCollitionPowerUpBoots(self):
        """Corrobora si el bomberman esta chocandose con el powerup. Si chocan,
        devuelve un True. En caso contrario, devuelve un False"""
        print("Hola")
        if self.bomberman.getHitbox().colliderect(self.moreSpeed.getHitbox()) == 1:
            self.bomberman.changeSpeed(self.moreSpeed.getExistance())
            return True
        else:
            return False

    def checkCollitionPowerUpBombs(self):
        """Corrobora si el bomberman esta chocandose con el powerup Si chocan,
        devuelve un True. En caso contrario, devuelve un False"""
        if self.bomberman.getHitbox().colliderect(self.moreBombs.getHitbox()) == 1:
            self.bomberman.changeStorage(self.moreBombs.getExistance())
            return True
        else:
            return False

    # Contador de tiempo

    def checkTime(self, time):
        """Toma un contador de segundos y confirma si se paso de 300 segundos.
        en caso de que lo haga devuelve un False, sino, un True"""
        if time < 300:
            return True
        else:
            return False
