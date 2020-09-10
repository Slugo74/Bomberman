class bomb:
    def __init__(self, proportions=(10, 10), hurt=25, time=5, pos=[0, 0],
                 sp=None):
        self.dimensions = proportions
        self.damage = hurt
        self.counter = time
        self.position = pos
        self.sprite = sp
        self.explosions = []
        self.hitbox = None

    def getPosition(self):
        return self.position

    def getCounter(self):
        return self.counter

    def setHitbox(self, newHitbox):
        self.hitbox = newHitbox

    def getHitbox(self):
        return self.hitbox

    def setSprite(self, aux):
        self.sprite = aux

    def getSprite(self):
        return self.sprite
