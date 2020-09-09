import pygame
import random

pygame.init()

# create display & run update
width = 640
height = 480
display = pygame.display.set_mode((width, height))

pygame.display.update()
pygame.display.set_caption('Snake game')

#colors
colors = {
    'head' : (0,255,0),
    'tail' : (0,200,0),
    'apple': (255,0,0)
}

size = 10

#position of snake
snake_pos = {
    'x' : width/2-size,
    'y' : height/2-size,
    'x-change' : 0,
    'y-change' : 0
}

#position of apple
apple_pos = {
    "x": round(random.randrange(0, width - size) / 10) * 10,
    "y": round(random.randrange(0, height - size) / 10) * 10,
}

#snake body
snake_body = []

#func to add body to snake
def appendBody():
    snake_body.append([-50,-50])

#movement speed
snake_speed = size

#apple counter
apple_eaten = 0

game_stop = False
clock = pygame.time.Clock()

while not game_stop:
    #game loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_stop = True
        
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                snake_pos['y-change'] = 0
                snake_pos['x-change'] = -snake_speed
            elif event.key == pygame.K_RIGHT:
                snake_pos['y-change'] = 0
                snake_pos['x-change'] = snake_speed
            elif event.key == pygame.K_UP:
                snake_pos['y-change'] = -snake_speed
                snake_pos['x-change'] = 0
            elif event.key == pygame.K_DOWN:
                snake_pos['y-change'] = snake_speed
                snake_pos['x-change'] = 0

    #fill scren
    display.fill((0,0,0))

    #change position snake
    snake_pos['x'] += snake_pos['x-change']
    snake_pos['y'] += snake_pos['y-change']

    # teleport snake if goes beyond borders
    if snake_pos['x'] > width-size:
        snake_pos['x'] = 0
    elif snake_pos['x'] < 0:
        snake_pos['x'] = width
    elif snake_pos['y'] > height-size:
        snake_pos['y'] = 0
    elif snake_pos['y'] < 0:
        snake_pos['y'] = height

    #draw snake-head
    pygame.draw.rect(display, colors['head'], [
        snake_pos['x'],
        snake_pos['y'],
        size,
        size
    ])

    #draw apple
    pygame.draw.rect(display, colors['apple'], [
        apple_pos['x'],
        apple_pos['y'],
        size,
        size
    ])

    #apple counter 
    fontObj = pygame.font.Font('freesansbold.ttf', 20)
    textSurfaceObj = fontObj.render(str(apple_eaten) + ' apples eaten', True, colors['head'])
    textRectObj = textSurfaceObj.get_rect()
    textRectObj.center = (85, 20)

    display.blit(textSurfaceObj, textRectObj)

    #win game
    if apple_eaten == 2:
        display = pygame.display.set_mode((width, height))
        display.fill((255,255,255))
        fontObj1 = pygame.font.Font('freesansbold.ttf', 50)
        textSurfaceObj1 = fontObj1.render('YOU WIN', True, colors['apple'])
        textRectObj1 = textSurfaceObj1.get_rect()
        textRectObj1.center = (width/2, height/2)
        pygame.display.update()
        display.blit(textSurfaceObj1, textRectObj1)
        

    #draw snake body
    for elem in range(len(snake_body)):
        pygame.draw.rect(display, colors['tail'], [
            snake_body[elem][0],
            snake_body[elem][1],
            size,
            size
        ])

    #move snake body
    bodyx = snake_pos['x']
    bodyy = snake_pos['y']
    for elem in range(len(snake_body)):
        _bodyx = snake_body[elem][0]
        _bodyy = snake_body[elem][1]

        snake_body[elem][0] = bodyx
        snake_body[elem][1] = bodyy

        bodyx = _bodyx
        bodyy = _bodyy

    #respawn apple
    if (apple_pos['x'] == snake_pos['x']) and (apple_pos['y'] == snake_pos['y']):
        apple_eaten += 1
        apple_pos = {
            "x": round(random.randrange(0, width - size) / 10) * 10,
            "y": round(random.randrange(0, height - size) / 10) * 10,
        }
        appendBody()

    pygame.display.update()

    clock.tick(30)

#close app, if required
pygame.quit()
quit()

