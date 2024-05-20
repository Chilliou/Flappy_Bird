import pygame
import random

class Pipe:
    def __init__(self, pos_x, pos_y) -> None:
        self.pos_x = pos_x
        self.pos_y = pos_y

class flappy:    
    def __init__(self,pos_x, pos_y) -> None:
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.game_status = "Starting"
        self.score = 0
        self.img_status = 0

    def jump(self):
        self.pos_y -= 30

    def change_image(self):
        if self.img_status == 0:
            self.img_status = 1
        elif self.img_status == 1:
            self.img_status = 2
        else:
            self.img_status = 0

def drawn_pipe(pos_x,pox_y):
    img_pipe = pygame.image.load("./Flappy_Bird_asset/Game_Objects/pipe-green.png")

    screen.blit(img_pipe,(pos_x, pox_y))
    test = pygame.transform.rotate(img_pipe,180)
    screen.blit(test,(pos_x, pox_y-400))

def drawn_pigeon():
    if pigeon.img_status == 0:
        img__flappy = pygame.image.load("./Flappy_Bird_asset/Game_Objects/yellowbird-downflap.png")
    elif pigeon.img_status == 1:
        img__flappy = pygame.image.load("./Flappy_Bird_asset/Game_Objects/yellowbird-midflap.png")
    else:
        img__flappy = pygame.image.load("./Flappy_Bird_asset/Game_Objects/yellowbird-upflap.png")

    screen.blit(img__flappy,(pigeon.pos_x,pigeon.pos_y))

def gravity():
    pigeon.pos_y += dt / 15

def velocity():
    for pipe in list_pipe:
        pipe.pos_x -= dt /15

# pygame setup
pygame.init()
screen = pygame.display.set_mode((288, 512))
clock = pygame.time.Clock()
running = True
dt = 0

pigeon = flappy(288/4,512/2)

bg = pygame.image.load("./Flappy_Bird_asset/Game_Objects/background-day.png")
base = pygame.image.load("./Flappy_Bird_asset/Game_Objects/base.png")

list_pipe = []

flappy_timer = pygame.USEREVENT + 1
pygame.time.set_timer(flappy_timer, 100)

pipe_timer = pygame.USEREVENT + 2
pygame.time.set_timer(pipe_timer, 2000)

test_pipe = Pipe(288,300)

while running:
    
    screen.blit(bg, (0,0))
    
    
    drawn_pigeon()
    for pipe in list_pipe:   
        drawn_pipe(pipe.pos_x,pipe.pos_y)

    screen.blit(base,(0,450))
    
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                pigeon.jump()

        if event.type == pygame.QUIT:
            running = False

        if event.type == flappy_timer:
            pigeon.change_image()

        if event.type == pipe_timer: 
            new_pipe = Pipe(288, 400-random.randrange(100))  # Adjust range for pipe position
            list_pipe.append(new_pipe)


    gravity()
    velocity()
    # flip() the display to put your work on screen
    pygame.display.flip()   


    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(60)

pygame.quit()
