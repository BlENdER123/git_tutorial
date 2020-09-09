import pygame
import random

#display info
width = 640
height = 480

#frames per second
fps = 30

# init colors
colors = {
    'white' : (255,255,255),
    'black' : (0,0,0),
    'red' : (255,0,0),
    'green' : (0,255,0),
    'blue' : (0,0,255)
}

#params of snake
snake_size = 10
snake_speed = snake_size

#snake class
class Snake(pygame.sprite.Sprite):
    def __init__(self):
        #unknown command
        pygame.sprite.Sprite.__init__(self)
        
        #params of snake in class
        self.image = pygame.Surface((snake_size, snake_size))
        self.image.fill(colors['red'])

        #draw snake
        self.rect = self.image.get_rect()
        self.rect.center = (width / 2, height / 2)
    
    def update(self):

        keystate = pygame.key.get_pressed()

        # if(keystate[pygame.K_LEFT]):
        #     self.rect.x += -snake_speed


#make window 
pygame.init()
#unknown
pygame.mixer.init()
#make window
screen = pygame.display.set_mode((width, height))
#name of the game
pygame.display.set_caption('Remake snkae with Class')
#unknown
clock = pygame.time.Clock()
# unknowm sprites
all_sprites = pygame.sprite.Group()
#make a new class of snake
snake = Snake()
#unknown
all_sprites.add(snake)

#cycle of game
running = True
while running:
    #optimaze fps
    clock.tick(fps)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                snake.rect.x += -snake_speed

        # здесь код передвижения


        all_sprites.update()

        screen.fill(colors['black'])
        all_sprites.draw(screen)

        pygame.display.flip()


pygame.quit()