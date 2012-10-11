import bulletml
import bulletml.bulletyaml
from bulletml.collision import collides_all
from bullet import Bullet

class BulletPattern():
    def __init__(self, start_pos, path, level):
        target = bulletml.Bullet()
        self._bulletml = bulletml.BulletML.FromDocument(open(path, "rU"))
        self._source = bulletml.Bullet.FromDocument(
            self._bulletml, x=150, y=150, target=target, rank=0.5)
        self._bullets = []
        self._active = set([self._source])
    
        for bul in list(self._active):
            bullet = Bullet(start_pos, bullet=bul, level = level)
            self._bullets.append(bullet)

        print self._active.__len__()

    def update(self, bullet):
        self._active.update(bullet)

    def active(self):
        return self._active

    def remove(self,bullet):
        self._bullets.remove(bullet)