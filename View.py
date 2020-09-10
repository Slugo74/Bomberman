import pygame
from pygame.locals import *
import character
import copy


class view:
    def __init__(self, proportions, play):
        pygame.init()
        self.game = play
        self.dimension = proportions
        self.map = None
        self.screen = pygame.display.set_mode(proportions)
        self.experimentalWall = None
        self.backgroundImage('mapaPosta.png')
        self.loadBomberman('bmsprite.png', (60, 60))
        self.loadEnemy('moneda 1.png', (50, 50))
        for i in range(self.game.getWallsListLength()):
            self.loadWalls('azu.png', i)
        self.loadPowerUpBoots('powerSpeed.png', (30, 30))
        self.loadPowerUpBombs('powerBomb.png', (30, 30))

        pygame.key.set_repeat(1)

    def backgroundImage(self, mapDirection):
        """Recibe una imagen, la cual carga como fondo del juego"""
        self.map = pygame.image.load(mapDirection)
        self.map = pygame.transform.scale(self.map,
                                          self.game.getDimensions())
        self.screen.blit(self.map, [0, 0])

    def reloadBackground(self):
        """Recarga la imagen del fondo previamente definida"""
        self.screen.blit(self.map, [0, 0])

    def loadWalls(self, imageDirecton, num):
        """Toma la lista de paredes irrompibles del Game y,
        con una imagen definida,
        las carga por encima del fondo"""
        self.game.iWallsList[num].setSprite(pygame.image.load(imageDirecton))
        self.game.iWallsList[num].setSprite(pygame.transform.scale(self.game.iWallsList[num].getSprite(),
                                                                   (50, 50)))
        auxPosition = self.game.iWallsList[num].getPositionWall()
        rectSprite = pygame.Surface.get_rect(self.game.iWallsList[num].getSprite(),
                                             center=auxPosition)
        self.game.iWallsList[num].setHitbox(pygame.Rect(rectSprite))
        self.screen.blit(self.game.iWallsList[num].getSprite(), rectSprite)
        return None

    def reloadWalls(self, num):
        """Vuelve a cargar las paredes."""
        auxImage = self.game.iWallsList[num].getSprite()
        auxPosition = self.game.iWallsList[num].getPositionWall()
        rectSprite = pygame.Surface.get_rect(auxImage, center=auxPosition)
        self.game.iWallsList[num].setHitbox(pygame.Rect(rectSprite))
        # pygame.draw.rect(self.screen, (255, 0, 0),
        #                  self.game.iWallsList[num].Hitbox, 2)
        self.screen.blit(auxImage, rectSprite)

    def loadBomberman(self, sprite, position):
        """Recibe la imagen a cargar y la posicion, y carga el bomberman"""
        self.game.bomberman.setSprite(pygame.image.load(sprite))
        ch = self.game.bomberman.getSprite()
        self.game.bomberman.sprite = pygame.transform.scale(ch, (40, 40))
        rectSprite = pygame.Surface.get_rect(self.game.bomberman.getSprite(),
                                             center=position)
        self.game.bomberman.setHitbox(rectSprite)
        self.screen.blit(self.game.bomberman.sprite, rectSprite)

    def reloadBomberman(self):
        """Vuelve a cargar el bomberman"""
        auxPos = self.game.getPositionBomberman()
        rectSprite = pygame.Surface.get_rect(self.game.bomberman.getSprite(),
                                             center=auxPos)
        self.game.bomberman.setHitbox(pygame.Rect(rectSprite))
        pygame.draw.rect(self.screen, (255, 0, 0),
                         self.game.bomberman.getHitbox(), 2)
        self.screen.blit(self.game.bomberman.getSprite(),
                         rectSprite)

    def loadBomb(self, sprite, proportions, num):
        """Toma una imagen, las proporciones y el numero de la bomba
        y la carga"""
        num = num - 1
        self.game.bombList[num].setSprite(pygame.image.load(sprite))
        bl = self.game.bombList[num].getSprite()
        self.game.bombList[num].setSprite(pygame.transform.scale(bl,
                                                                 proportions))
        p = self.game.getPositionBomberman()
        positionRect = pygame.Surface.get_rect(self.game.bombList[num].getSprite(),
                                               center=p)
        self.game.bombList[num].setHitbox(positionRect)
        pygame.draw.rect(self.screen, (255, 0, 0),
                         self.game.bombList[num].getHitbox(),
                         2)
        self.screen.blit(self.game.bombList[num].getSprite(), positionRect)

    def reloadBomb(self, num):
        """Vuelve a cargar una bomba. Para diferenciar cual,
        recibe un numero"""
        if self.game.isBombCreated() is not False:
            p = self.game.bombList[num].position
            p_rect = pygame.Surface.get_rect(self.game.bombList[num].sprite,
                                             center=p)
            pygame.draw.rect(self.screen, (255, 0, 0),
                             self.game.bombList[num].getHitbox(),
                             2)
            self.screen.blit(self.game.bombList[num].sprite, p_rect)

    def loadEnemy(self, sprite, proportions):
        """Tomando una imagen y sus proporciones, carga al enemigo"""
        self.game.enemy.setSprite(pygame.image.load(sprite))
        auxSprite = self.game.enemy.getSprite()
        self.game.enemy.setSprite(pygame.transform.scale(auxSprite,
                                                         proportions))
        Hitbox = pygame.Surface.get_rect(self.game.enemy.getSprite(),
                                         center=self.game.enemy.getActuaPos())
        self.game.enemy.setHitbox(Hitbox)
        self.screen.blit(self.game.enemy.getSprite(), Hitbox)

    def reloadEnemy(self):
        """Recarga al enemigo"""
        Hitbox = pygame.Surface.get_rect(self.game.enemy.getSprite(),
                                         center=self.game.enemy.getActuaPos())
        self.game.enemy.setHitbox(Hitbox)
        pygame.draw.rect(self.screen, (255, 0, 0),
                         self.game.enemy.getHitbox(), 2)
        self.screen.blit(self.game.enemy.getSprite(),
                         self.game.enemy.getHitbox())

    def loadFire(self, posBomb, scale, image):
        return None

    def getViewListLength(self):
        return len(self.bomb)

    def loadGameOver(self, image):
        """Toma una imagen. Dicha imagen
        es cargada como el 'GameOver' del juego"""
        gameOver = pygame.image.load(image)
        gameOver = pygame.transform.scale(gameOver, self.dimension)
        self.screen.blit(gameOver, [0, 0])

    def reloadGameOver(self, image):
        """Vuelve a cargar la imagen del 'GameOver'"""
        gameOver = pygame.image.load(image)
        gameOver = pygame.transform.scale(gameOver, self.dimension)
        self.screen.blit(gameOver, [0, 0])

    def loadPowerUpBoots(self, image, proportions):
        """Toma una imagen y sus proporciones y, en base a eso,
        carga el powerup de aumento de velocidad"""
        sprite = pygame.image.load(image)
        sprite = pygame.transform.scale(sprite, proportions)
        self.game.moreSpeed.setSprite(sprite)
        posPower = self.game.moreSpeed.getPosition()
        rectSprite = pygame.Surface.get_rect(self.game.moreSpeed.getSprite(),
                                             center=posPower)
        self.game.moreSpeed.setHitbox(rectSprite)
        pygame.draw.rect(self.screen, (255, 0, 0), rectSprite, 2)
        self.screen.blit(sprite, rectSprite)

    def reloadPowerUpBoots(self):
        """Recarga el powerup de aumento de velocidad"""
        if self.game.moreSpeed.getExistance() is False:
            return None
        auxSprite = pygame.Surface.get_rect(self.game.moreSpeed.getSprite(),
                                            center=self.game.moreSpeed.getPosition())
        self.game.moreSpeed.setHitbox(auxSprite)
        pygame.draw.rect(self.screen, (255, 0, 0),
                         self.game.moreSpeed.getHitbox(), 2)
        self.screen.blit(self.game.moreSpeed.getSprite(),
                         self.game.moreSpeed.getHitbox())

    def loadPowerUpBombs(self, image, proportions):
        """Toma una imagen y sus proporciones y, en base a eso,
        carga el powerup de aumento de bombas"""
        sprite = pygame.image.load(image)
        sprite = pygame.transform.scale(sprite, proportions)
        self.game.moreBombs.setSprite(sprite)
        posPower = self.game.moreBombs.getPosition()
        rectSprite = pygame.Surface.get_rect(self.game.moreBombs.getSprite(),
                                             center=posPower)
        self.game.moreBombs.setHitbox(rectSprite)
        pygame.draw.rect(self.screen, (255, 0, 0), rectSprite, 2)
        self.screen.blit(sprite, rectSprite)

    def reloadPowerUpBombs(self):
        """Recarga el powerup de aumento de bombas"""
        if self.game.moreBombs.getExistance() is False:
            return None
        auxSprite = pygame.Surface.get_rect(self.game.moreBombs.getSprite(),
                                            center=self.game.moreBombs.getPosition())
        self.game.moreBombs.setHitbox(auxSprite)
        pygame.draw.rect(self.screen, (255, 0, 0),
                         self.game.moreBombs.getHitbox(), 2)
        self.screen.blit(self.game.moreBombs.getSprite(),
                         self.game.moreBombs.getHitbox())

    def checkBombSuperposition(self):
        return None
