from pygame import *

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
    
    if finish != True:
        window.fill(back)

        Ping.update()
        Ping.reset()

        Pong.update2()
        Pong.reset()

        Ball.reset()

    display.update()
    clock.tick(FPS)
