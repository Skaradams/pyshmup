import os
import sys 

sys.path.append(os.path.abspath(
    os.path.join(os.path.dirname(__file__), 'bloodyhell')
))

from sandbox import SandBox

def run():
    import settings

    from bloodyhell.game import Game

    game = Game(
        'test shoot',
        (800, 600),
        os.path.join(os.path.dirname(__file__), 'res'),
        fps=24
    )
    navigator = game.navigator()
    navigator.set_current_view(SandBox())
    game.run()

if __name__ == '__main__':
    run()
