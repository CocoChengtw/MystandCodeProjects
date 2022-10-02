"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman,
and Jerry Liao.

This project applied the coder 'breakoutgraphics.py' to set the game,
and based on the setting to design how the game actually go.
"""

from campy.gui.events.timer import pause
from breakoutgraphics import BreakoutGraphics

FRAME_RATE = 10         # 100 frames per second
NUM_LIVES = 3			# Number of attempts
bricks = 100


def main():
    """
    Firstly, building up the environment of the game.
    Secondly, setting up the moving ball and the rules of the game.
    Lastly, making sure the ending mark showed.
    """
    global bricks
    graphics = BreakoutGraphics()
    dx = graphics.get_dx()
    dy = graphics.get_dy()

    graphics.move()
    graphics.click()
    num = NUM_LIVES

    while True:
        pause(FRAME_RATE)
        if graphics.key and num > 0:
            pause(FRAME_RATE)
            graphics.ball.move(dx, dy)
            if graphics.ball.x < 0 or graphics.ball.x > graphics.window.width-graphics.ball.width:
                dx = -dx
            if graphics.ball.y < 0:
                dy = -dy
        for i in range(2):
            for j in range(2):
                ob = graphics.window.get_object_at(graphics.ball.x+graphics.ball.width*j, graphics.ball.y+graphics.ball.height*i)
                if ob is not None:
                    if ob.y == graphics.paddle.y:
                        dy = -dy
                    else:
                        graphics.window.remove(ob)
                        bricks -= 1
                        dy = -dy
                break
        if graphics.ball.y > graphics.window.height:
            graphics.key = False
            num -= 1
            graphics.window.add(graphics.ball, x=(graphics.window.width-graphics.ball.width)/2,
                                y=(graphics.window.height-graphics.ball.height)/2)
        if num == 0 or bricks == 0:
            break

    if num == 0:
        graphics.get_lose()
        print('game over:(')
    else:
        graphics.get_win()
        print('you win!')


if __name__ == '__main__':
    main()
