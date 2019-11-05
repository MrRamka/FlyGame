from pygame import *


class Coin(sprite.Sprite):
    def __init__(self, x, y):
        super(Coin, self).__init__()
        position = (x, y)
        self.image = image.load('images/entities/coin.png')
        self.original_image = self.image
        self.rect = self.image.get_rect(center=position)
        self.position = Vector2(position)

    def update(self):
        pass

