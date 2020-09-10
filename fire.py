class Fire:
    def __init__(self, pos, cajaDeGolpes):
        self.position = pos
        self.hitbox = cajaDeGolpes

    def setHitbox(self, aux):
        self.hitbox = aux

    def getHitbox(self):
        return self.hitbox
