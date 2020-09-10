class PowerUP:
    def __init__(self, place):
        self.sprite = None
        self.position = place
        self.hitbox = None
        self.existance = True

    def setHitbox(self, aux):
        self.hitbox = aux

    def getHitbox(self):
        return self.hitbox

    def setSprite(self, aux):
        self.sprite = aux

    def getSprite(self):
        return self.sprite

    def setPosition(self, aux):
        self.position = aux

    def getPosition(self):
        return self.position

    def setExistance(self, aux):
        self.existance = aux

    def getExistance(self):
        return self.existance


class PowerUPBoots(PowerUP):
    def __init__(self, place):
        self.sprite = None
        self.position = place
        self.hitbox = None
        self.existance = True


class PowerUPBombs(PowerUP):
    def __init__(self, place):
        self.sprite = None
        self.position = place
        self.hitbox = None
        self.existance = True
