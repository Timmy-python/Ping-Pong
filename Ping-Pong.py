from pygame import *
font.init()

font1 = font.Font(None, 50)
win1 = font1.render('PLAYER 1 WINS!', True, (255,255,0))
win2 = font1.render("PLAYER 2 WINS!", True, (255,255,0))

speed_x = 5
speed_y = 5

back = (200, 255, 255)
win_width = 600
win_height = 400
window = display.set_mode((win_width,win_height))
display.set_caption('Ping-Pong')
window.fill(back)


class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
        sprite.Sprite.__init__(self)

        self.image = transform.scale(image.load(player_image), (size_x, size_y))
        self.speed = player_speed

        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))



class Player(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < win_height - 150:
            self.rect.y += self.speed

    def update2(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < win_height - 150:
            self.rect.y += self.speed

Ping = Player('racket.png', 0, 200, 50, 150, 5)
Pong = Player('racket.png', 550, 200, 50, 150, 5)
Ball = GameSprite("ball.png", 275, 200, 50, 50, 5)

clock = time.Clock()
FPS = 60
game = True
finish = False

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False

    if Ball.rect.x < 0:
        finish = True
        window.blit(win2, (200,200))

    elif Ball.rect.x > 550:
        finish = True
        window.blit(win1, (200,200))
    
    if finish != True:
        window.fill(back)

        if sprite.collide_rect(Ping, Ball) or sprite.collide_rect(Pong, Ball):
            speed_x *= -1
            speed_y *= 1

        Ball.rect.x += speed_x
        Ball.rect.y += speed_y
    
        if Ball.rect.y > 350 or Ball.rect.y < 0:
            speed_y *= -1

        if Ball.rect.x > 560 or Ball.rect.x < 0:
            speed_x *= -1

        Ping.update()
        Ping.reset()

        Pong.update2()
        Pong.reset()

        Ball.reset()

    display.update()
    clock.tick(FPS)
