from pygame import *

MOVE_SPEED = 2


class Meteor(sprite.Sprite):
    def __init__(self, x, y, dir_x, dir_y):
        super(Meteor, self).__init__()
        position = (x, y)
        self.image = image.load('images/entities/spaceMeteors_001.png')
        self.original_image = self.image
        self.rect = self.image.get_rect(center=position)
        self.position = Vector2(position)
        self.direction = Vector2(dir_x, dir_y)
        self.speed = MOVE_SPEED

    def update(self):
        self.position += self.direction * self.speed
        self.rect.center = self.position
