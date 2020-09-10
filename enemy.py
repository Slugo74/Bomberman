class Enemy:
    def __init__(self):
        self.actualPos = [651, 50]
        self.sprite = None
        self.width = 38
        self.length = 40
        self.hitbox = None

    def setHitbox(self, aux):
        self.hitbox = aux

    def getHitbox(self):
        return self.hitbox

    def setSprite(self, image):
        self.sprite = image

    def getSprite(self):
        return self.sprite

    def getPostion(self):
        return self.actualPos
