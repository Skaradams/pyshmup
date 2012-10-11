import os
import sys

import pygame

import bulletml
import bulletml.bulletyaml
from bulletml.collision import collides_all

pygame.display.init()
screen = pygame.display.set_mode([600, 600], pygame.DOUBLEBUF)

filename = os.path.join(os.path.dirname(__file__), 'python-bulletml-2', 'examples', 'boss', '[Guwange]_round_4_boss_eye_ball.xml')
target = bulletml.Bullet()
doc = bulletml.BulletML.FromDocument(open(filename, "rU"))
source = bulletml.Bullet.FromDocument(
    doc, x=150, y=150, target=target, rank=0.5)
                        

red = pygame.Surface([3, 3])
red.fill([255, 0, 0])
green = pygame.Surface([3, 3])
green.fill([0, 255, 0])
blue = pygame.Surface([3, 3])
blue.fill([0, 0, 255])
clock = pygame.time.Clock()
target = bulletml.Bullet()

bullets = dict(red=red, green=green, blue=blue)

active = set([source])
print "lACTIVE"

source.vanished = True

while (True):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            raise SystemExit
    lactive = list(active)
    for obj in lactive:
        new = obj.step()
        active.update(new)
        if (obj.finished
            or not (-50 < obj.x < 350)
            or not (-50 < obj.y < 350)):
            active.remove(obj)
    if lactive:
        collides = collides_all(target, lactive)
    screen.fill([0, 0, 64] if collides else [0, 0, 0] )
    for obj in active:
        try:
            x, y = obj.x, obj.y
        except AttributeError:
            pass
        else:
            if not obj.vanished:
                x *= 2
                y *= 2
                x -= 1
                y -= 1
                bullet = bullets.get(obj.appearance, red)
                screen.blit(bullet, [x, 600 - y])

    pygame.display.flip()
