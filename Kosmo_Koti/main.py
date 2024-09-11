from random import randint

import pygame as pg

pg.mixer.init()

size = (1920, 1020)
screen = pg.display.set_mode(size)
pg.display.set_caption("Kosmo_Koti")


# def move(starship_rect, events):
#     for event in events:
#         # напиши код здесь
#         if event.type == pg.KEYDOWN:
#             if event.key == pg.K_a:
#                 starship_rect.x -= 1
#             if event.key == pg.K_d:
#                 starship_rect.x += 1
#             if event.key == pg.K_q:
#                 starship_rect.x -= 10
#             if event.key == pg.K_e:
#                 starship_rect.x += 10
#     return starship_rect

fps = 10

clock = pg.time.Clock()

small_rect = pg.Rect(20, 20, 50, 50)
big_rect = pg.Rect(size[0] // 2 - 100 // 2, 20, 100, 300)

sound1 = pg.mixer.Sound("1.mp3")
sound2 = pg.mixer.Sound("2.mp3")
sound3 = pg.mixer.Sound("3.mp3")
sound4 = pg.mixer.Sound("4.mp3")
sound5 = pg.mixer.Sound("5.mp3")

while True:

    for event in pg.event.get():
        if event.type == pg.QUIT:
            quit()

        if event.type == pg.KEYDOWN:

            number = randint(1, 5)

            if event.key == pg.K_LEFT:

                if number == 1:
                    sound1.play()
                elif number == 2:
                    sound2.play()
                elif number == 3:
                    sound3.play()
                elif number == 4:
                    sound4.play()
                elif number == 5:
                    sound5.play()

                small_rect.x -= 10

            elif event.key == pg.K_a:

                if number == 1:
                    sound1.play()
                elif number == 2:
                    sound2.play()
                elif number == 3:
                    sound3.play()
                elif number == 4:
                    sound4.play()
                elif number == 5:
                    sound5.play()

                small_rect.x -= 10

            if event.key == pg.K_RIGHT:

                if number == 1:
                    sound1.play()
                elif number == 2:
                    sound2.play()
                elif number == 3:
                    sound3.play()
                elif number == 4:
                    sound4.play()
                elif number == 5:
                    sound5.play()

                small_rect.x += 10

            elif event.key == pg.K_d:

                if number == 1:
                    sound1.play()
                elif number == 2:
                    sound2.play()
                elif number == 3:
                    sound3.play()
                elif number == 4:
                    sound4.play()
                elif number == 5:
                    sound5.play()

                small_rect.x += 10

            if event.key == pg.K_UP:

                if number == 1:
                    sound1.play()
                elif number == 2:
                    sound2.play()
                elif number == 3:
                    sound3.play()
                elif number == 4:
                    sound4.play()
                elif number == 5:
                    sound5.play()

                small_rect.y -= 10

            elif event.key == pg.K_w:

                if number == 1:
                    sound1.play()
                elif number == 2:
                    sound2.play()
                elif number == 3:
                    sound3.play()
                elif number == 4:
                    sound4.play()
                elif number == 5:
                    sound5.play()

                small_rect.y -= 10

            if event.key == pg.K_DOWN:

                if number == 1:
                    sound1.play()
                elif number == 2:
                    sound2.play()
                elif number == 3:
                    sound3.play()
                elif number == 4:
                    sound4.play()
                elif number == 5:
                    sound5.play()

                small_rect.y += 10

            elif event.key == pg.K_s:

                if number == 1:
                    sound1.play()
                elif number == 2:
                    sound2.play()
                elif number == 3:
                    sound3.play()
                elif number == 4:
                    sound4.play()
                elif number == 5:
                    sound5.play()

                small_rect.y += 10

    screen.fill(pg.Color('black'))
#     type = randint(1, 4)
#     if type == 1:
#         pg.draw.circle(screen, pg.Color('red'), (100, 100), 10)
#     if type == 2:
    pg.draw.rect(screen, pg.Color('green'), big_rect)
    pg.draw.rect(screen, pg.Color('orange'), small_rect)

#     if type == 3:
#         pg.draw.polygon(screen, pg.Color('green'), ((150, 170), (450, 70), (30, 20)))
#     if type == 4:
#         pg.draw.ellipse(screen, pg.Color('purple'), (300, 300, 200, 100))

    pg.display.flip()
    clock.tick(fps)

# r = int(input('Введите количество красного: '))
# g = int(input('Введите количество зеленого: '))
# b = int(input('Введите количество голубого: '))
#
# def proverka(r, g, b):
#     if r > g and r > b:
#         print('На космических мышей нападают коты.')
#     elif g > r and g > b:
#         print('На инопланетных котов нападают космические мыши.')
#     elif b > r and b > g:
#         print('Ошибочный сигнал.')
#
# proverka(r, g, b)




