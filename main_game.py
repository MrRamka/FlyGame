import pygame
from config import *
from menu_scene import MenuScene

pygame.font.init()
pygame.init()
screen = pygame.display.set_mode(DISPLAY)
pygame.display.set_caption(GAME_TITLE)
clock = pygame.time.Clock()
done = False
active_scene = MenuScene()
while not done:
    clock.tick(FPS)
    pressed_keys = pygame.key.get_pressed()
    filtered_events = []
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        else:
            filtered_events.append(event)
    active_scene.process_input(filtered_events, pressed_keys)
    active_scene.update()
    active_scene.render(screen)
    active_scene = active_scene.next

    pygame.display.update()
