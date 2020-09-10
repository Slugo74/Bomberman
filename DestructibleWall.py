class DestructubleWall:
    def __init__(self, place, image):
        self.position = place
        self.sprite = image
        self.x = self.position[0]
        self.y = self.position[1]
        self.width = 45
        self.length = 45
        self.Hitbox = None

    def getPositionWall(self):
        return self.position

    def setSprite(self, image):
        self.sprite = image

    def getSprite(self):
        return self.sprite

    def setHitbox(self, aux):
        self.Hitbox = aux

    def getHitbox(self):
        return self.Hitbox
