import pygame

from scene_base import SceneBase
from config import *
from colors import *


def read_data():
    f = open(SCORE_FILE, 'r')
    arr = []
    for line in f:
        temp = line.split(':')
        temp[1] = int(temp[1])
        arr.append(temp)
    arr = sorted(arr, key=lambda x: x[1], reverse=True)[:10]
    return arr


class HighScore(SceneBase):
    def __init__(self):
        SceneBase.__init__(self)
        self.TITLE_FONT = pygame.font.SysFont(FONT_FAMILY, TITLE_FONT_SIZE)
        self.FONT = pygame.font.SysFont(FONT_FAMILY, FONT_SIZE)
        self.second_font = pygame.font.SysFont(FONT_FAMILY, int(FONT_SIZE * 2 / 4))
        self.back_button = pygame.Rect(WIN_WIDTH * 1 / 10, WIN_HEIGHT * 1 / 10, WIN_WIDTH / 5, WIN_HEIGHT / 10)
        self.back_text = self.FONT.render('back', False, pygame.Color(BLUE))
        self.best_players = read_data()

    def process_input(self, events, pressed_keys):
        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = event.pos
                if self.back_button.collidepoint(mouse_pos):
                    from menu_scene import MenuScene
                    self.switch_to_scene(MenuScene())

    def update(self):
        pygame.display.update()

    def render(self, screen):
        screen.fill(pygame.Color(BACKGROUND_COLOR))

        # Play button position
        screen.blit(self.back_text, (WIN_WIDTH * 1 / 10, WIN_HEIGHT * 1 / 10))
        for i in range(len(self.best_players)):
            current_user = self.second_font.render(
                self.best_players[i][0] + ':  ' + str(self.best_players[i][1]) + '  coins in ' + self.best_players[i][2]
                + ' sec, ' + self.best_players[i][3].replace('\n', ''), False, pygame.Color(WHITE))
            screen.blit(current_user, (WIN_WIDTH * 1 / 10, WIN_HEIGHT * 3 / 10 + i * WIN_HEIGHT * 1 / 15))
