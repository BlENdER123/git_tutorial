# игра реверси

import pygame

WIDTH = 695
HEIGHT = 695

step = WIDTH/10

display = pygame.display.set_mode((WIDTH,HEIGHT))

pygame.display.update()

# загружаем фоновую картинку

bg = pygame.image.load('bg.png')

clock = pygame.time.Clock()

game_end = False

while not game_end:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_end = True

    display.blit(bg, (0,0))
    pygame.display.update()
    
    clock.tick(30)

pygame.quit()
quit()