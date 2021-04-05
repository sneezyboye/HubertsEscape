import pygame as pg
from settings import *
vec = pg.math.Vector2

class Player(pg.sprite.Sprite):
    def __init__(self, game, x, y):
        self.groups = game.all_sprites
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.color = GREEN
        self.image = pg.Surface((TILESIZE, TILESIZE))
        self.image.fill(self.color)
        self.rect = self.image.get_rect()
        self.x = x * TILESIZE
        self.y = y * TILESIZE
        self.gravity = 0
        self.gravity_inc = PLAYER_GRAVITY * self.game.dt
        self.on_floor = False
        self.jumping = False
        self.bounce = False
        self.vy = 0
        self.vx = 0
        self.acy = 0
        self.acx = 0

    def get_keys(self):
        keys = pg.key.get_pressed()
        if keys[pg.K_LEFT] or keys[pg.K_a]:
            self.acx = -PLAYER_ACC
        if keys[pg.K_RIGHT] or keys[pg.K_d]:
            self.acx = PLAYER_ACC
#        if self.vx != 0 and self.vy != 0:
#            self.vx *= 0.7071
#            self.vy *= 0.7071

    def collide_with_walls(self, dir):
        if dir == 'x':
            hits = pg.sprite.spritecollide(self, self.game.walls, False)
            if hits:
                if self.vx > 0:
                    self.x = hits[0].rect.left - self.rect.width
                if self.vx < 0:
                    self.x = hits[0].rect.right
                self.vx = 0
                self.rect.x = self.x

        if dir == 'y':
            hits = pg.sprite.spritecollide(self, self.game.walls, False)
            if hits:
                self.on_floor = True
                self.jumping = False
                if hits[0].type == "bouncy":
                    self.bounce = True
                else:
                    self.bounce = False
                if self.vy > 0:
                    self.y = hits[0].rect.top - self.rect.height
                if self.vy < 0:
                    self.y = hits[0].rect.bottom
                self.vy = 0
                self.rect.y = self.y
            else:
                self.on_floor = False

    def jump(self):
        self.rect.y += 1
        hits = pg.sprite.spritecollide(self, self.game.walls, False)
        self.rect.y -= 1
        if hits:
            self.jumping = True
            self.on_floor = False

    def update(self):
        self.acx = 0
        self.vy = 0
        self.get_keys()
        self.fall()
        if self.bounce == True:
            self.vy += -BOUNCE_SPEED
        elif self.jumping:
            self.vy += -JUMP_SPEED
        self.acx += self.vx * PLAYER_FRICTION
        self.vx += self.acx
        self.y += self.vy * self.game.dt
        self.x += (self.vx + 0.5 * self.acx) * self.game.dt
        self.rect.x = self.x
        self.collide_with_walls('x')
        self.rect.y = self.y
        self.collide_with_walls('y')

    def fall(self):
        if self.on_floor == True:
            self.gravity = 0
        else:
            self.gravity += self.gravity_inc
            #self.gravity_inc += 1
        self.vy += self.gravity

class Wall(pg.sprite.Sprite):
    def __init__(self, game, x, y, type):
        self.groups = game.all_sprites, game.walls
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = pg.Surface((TILESIZE, TILESIZE))
        self.type = type
        if type == "normal":
            self.color = DARKER_WHITE
        if type == "bouncy":
            self.color = LIGHT_BLUE
        self.image.fill(self.color)
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.rect.x = x * TILESIZE
        self.rect.y = y * TILESIZE
        self.type = type
