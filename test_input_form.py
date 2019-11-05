import pygame as pg

from input_box import InputBox

pg.init()
screen = pg.display.set_mode((640, 480))


def main():
    clock = pg.time.Clock()
    input_box1 = InputBox(100, 100, 140, 32)

    done = False

    while not done:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                done = True
            input_box1.handle_event(event)

        screen.fill((30, 30, 30))
        input_box1.draw(screen)

        input_box1.update()
        pg.display.flip()
        clock.tick(30)


if __name__ == '__main__':
    main()
    pg.quit()
