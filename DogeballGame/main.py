import pygame as pg
import math, random
pg.init()

clock = pg.time.Clock()

scrHeight = 600
scrWidth = 800

display = pg.display.set_mode((scrWidth, scrHeight))
pg.display.set_caption("Dodgeball Ultimate")
pg.mouse.set_visible(False)

icon = pg.image.load("Assets/Sprites/Icons/dodgeball.png")
pg.display.set_icon(icon)

dodgeballs = 0
dodgeballTextColor = (0, 0, 0)

class Crosshair(pg.sprite.Sprite):
    def __init__(self, picture_path):
        super().__init__()
        self.image = pg.image.load(picture_path)
        self.rect = self.image.get_rect()

    def shoot(self):
        pg.sprite.spritecollide(crosshair, dodgeball_group, True)
        
    def update(self):
        self.rect.center = pg.mouse.get_pos()

class dodgeball_counter(object):
    def __init__(self, x, y):
        self.font = pg.font.Font("Fonts/FROSTBITE.ttf", 20)
        self.x = x
        self.y = y

    def draw(self, display):
        display.blit(self.font.render("Dodgeballs: " + str(dodgeballs), False, dodgeballTextColor), (self.x, self.y))

class player(object):
    def __init__(self, x, y, width, height, radius):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.radius = radius
        self.color = (255, 0, 0)
        self.vel = 5
        self.hitbox = (self.x - 20, self.y - 20, 40, 40)

    def draw(self, display):
        pg.draw.circle(display, self.color, (self.x, self.y), self.radius)

class player2(object):
    def __init__(self, x, y, width, height, radius):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.radius = radius
        self.color = (255, 0, 0)
        self.vel = 5

class balls(pg.sprite.Sprite):
    def __init__(self, picture_path, x, y):
        super().__init__()
        self.image = pg.image.load(picture_path)
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.rect.center = [x, y]

def redrawGameWindow():
    display.fill((10, 145, 135))

    dodgeball_group.draw(display)

    man.draw(display)
    man_keys.draw(display)

    crosshair_group.draw(display)
    crosshair_group.update()

    dodgeballCounter.draw(display)

    pg.draw.line(display, (255, 255, 255), (scrWidth / 2, 0), (scrWidth / 2, 600), 10)

    pg.display.update()
    pg.display.flip()

# Man
man = player(430, 300, 20, 20, 15)
man_keys = player(170, 300, 20, 20, 15)

# Dodgeball Counter
dodgeballCounter = dodgeball_counter(620, 15)

# Crosshair
crosshair = Crosshair("Assets/Sprites/Images/crosshair.png")
crosshair_group = pg.sprite.Group()
crosshair_group.add(crosshair)

# Dodgeball
dodgeball_group = pg.sprite.Group()
new_dodgeball = balls("Assets/Sprites/Images/dodgeball_game.png", random.randint(0, scrWidth), random.randint(0, scrHeight))
dodgeball_group.add(new_dodgeball)

# mainloop
running = True
while running:
    clock.tick(60)
    
    mouseX, mouseY = pg.mouse.get_pos() 

    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

        if event.type == pg.MOUSEBUTTONDOWN:
            if event.button == 1:
                if mouseX > new_dodgeball.x - 17 and mouseX < new_dodgeball.x + 17 and mouseY < new_dodgeball.y + 20 and mouseY > new_dodgeball.y - 20:                
                    crosshair.shoot()
                    dodgeballs += 1
                    new_dodgeball.y += 1000
                    new_dodgeball.x += 1000                        

    keys = pg.key.get_pressed()

    if keys[pg.K_a] and man.x > scrWidth / 2 + 18:
        man.x -= man.vel
    else:
        man.x += 0

    if keys[pg.K_d] and man.x < scrWidth - 10:
        man.x += man.vel
    else:
        man.x += 0

    if keys[pg.K_w] and man.y > 10:
        man.y -= man.vel
    else:
        man.y -= 0

    if keys[pg.K_s] and man.y < scrHeight - 10:
        man.y += man.vel
    else:
        man.y += 0

    if keys[pg.K_LEFT] and man_keys.x > 10:
        man_keys.x -= man_keys.vel
    else:
        man_keys.x -= 0

    if keys[pg.K_RIGHT] and man_keys.x < scrWidth / 2 - 15:
        man_keys.x += man_keys.vel
    else:
        man_keys.x += 0

    if keys[pg.K_UP] and man_keys.y > 10:
        man_keys.y -= man_keys.vel
    else:
        man_keys.y -= 0

    if keys[pg.K_DOWN] and man_keys.y < scrHeight - 10:
        man_keys.y += man_keys.vel
    else:
        man_keys.y += 0

    redrawGameWindow()
pg.quit()