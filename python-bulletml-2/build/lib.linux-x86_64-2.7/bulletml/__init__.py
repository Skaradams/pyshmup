"""BulletML parser.

BulletML is the Bullet Markup Language. BulletML can describe the
barrage of bullets in shooting games. (For example Progear, Psyvariar,
Gigawing2, G DARIUS, XEVIOUS, ...) This module parses and executes
BulletML scripts in Python. All data structures in it are
renderer-agnostic.

In addition to the standard BulletML XML format, this module supports
an equivalent YAML format. See bulletml.bulletyaml for more details.

Finally, three simple collision routines are provided:
bulletml.overlaps for stationary circles, bulletml.collides for moving
circles, and bulletml.collides_all for one moving circle against many
moving circles.

More information is available at the BulletML homepage,
http://www.asahi-net.or.jp/~cs8k-cyu/bulletml/index_e.html, or the
python-bullet homepage, http://code.google.com/p/python-bulletml/.

Basic Usage:

    from bulletml import Bullet, BulletML
    doc = Bulletml.BulletML.FromDocument(open("test.xml", "rU"))
    player = ...  # On your own here, but it needs x and y fields.
    rank = 0.5    # Player difficulty, 0 to 1
    bullet = Bullet.FromDocument(doc, x, y, target=player, rank=rank)
    bullets = [bullet]
    ...
    for bullet in bullets:
        bullets.extend(bullet.step())
    ...

For drawing, you're on your own, but Bullet instances have a number of
attributes that can be used to influence it.

"""

from bulletml.parser import BulletML
from bulletml.impl import Bullet
from bulletml.collision import overlaps, collides, collides_all

VERSION = (2,)
VERSION_STRING = ".".join(map(str, VERSION))

__all__ = ["VERSION", "VERSION_STRING", "Bullet", "BulletML",
           "overlaps", "collides", "collides_all"]

