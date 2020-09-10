import View
import Game
import pygame
import sys
import time
Controls = {'273': [0, -1], '274': [0, 1], '275': [1, 0], '276': [-1, 0]}


class Master:
    def __init__(self):
        # El controlador inicializa el juego
        # y la vista.
        self.counter = 0
        self.dimensions = (700, 700)
        self.game = Game.game(self.dimensions)
        self.view = View.view(self.dimensions, self.game)
        self.mainLoop()

    def mainLoop(self):
        """Es el bucle principal del juego.
        Se termina en caso de que el usuario salga del juego
        o el bomberman muera"""
        main = True
        walls = self.game.getHitboxIWalls()
        while main is True:
            self.counter = float(pygame.time.get_ticks() / 1000)
            main = self.game.checkTime(self.counter)
            self.view.reloadBackground()
            for i in range(self.game.getWallsListLength()):
                self.view.reloadWalls(i)
            self.view.reloadPowerUpBoots()
            self.view.reloadPowerUpBombs()
            # print(self.counter)
            for event in pygame.event.get():
                if event.type == pygame.QUIT: sys.exit()
                # self.juego.mover_bm(event.tevent_name())
                if event.type == pygame.KEYDOWN:  # alguien presionó una tecla
                    # print(pygame.event.event_name(event.type))
                    # print(event.key)
                    if event.key == 32 or event.key in range(273, 277):
                        if event.key == 32:
                            # print('BombasCreadas',
                            #      self.game.())
                            # print('AlmBombas',
                            #       selgetBombsListLengthf.game.getNumberOfBombs())
                            numberOfBombs = self.game.getNumberOfBombs()
                            if self.game.getBombsListLength() < numberOfBombs:
                                self.game.createBomb(self.counter)
                                num = self.game.getBombsListLength()
                                print(num)
                                self.view.loadBomb('bomb.png', (35, 35), num)
                                time.sleep(0.20)
                        else:
                            # print(Controls[str(event.key)])
                            # print(self.game.bomberman.Hitbox)
                            # print(self.game.iWallsList[3].Hitbox)
                            # print(self.game.bomberman.Hitbox.colliderect(self.game.iWallsList[3].Hitbox))
                            # print(collitionAux)
                            auxDir = Controls[str(event.key)]
                            self.game.moveBomberman(auxDir)
            dead = self.game.checkCollitionEnemy(self.counter)
            if dead is True:
                self.view.loadGameOver('gameOver.jpg')
                main = False
                # self.game.bombList.pop(self.game.getListNumber()- 1)
            for bombNumber in range(self.game.getBombsListLength()):
                self.view.reloadBomb(bombNumber)
            for bombNo in range(self.game.getBombsListLength()):
                self.game.explosion(bombNo - 1, self.counter)
            self.view.reloadEnemy()
            self.view.reloadBomberman()
            pygame.display.flip()
        self.view.reloadGameOver('gameOver.jpg')
        sys.exit()


if __name__ == "__main__":
    Master = Master()
