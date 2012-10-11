import os
import sys 
from bloodyhell.world.actor import Actor
from bulletpattern import BulletPattern
from bullet import Bullet


class Ship(Actor):

    def __init__(self, position, size, level=None):
        super(Ship, self).__init__(
            'ship', 'ship', position, size
        )
        self._speed = 4.0

        self._x_vel = 0.0
        self._y_vel = 0.0
        self._bullets = []

        self.listen_key('right')
        self.listen_key('left')
        self.listen_key('up')
        self.listen_key('down')
        self.listen_key('space')
        self._level = level

    def update(self):
        super(Ship, self).update()
        self.set_y_velocity(self._y_vel)
        self.set_x_velocity(self._x_vel)

    def bullets(self):
        return self._bullets

    def on_right_pressed(self):
        self._x_vel = self._speed

    def on_right_released(self):
        self._x_vel = 0.0

    def on_left_pressed(self):
        self._x_vel = -self._speed

    def on_left_released(self):
        self._x_vel = 0.0

    def on_up_pressed(self):
        self._y_vel = self._speed

    def on_up_released(self):
        self._y_vel = 0.0

    def on_down_pressed(self):
        self._y_vel = -self._speed

    def on_down_released(self):
        self._y_vel = 0.0
    
    def on_space_pressed(self):
        (x,y) = self.position()
        # self._bullets.append(Bullet((x+1.0, y)))
        path = os.path.join(os.path.dirname(__file__), 'python-bulletml-2', 'examples', 'normal', 's-fall.xml')
        self._bullets.append(BulletPattern((x+1.0, y), path, self._level))

    def on_space_released(self):
        pass
        
    def on_collision(self, chunk, point):
        pass
