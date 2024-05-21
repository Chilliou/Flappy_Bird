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
    global img_flappy
    if pigeon.img_status == 0:
        img_flappy = pygame.image.load("./Flappy_Bird_asset/Game_Objects/yellowbird-downflap.png")
    elif pigeon.img_status == 1:
        img_flappy = pygame.image.load("./Flappy_Bird_asset/Game_Objects/yellowbird-midflap.png")
    else:
        img_flappy = pygame.image.load("./Flappy_Bird_asset/Game_Objects/yellowbird-upflap.png")

    screen.blit(img_flappy,(pigeon.pos_x,pigeon.pos_y))

def drawn_score():
    pos_base_x = 140
    for c in str(pigeon.score):
        match c:
            case '0':
                screen.blit(img_0,(pos_base_x,100))
            case '1':
                screen.blit(img_1,(pos_base_x,100))
            case '2':
                screen.blit(img_2,(pos_base_x,100))
            case '3':
                screen.blit(img_3,(pos_base_x,100))
            case '4':
                screen.blit(img_4,(pos_base_x,100))
            case '5':
                screen.blit(img_5,(pos_base_x,100))
            case '6':
                screen.blit(img_6,(pos_base_x,100))
            case '7':
                screen.blit(img_7,(pos_base_x,100))
            case '8':
                screen.blit(img_8,(pos_base_x,100))
            case '9':
                screen.blit(img_9,(pos_base_x,100))   
            case _:
                print("Error")
                
        pos_base_x += 24

def drawn_end():
    screen.blit(end,(50,200))

def gravity():
    pigeon.pos_y += dt / 15

def velocity():
    for pipe in list_pipe:
        pipe.pos_x -= dt /15

def collision():
    if pigeon.pos_y > 450: #450= niveau du sol ps:le passer en const
        print("Perdu")
        pigeon.game_status = "End"
    for p in list_pipe:
        if (pigeon.pos_x > p.pos_x and pigeon.pos_x < p.pos_x + 52) and (pigeon.pos_y < p.pos_y-80 or pigeon.pos_y > p.pos_y) : 
           print("Perdu")
           pigeon.game_status = "End"


# pygame setup
pygame.init()
screen = pygame.display.set_mode((288, 512))
clock = pygame.time.Clock()
running = True
dt = 0

pigeon = flappy(288/4,512/2)

bg = pygame.image.load("./Flappy_Bird_asset/Game_Objects/background-day.png")
base = pygame.image.load("./Flappy_Bird_asset/Game_Objects/base.png")
end = pygame.image.load("./Flappy_Bird_asset/UI/gameover.png")
start_screen = pygame.image.load("./Flappy_Bird_asset/UI/message.png")

img_0 = pygame.image.load("./Flappy_Bird_asset/UI/Numbers/0.png")
img_1 = pygame.image.load("./Flappy_Bird_asset/UI/Numbers/1.png")
img_2 = pygame.image.load("./Flappy_Bird_asset/UI/Numbers/2.png")
img_3 = pygame.image.load("./Flappy_Bird_asset/UI/Numbers/3.png")
img_4 = pygame.image.load("./Flappy_Bird_asset/UI/Numbers/4.png")
img_5 = pygame.image.load("./Flappy_Bird_asset/UI/Numbers/5.png")
img_6 = pygame.image.load("./Flappy_Bird_asset/UI/Numbers/6.png")
img_7 = pygame.image.load("./Flappy_Bird_asset/UI/Numbers/7.png")
img_8 = pygame.image.load("./Flappy_Bird_asset/UI/Numbers/8.png")
img_9 = pygame.image.load("./Flappy_Bird_asset/UI/Numbers/9.png")




list_pipe = []

flappy_timer = pygame.USEREVENT + 1
pygame.time.set_timer(flappy_timer, 100)

pipe_timer = pygame.USEREVENT + 2
pygame.time.set_timer(pipe_timer, 2000)

score_timer = pygame.USEREVENT + 3
pygame.time.set_timer(score_timer, 2000)

test_pipe = Pipe(288,300)

while running:

    if pigeon.game_status == "Starting":
        screen.blit(bg, (0,0))
        screen.blit(base,(0,450))
        drawn_pigeon()
        screen.blit(start_screen,(50,50))
        
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    pigeon.jump()
                    pigeon.game_status = "Playing"
    
    if pigeon.game_status == "Playing":
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
            
            if event.type == score_timer:
                pigeon.score+=1
        gravity()
        velocity()
        collision()
        drawn_score()
    
    if pigeon.game_status == "End":
        drawn_end()
        
    # flip() the display to put your work on screen
    pygame.display.flip()   


    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(60)

pygame.quit()
