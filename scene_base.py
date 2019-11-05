import pygame

from colors import BACKGROUND_COLOR
from config import DISPLAY


class SceneBase:
    def __init__(self):
        self.next = self
        self.bg = pygame.Surface(DISPLAY)
        self.bg.fill(pygame.Color(BACKGROUND_COLOR))

    def process_input(self, event, pressed_keys):
        print("you didn't override this in the child class")

    def update(self):
        print("you didn't override this in the child class")

    def render(self, screen):
        print(" you didn't override this in the child class")

    def switch_to_scene(self, next_scene):
        self.next = next_scene

    def terminate(self):
        self.switch_to_scene(None)
