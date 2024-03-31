import pygame
pygame.init()   #инициализируем pygame

W, H = 640, 480
sc = pygame.display.set_mode((W, H), pygame.DOUBLEBUF | pygame.HWSURFACE)    # есть много свойств для окна, см. справку
pygame.display.set_caption('Hello pyGame')
# pygame.display.set_icon(pygame.image.load('myfile.bmp'))  # устанавливаем иконку

FPS = 60                                    # частота обновления типа задержка
clock = pygame.time.Clock()

# рисуем
# определим цвета (не обязательно но можно для удобства)
WHITE = (255, 255, 255)
BLUE = (0, 0, 100)
RED = (255, 0, 0)

# просто рисуем фигуры
# pygame.draw.rect(sc, WHITE, (10,10,620,460), 2)       # draw есть еще line, aaline, lines, aalines, polygon, circle, ellipse, arc
# pygame.draw.rect(sc, BLUE, (20,20,600,440))
# pygame.draw.lines(sc, WHITE, False, [(30, 30), (70, 30), (50, 90)], 1)
# pygame.draw.lines(sc, WHITE, True, [(590, 30), (550, 30), (570, 90)], 1)
# pygame.display.update()

x = 320
y = 400
speed = 3

flRunning = True
while flRunning:        # главный цикл обработки событий
    for event in pygame.event.get():        # запускаем сканер обработчика осбытий
        if event.type == pygame.QUIT:       # проверка "не закрыли ли мы окно"
#            exit()                          # прерываение работы всего приложения
            pygame.quit()                   # завершить работы модуля pyGame
            flRunning = False

        elif event.type == pygame.MOUSEBUTTONDOWN:
            print("Кнопка: ", event.button, event.pos)
            x = event.pos[0]
            y = event.pos[1]
        elif event.type == pygame.MOUSEMOTION:
            #print("позиция мыши: ", event.pos, event.rel)
            s = 1

    # можно использовать такой вариант для контроля мыши
    # pressed = pygame.mouse.get_pressed()
    # if pressed[0]:
    #    pos = pygame.mouse.get_pos()

    sc.fill(WHITE)

    pos = pygame.mouse.get_pos()
    pygame.mouse.set_visible(False)   # скрыть курсор мыши
    if pygame.mouse.get_focused():
        pygame.draw.circle(sc, BLUE, pos, 5)

    # обработка нажатий клавиш (без эвентов)
    keys = pygame.key.get_pressed()     # получаем состояние клавиатуры тут только основные клавиши shift, ctrl, alt и тд - нету
    if keys[pygame.K_LEFT]:             # проверяем нажатие стрелки лево
        x -= speed
    if keys[pygame.K_RIGHT]:            # проверяем нажатие стрелки право
        x += speed

    pygame.draw.rect(sc, RED, (x, y, 30, 5))
    pygame.display.update()

    clock.tick(FPS)

print('Game Over')
