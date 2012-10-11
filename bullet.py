from math import sin, cos
import bulletml
import bulletml.bulletyaml
from bulletml.collision import collides_all

from bloodyhell.world.actor import Actor

class Bullet(Actor):
    def __init__(self, position, bullet, level, size=(0.3, 0.3)):
        super(Bullet, self).__init__(
            'bullet', 'bullet', position, size
        )
        self._level = level
        self._bullet = bullet
        self._position = position
        level.add_chunk(self, level.SPRITES)

    def update(self):
        super(Bullet, self).update()
        # TODO : Step()
        # Replace with speed from BulletML

        liste = self._bullet.step()
        
        for bul in liste:
            if bul != self._bullet:
                Bullet(self._position, bullet = bul, level = self._level)
            else:         
                self._bullet = bul

        self.set_x_velocity(cos(self._bullet.direction)*2)
        self.set_y_velocity(sin(self._bullet.direction)*2)

    def on_collision(self, chunk, point):
        print "bullet collided"