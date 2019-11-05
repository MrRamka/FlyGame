import pygame

from game_scene import GameScene
from input_box import InputBox
from scene_base import SceneBase
from config import *
from colors import *


class NameScene(SceneBase):
    def __init__(self):
        SceneBase.__init__(self)
        self.FONT = pygame.font.SysFont(FONT_FAMILY, FONT_SIZE)
        self.play_button = pygame.Rect(WIN_WIDTH * 5.5 / 10, WIN_HEIGHT * 3 / 5, WIN_WIDTH / 5, WIN_HEIGHT / 10)
        self.back_button = pygame.Rect(WIN_WIDTH * 2.5 / 10, WIN_HEIGHT * 3 / 5, WIN_WIDTH / 5, WIN_HEIGHT / 10)
        self.play_text = self.FONT.render('PLAY', False, pygame.Color(WHITE))
        self.back_text = self.FONT.render('back', False, pygame.Color(BLUE))
        self.enter_name_text = self.FONT.render('Enter your name', False, pygame.Color(BLUE))
        self.name_input_form = InputBox(WIN_WIDTH * 2.5 / 10, WIN_HEIGHT * 2 / 5, WIN_WIDTH / 2, WIN_HEIGHT / 10)
        self.hint_text = self.FONT.render('', False, pygame.Color(RED))
        self.blank_from = True

    def process_input(self, events, pressed_keys):
        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = event.pos

                if self.play_button.collidepoint(mouse_pos):
                    if self.name_input_form.get_text() != '':
                        self.save()
                        self.switch_to_scene(GameScene())
                        self.blank_from = False
                    else:
                        self.hint_text = self.FONT.render('Enter name!', False, pygame.Color(RED))
                if self.back_button.collidepoint(mouse_pos):
                    from menu_scene import MenuScene
                    self.switch_to_scene(MenuScene())
            self.name_input_form.handle_event(event)

    def update(self):
        pygame.display.update()

    def render(self, screen):
        screen.fill(pygame.Color(BACKGROUND_COLOR))

        # Play button position
        screen.blit(self.play_text, (WIN_WIDTH * 5.5 / 10, WIN_HEIGHT * 3 / 5))

        # Back score button
        screen.blit(self.back_text, (WIN_WIDTH * 2.5 / 10, WIN_HEIGHT * 3 / 5))

        # Enter name text
        screen.blit(self.enter_name_text, (WIN_WIDTH * 2.5 / 10, WIN_HEIGHT * 1 / 5))

        # Hint text
        screen.blit(self.hint_text, (WIN_WIDTH * 2.5 / 10, WIN_HEIGHT * 4 / 5))

        # Draw input form with text
        self.name_input_form.draw(screen)

    def save(self):
        f = open(SCORE_FILE, 'a')
        f.write(self.name_input_form.text + ':')
        f.close()
