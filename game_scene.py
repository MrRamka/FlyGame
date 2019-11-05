import pygame
import datetime
from random import randint

from coin import Coin
from space_ship import SpaceShip
from meteor import Meteor
from scene_base import SceneBase
from config import *
from colors import *


def create_coin():
    x = randint(150, WIN_WIDTH - 150)
    y = randint(150, WIN_HEIGHT - 150)
    return Coin(x, y)


class GameScene(SceneBase):
    def __init__(self):
        SceneBase.__init__(self)
        self.FONT = pygame.font.SysFont(FONT_FAMILY, int(FONT_SIZE / 2))
        self.FONT_2 = pygame.font.SysFont(FONT_FAMILY, FONT_SIZE)
        self.space_ship = SpaceShip(WIN_WIDTH / 2, WIN_HEIGHT / 2)
        self.start_time = datetime.datetime.now()
        self.space_ship_sprite = pygame.sprite.RenderPlain(self.space_ship)
        self.coins = 0

        self.time_text = self.FONT.render(str(self.start_time), False, pygame.Color(BLUE))
        self.best_coin = 0
        self.best_time_text = self.FONT.render(str(self.best_coin), False, pygame.Color(BLUE))
        self.coins_text = self.FONT.render('Coins: ' + str(self.coins), False, pygame.Color(BLUE))
        self.menu_button = pygame.Rect(WIN_WIDTH * 8.5 / 10, WIN_HEIGHT * 8.5 / 10, WIN_WIDTH / 10, WIN_HEIGHT / 10)
        self.menu_button_text = self.FONT.render('MENU', False, pygame.Color(BLUE))

        self.pause_button = pygame.Rect(WIN_WIDTH * 7.5 / 10, WIN_HEIGHT * 8.5 / 10, WIN_WIDTH / 10, WIN_HEIGHT / 10)
        self.pause_button_text = self.FONT.render('PAUSE', False, pygame.Color(WHITE))

        self.continue_button = pygame.Rect(WIN_WIDTH * 5.5 / 10, WIN_HEIGHT * 3 / 5, WIN_WIDTH / 5, WIN_HEIGHT / 10)
        self.menu_pause_button = pygame.Rect(WIN_WIDTH * 2.5 / 10, WIN_HEIGHT * 3 / 5, WIN_WIDTH / 5, WIN_HEIGHT / 10)
        self.continue_button_text = self.FONT_2.render('Continue', False, pygame.Color(WHITE))
        self.menu_pause_button_text = self.FONT_2.render('Menu', False, pygame.Color(WHITE))
        self.dead = False
        self.game_paused = False
        self.current_time = 0
        self.meteors_sprite = []
        self.meteors = []
        self.border_meteors = []
        self.border_meteors_sprite = []
        self.coin_obj = create_coin()
        self.coin_sprite = pygame.sprite.RenderPlain(self.coin_obj)
        self.previous_meteorite_time = 0
        self.best_coin_time = 0
        for i in range(0, WIN_WIDTH, 100):
            inaccuracy = randint(-50, 0)
            self.create_meteorite(i, inaccuracy, 0, 0, True)
            self.create_meteorite(i, WIN_HEIGHT - inaccuracy, 0, 0, True)

        for i in range(0, WIN_HEIGHT, 100):
            inaccuracy = randint(-50, 0)
            self.create_meteorite(inaccuracy, i, 0, 0, True)
            self.create_meteorite(WIN_WIDTH - inaccuracy, i, 0, 0, True)

    def create_meteorite(self, x, y, dir_x, dir_y, border=False):
        meteor = Meteor(x, y, dir_x, dir_y)
        meteor_sprite = pygame.sprite.RenderPlain(meteor)
        if not border:
            self.meteors.append(meteor)
            self.meteors_sprite.append(meteor_sprite)
            # print(self.meteors)
            # print(self.meteors_sprite)
        else:
            self.border_meteors.append(meteor)
            self.border_meteors_sprite.append(meteor_sprite)
            # print(self.border_meteors)
            # print(self.border_meteors_sprite)

    def process_input(self, events, pressed_keys):
        for event in events:
            if not self.game_paused and event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = event.pos
                if self.menu_button.collidepoint(mouse_pos):
                    self.save()
                    self.game_paused = False
                    from menu_scene import MenuScene
                    self.switch_to_scene(MenuScene())
                if self.pause_button.collidepoint(mouse_pos):
                    self.game_paused = True

            if self.game_paused and event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = event.pos
                if self.menu_pause_button.collidepoint(mouse_pos):
                    self.save()
                    self.game_paused = False
                    from menu_scene import MenuScene
                    self.switch_to_scene(MenuScene())
                if self.continue_button.collidepoint(mouse_pos):
                    self.game_paused = False

            if not self.game_paused and event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    self.space_ship.speed += 0
                elif event.key == pygame.K_s:
                    self.space_ship.speed -= 0
                elif event.key == pygame.K_a:
                    self.space_ship.angle_speed = -4
                elif event.key == pygame.K_d:
                    self.space_ship.angle_speed = 4
            elif not self.game_paused and event.type == pygame.KEYUP:
                if event.key == pygame.K_a:
                    self.space_ship.angle_speed = 0
                elif event.key == pygame.K_d:
                    self.space_ship.angle_speed = 0

    def update(self):
        if not self.game_paused:
            if self.space_ship.alive:
                all_meteorites = []
                took = pygame.sprite.spritecollide(self.space_ship_sprite.sprites()[0], self.coin_sprite, True)
                if took:
                    self.coins += 1
                    self.coins_text = self.FONT.render('Coins: ' + str(self.coins), False,
                                                       pygame.Color(BLUE))
                    self.coin_sprite = pygame.sprite.RenderPlain(create_coin())
                for i in self.meteors_sprite:
                    all_meteorites.append(i)
                for i in self.border_meteors_sprite:
                    all_meteorites.append(i)

                self.space_ship_sprite.update(all_meteorites)
                for meteor in self.meteors_sprite:
                    meteor.update()

                self.current_time = datetime.datetime.now() - self.start_time
                self.time_text = self.FONT.render('Time: ' + str(self.current_time.seconds), False,
                                                  pygame.Color(BLUE))
                self.best_time_text = self.FONT.render('Your Best: ' + str(self.best_coin), False,
                                                       pygame.Color(BLUE))

                self.coins_text = self.FONT.render('Coins: ' + str(self.coins), False, pygame.Color(BLUE))

                if int(self.current_time.seconds) - self.previous_meteorite_time >= 1:
                    random_ps = START_POSITION.get(randint(1, AMOUNT_START_POSITION))
                    self.create_meteorite(random_ps[0], random_ps[1], random_ps[2], random_ps[3])
                    self.previous_meteorite_time = self.current_time.seconds

            if not self.space_ship.alive:
                if self.coins > self.best_coin:
                    self.best_coin = self.coins
                    self.best_coin_time = self.current_time.seconds
                self.start_time = datetime.datetime.now()
                while datetime.datetime.now().second - self.start_time.second < END_GAME_TIME:
                    pass
                self.start_time = datetime.datetime.now()
                self.meteors_sprite = []
                self.meteors = []
                self.previous_meteorite_time = 0
                self.coins = 0
                self.space_ship.alive = True

    def render(self, screen):
        screen.fill(pygame.Color(BACKGROUND_COLOR))
        if not self.game_paused:
            self.space_ship_sprite.draw(screen)

            self.coin_sprite.draw(screen)
            # Draw meteors
            for meteor in self.meteors_sprite:
                meteor.draw(screen)
            for meteor in self.border_meteors_sprite:
                meteor.draw(screen)

            screen.blit(self.time_text, (WIN_WIDTH * 1 / 15, WIN_HEIGHT * 1.5 / 15))
            screen.blit(self.coins_text, (WIN_WIDTH * 3 / 15, WIN_HEIGHT * 1.5 / 15))
            screen.blit(self.best_time_text, (WIN_WIDTH * 5 / 15, WIN_HEIGHT * 1.5 / 15))
            screen.blit(self.menu_button_text, (WIN_WIDTH * 8.5 / 10, WIN_HEIGHT * 8.5 / 10))
            screen.blit(self.pause_button_text, (WIN_WIDTH * 7.5 / 10, WIN_HEIGHT * 8.5 / 10))

        else:
            self.space_ship_sprite.draw(screen)
            self.coin_sprite.draw(screen)

            # Draw meteors
            for meteor in self.meteors_sprite:
                meteor.draw(screen)
            for meteor in self.border_meteors_sprite:
                meteor.draw(screen)

            screen.blit(self.time_text, (WIN_WIDTH * 1 / 15, WIN_HEIGHT * 1.5 / 15))
            screen.blit(self.coins_text, (WIN_WIDTH * 3 / 15, WIN_HEIGHT * 1.5 / 15))
            screen.blit(self.best_time_text, (WIN_WIDTH * 5 / 15, WIN_HEIGHT * 1.5 / 15))

            # Continue button position
            screen.blit(self.continue_button_text, (WIN_WIDTH * 5.5 / 10, WIN_HEIGHT * 3 / 5))

            # Menu  button
            screen.blit(self.menu_pause_button_text, (WIN_WIDTH * 2.5 / 10, WIN_HEIGHT * 3 / 5))

    def save(self):
        f = open(SCORE_FILE, 'a')
        f.write(str(self.best_coin) + ':' + str(self.best_coin_time) + ':' + str(datetime.datetime.now().date()) + '\n')
        f.close()
