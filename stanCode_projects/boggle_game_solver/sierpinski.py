"""
File: sierpinski.py
Name: Coco
---------------------------
This file recursively prints the Sierpinski triangle on GWindow.
The Sierpinski triangle is a fractal described in 1915 by Waclaw Sierpinski.
It is a self similar structure that occurs at different levels of iterations.
"""

from campy.graphics.gwindow import GWindow
from campy.graphics.gobjects import GLine
from campy.gui.events.timer import pause

# Constants
ORDER = 6                  # Controls the order of Sierpinski Triangle
LENGTH = 600               # The length of order 1 Sierpinski Triangle
UPPER_LEFT_X = 150		   # The upper left x coordinate of order 1 Sierpinski Triangle
UPPER_LEFT_Y = 100         # The upper left y coordinate of order 1 Sierpinski Triangle
WINDOW_WIDTH = 950         # The width of the GWindow
WINDOW_HEIGHT = 700        # The height of the GWindow

# Global Variable
window = GWindow(width=WINDOW_WIDTH, height=WINDOW_HEIGHT)  # The canvas to draw Sierpinski Triangle


def main():
	"""
	First, draw the big upsidedown triangle
	Second, depends on the given order number to decide how many level(K) should be
	Third, order K triangle would be consisted of 3 order K-1 triangles
	"""
	l1 = GLine(UPPER_LEFT_X, UPPER_LEFT_Y, UPPER_LEFT_X + LENGTH, UPPER_LEFT_Y)
	l2 = GLine(UPPER_LEFT_X, UPPER_LEFT_Y, UPPER_LEFT_X + (LENGTH / 2), UPPER_LEFT_Y + (LENGTH * 0.866))
	l3 = GLine(UPPER_LEFT_X + LENGTH, UPPER_LEFT_Y, UPPER_LEFT_X + (LENGTH / 2), UPPER_LEFT_Y + (LENGTH * 0.866))
	window.add(l1)
	window.add(l2)
	window.add(l3)
	sierpinski_triangle(ORDER, LENGTH, UPPER_LEFT_X, UPPER_LEFT_Y)


def sierpinski_triangle(order, length, upper_left_x, upper_left_y):
	"""
	:param order: integer, number decided K triangle
	:param length: integer, the length of outer triangle
	:param upper_left_x: integer, the x position of the outer triangle's upper left point
	:param upper_left_y: integer, the y position of the outer triangle's upper left point
	:return: pic, K triangles
	"""
	if order == 1:
		pass
	else:
		l1 = GLine(upper_left_x + (length / 2), upper_left_y, upper_left_x + (length / 2) - (length * 0.25), upper_left_y + (length * 0.433))
		l2 = GLine(upper_left_x + (length / 2), upper_left_y, upper_left_x + (length / 2) + (length * 0.25), upper_left_y + (length * 0.433))
		l3 = GLine(upper_left_x + (length / 2) - (length * 0.25), upper_left_y + (length * 0.433), upper_left_x + (length / 2) + (length * 0.25), upper_left_y + (length * 0.433))
		window.add(l1)
		window.add(l2)
		window.add(l3)
		sierpinski_triangle(order - 1, length / 2, upper_left_x, upper_left_y)
		sierpinski_triangle(order - 1, length / 2, upper_left_x + (length / 2), upper_left_y)
		sierpinski_triangle(order - 1, length / 2, upper_left_x + (length / 4), upper_left_y + (length * 0.433))


if __name__ == '__main__':
	main()