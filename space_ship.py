from pygame import *

from meteor import Meteor

MOVE_SPEED = 3
WIDTH = 90
HEIGHT = 82


class SpaceShip(sprite.Sprite):
    def __init__(self, x, y):
        super(SpaceShip, self).__init__()
        position = (x, y)
        self.alive = True
        self.image = Surface((WIDTH, HEIGHT), SRCALPHA)
        self.image = image.load('images/ships/enemyBlue1.png')
        self.original_image = self.image
        self.rect = self.image.get_rect(center=position)
        self.position = Vector2(x, y)
        self.direction = Vector2(0, 1)
        self.speed = MOVE_SPEED
        self.angle_speed = 0
        self.angle = 0

    def update(self, items):
        if self.angle_speed != 0:
            self.direction.rotate_ip(self.angle_speed)
            self.angle += self.angle_speed
            self.image = transform.rotate(self.original_image, -self.angle)
            self.rect = self.image.get_rect(center=self.rect.center)
        self.position += self.direction * self.speed
        self.rect.center = self.position
        self.collide(items)

    def die(self):
        # self.direction = Vector2(0, 0)
        # time.wait(1500)
        self.teleport(700, 400)

    def teleport(self, goX, goY):
        self.rect.x = goX
        self.rect.y = goY
        self.position = (goX, goY)
        self.alive = True

    def collide(self, items):
        for i in items:
            for j in i:
                if sprite.collide_rect(self, j):
                    if isinstance(j, Meteor):
                        self.die()
                        self.alive = False
