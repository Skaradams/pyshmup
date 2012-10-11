import os
import sys 

import bulletml
import bulletml.bulletyaml
from bulletml.collision import collides_all

from bloodyhell.game import Game
from bloodyhell.level import Level
from bloodyhell.layer.rect import Rect
from bloodyhell.layer import Layer
from bloodyhell.world.actor import Actor
from bloodyhell.world.fence import Fence
from bloodyhell.world.decoration import Decoration

from ship import Ship

class SandBox(Level):

    def __init__(self):
        RESOLUTION = (800, 600)
        res_width, res_height = RESOLUTION
        super(SandBox, self).__init__(camera_config={
            'target': (5.0, 3.5),
            'width': 15.0,
            'rect': Rect((10, 10), (res_width - 20, res_height - 20)),
            'limits': {'left': 0.0, 'bottom': 0.0,
                       'right': 70.0, 'top': 10.0}
        }, gravity=(0, 0))
        self.listen('quit')
        
        # Add background (filled with skyblue)
        self.add_layer(
            Layer(position=(0, 0), size=RESOLUTION).fill('005656'),
            self.BACKGROUND
        )

        self.loader().load_package('static')
        j1 = 1
        j2 = 5
        for i in range(50):
                self.add_chunk(
                    Fence(
                        (i * 0.49, 2.0 + j1),
                        (0.5, 0.5),
                        'static.brick'
                    ),
                    self.PLATFORM
                )
                self.add_chunk(
                    Fence(
                        (i * 0.49, 2.0 + j2),
                        (0.5, 0.5),
                        'static.brick'
                    ),
                    self.PLATFORM
                )

        # BulletML test
        target = bulletml.Bullet()
        path = os.path.join(os.path.dirname(__file__), 'python-bulletml-2', 'examples', 'normal', 'threefire.xml')
        self._bulletml = bulletml.BulletML.FromDocument(open(path, "rU"))
        source = bulletml.Bullet.FromDocument(
            self._bulletml, x=150, y=150, target=target, rank=0.5)
        self._bullets = [source]
   

        self.loader().load_package('ship')
        self.loader().load_package('bullet')

        self._ship = Ship(position=(1.5, 4.0), size=(1.0, 0.5), level=self)
        self.add_chunk(self._ship, self.SPRITES)

        self.world().camera().watch(self._ship)

    def on_frame(self, delta):
        super(SandBox, self).on_frame(delta)
        # while self._ship.bullets().__len__() > 0:
        #     bullet = self._ship.bullets().pop()

        #     self.add_chunk(bullet, self.SPRITES)
    def on_quit(self, event):
        sys.exit()
