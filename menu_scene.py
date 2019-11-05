import pygame

from game_scene import GameScene
from high_score_scene import HighScore
from name_scene import NameScene
from scene_base import SceneBase
from config import *
from colors import *
from space_ship import SpaceShip


class MenuScene(SceneBase):
    def __init__(self):
        SceneBase.__init__(self)
        self.TITLE_FONT = pygame.font.SysFont(FONT_FAMILY, TITLE_FONT_SIZE)
        self.FONT = pygame.font.SysFont(FONT_FAMILY, FONT_SIZE)
        self.play_button = pygame.Rect(WIN_WIDTH * 5.5 / 10, WIN_HEIGHT * 3 / 5, WIN_WIDTH / 5, WIN_HEIGHT / 10)
        self.high_button = pygame.Rect(WIN_WIDTH * 5.5 / 10, WIN_HEIGHT * 4 / 5, WIN_WIDTH / 5, WIN_HEIGHT / 10)
        self.text = self.TITLE_FONT.render('FLY...', False, pygame.Color(WHITE))
        self.play_text = self.FONT.render('PLAY', False, pygame.Color(WHITE))
        self.high_score_text = self.FONT.render('HIGH', False, pygame.Color(BLUE))
        self.space_ship = pygame.image.load('images/ships/spaceShips_007.png')

    def process_input(self, events, pressed_keys):
        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = event.pos

                if self.play_button.collidepoint(mouse_pos):
                    self.switch_to_scene(NameScene())
                if self.high_button.collidepoint(mouse_pos):
                    self.switch_to_scene(HighScore())

    def update(self):
        pygame.display.update()

    def render(self, screen):
        screen.fill(pygame.Color(BACKGROUND_COLOR))

        screen.blit(self.text, (WIN_WIDTH * 3 / 10, WIN_HEIGHT * 1 / 5))

        # Play button position
        screen.blit(self.play_text, (WIN_WIDTH * 5.5 / 10, WIN_HEIGHT * 3 / 5))

        # High score button
        screen.blit(self.high_score_text, (WIN_WIDTH * 5.5 / 10, WIN_HEIGHT * 4 / 5))

        screen.blit(self.space_ship, (WIN_WIDTH * 2.5 / 10, WIN_HEIGHT * 3 / 5))
