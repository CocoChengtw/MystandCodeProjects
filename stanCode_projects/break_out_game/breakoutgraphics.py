"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman, 
and Jerry Liao.

This project is to write the elements and systems which the game needs,
including the window, bricks, a paddle, and other pre-settings.
"""
from campy.graphics.gwindow import GWindow
from campy.graphics.gobjects import GOval, GRect, GLabel
from campy.gui.events.mouse import onmouseclicked, onmousemoved
import random

BRICK_SPACING = 5      # Space between bricks (in pixels). This space is used for horizontal and vertical spacing
BRICK_WIDTH = 40       # Height of a brick (in pixels)
BRICK_HEIGHT = 15      # Height of a brick (in pixels)
BRICK_ROWS = 10        # Number of rows of bricks
BRICK_COLS = 10        # Number of columns of bricks
BRICK_OFFSET = 50      # Vertical offset of the topmost brick from the window top (in pixels)
BALL_RADIUS = 10       # Radius of the ball (in pixels)
PADDLE_WIDTH = 75      # Width of the paddle (in pixels)
PADDLE_HEIGHT = 15     # Height of the paddle (in pixels)
PADDLE_OFFSET = 50     # Vertical offset of the paddle from the window bottom (in pixels)
INITIAL_Y_SPEED = 7    # Initial vertical speed for the ball
MAX_X_SPEED = 5        # Maximum initial horizontal speed for the ball


class BreakoutGraphics:

    def __init__(self, ball_radius=BALL_RADIUS, paddle_width=PADDLE_WIDTH, paddle_height=PADDLE_HEIGHT,
                 paddle_offset=PADDLE_OFFSET, brick_rows=BRICK_ROWS, brick_cols=BRICK_COLS, brick_width=BRICK_WIDTH,
                 brick_height=BRICK_HEIGHT, brick_offset=BRICK_OFFSET, brick_spacing=BRICK_SPACING, title='Breakout'):

        # Create a graphical window, with some extra space
        window_width = brick_cols * (brick_width + brick_spacing) - brick_spacing
        window_height = brick_offset + 3 * (brick_rows * (brick_height + brick_spacing) - brick_spacing)
        self.window = GWindow(width=window_width, height=window_height, title=title)

        # Create a paddle
        self.paddle = GRect(paddle_width, paddle_height, x=(self.window.width-paddle_width)/2, y=self.window.height
                                                                                                 - paddle_offset)
        self.paddle.filled = True
        self.window.add(self.paddle)

        # Center a filled ball in the graphical window
        self.ball = GOval(ball_radius*2, ball_radius*2, x=(self.window.width-ball_radius*2)/2,
                          y=(self.window.height-ball_radius*2)/2)
        self.ball.filled = True
        self.window.add(self.ball)

        # Create the key of clicking mouse to start
        self.key = False

        # Create the speed variance
        self.__dy = INITIAL_Y_SPEED
        self.__dx = random.randint(1, MAX_X_SPEED)
        if random.random() > 0.5:
            self.__dx = -self.__dx

        # Create the ending mark elements
        self.endmark = GRect(240, 80)
        self.endmark.filled = True
        self.endmark.fill_color = 'white'
        self.endmark.color = 'black'
        self.win = GLabel('You Win!')
        self.lose = GLabel('Game Over:(')

        # Draw bricks
        for i in range(brick_rows):
            for j in range(brick_cols):
                self.brick = GRect(brick_width, brick_height)
                self.brick.filled = True
                if i < 2:
                    self.brick.fill_color = 'red'
                elif i < 4:
                    self.brick.fill_color = 'orange'
                elif i < 6:
                    self.brick.fill_color = 'yellow'
                elif i < 8:
                    self.brick.fill_color = 'green'
                else:
                    self.brick.fill_color = 'blue'
                self.window.add(self.brick, x=(brick_width + brick_spacing) * j,
                                y=(brick_height + brick_spacing) * i + brick_offset)

    # Default initial velocity for the ball
    def get_dy(self):
        return self.__dy

    def get_dx(self):
        return self.__dx

    @staticmethod
    def __dy():
        return INITIAL_Y_SPEED

    # Initialize our mouse listeners
    def click(self):
        onmouseclicked(self.start)

    def move(self):
        onmousemoved(self.mouse)

    def start(self, m):
        self.key = True

    def mouse(self, m):
        if m.x <= self.paddle.width // 2:
            self.paddle.x = 0
        elif m.x >= self.window.width - self.paddle.width:
            self.paddle.x = self.window.width - self.paddle.width
        else:
            self.paddle.x = m.x - self.paddle.width // 2

    # If the player win the game, then show the win mark
    def get_win(self):
        self.window.add(self.endmark, x=(self.window.width-self.endmark.width)/2,
                        y=(self.window.height-self.endmark.height)/2)
        self.win.font = '-40'
        self.window.add(self.win, x=(self.window.width-self.win.width)/2,
                        y=(self.window.height-self.endmark.height)/2+60)

    # If the player lose the game, then show the lose mark
    def get_lose(self):
        self.window.add(self.endmark, x=(self.window.width-self.endmark.width)/2,
                        y=(self.window.height-self.endmark.height)/2)
        self.lose.font = '-40'
        self.window.add(self.lose, x=(self.window.width-self.lose.width)/2,
                        y=(self.window.height-self.endmark.height)/2+60)

