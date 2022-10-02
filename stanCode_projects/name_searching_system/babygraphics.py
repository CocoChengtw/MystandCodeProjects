"""
File: babygraphics.py
Name: Coco
--------------------------------
SC101 Baby Names Project
Adapted from Nick Parlante's Baby Names assignment by
Jerry Liao.
"""

import tkinter
import babynames
import babygraphicsgui as gui

FILENAMES = [
    'data/full/baby-1900.txt', 'data/full/baby-1910.txt',
    'data/full/baby-1920.txt', 'data/full/baby-1930.txt',
    'data/full/baby-1940.txt', 'data/full/baby-1950.txt',
    'data/full/baby-1960.txt', 'data/full/baby-1970.txt',
    'data/full/baby-1980.txt', 'data/full/baby-1990.txt',
    'data/full/baby-2000.txt', 'data/full/baby-2010.txt'
]
CANVAS_WIDTH = 1000
CANVAS_HEIGHT = 600
YEARS = [1900, 1910, 1920, 1930, 1940, 1950,
         1960, 1970, 1980, 1990, 2000, 2010]
GRAPH_MARGIN_SIZE = 20
COLORS = ['red', 'purple', 'green', 'blue']
TEXT_DX = 2
LINE_WIDTH = 2
MAX_RANK = 1000


def get_x_coordinate(width, year_index):
    """
    Given the width of the canvas and the index of the current year
    in the YEARS list, returns the x coordinate of the vertical
    line associated with that year.

    Input:
        width (int): The width of the canvas
        year_index (int): The index where the current year is in the YEARS list
    Returns:
        x_coordinate (int): The x coordinate of the vertical line associated
                            with the current year.
    """
    # to get the location of the year on the graph
    line_dist = (width-(GRAPH_MARGIN_SIZE*2))/len(YEARS)
    x_coordinate = GRAPH_MARGIN_SIZE + line_dist*year_index
    return x_coordinate


def draw_fixed_lines(canvas):
    """
    Draws the fixed background lines on the canvas.

    Input:
        canvas (Tkinter Canvas): The canvas on which we are drawing.
    """
    canvas.delete('all')            # delete all existing lines from the canvas

    # Draw the top and button line of the boundary
    canvas.create_line(GRAPH_MARGIN_SIZE, GRAPH_MARGIN_SIZE, CANVAS_WIDTH-GRAPH_MARGIN_SIZE, GRAPH_MARGIN_SIZE, width=LINE_WIDTH)
    canvas.create_line(GRAPH_MARGIN_SIZE, CANVAS_HEIGHT-GRAPH_MARGIN_SIZE, CANVAS_WIDTH-GRAPH_MARGIN_SIZE, CANVAS_HEIGHT-GRAPH_MARGIN_SIZE, width=LINE_WIDTH)

    # Draw the year and the corresponding line on the graph
    for y in range(1, len(YEARS)):
        canvas.create_line(get_x_coordinate(CANVAS_WIDTH, y), 0, get_x_coordinate(CANVAS_WIDTH, y), CANVAS_HEIGHT)
    for y in range(len(YEARS)):
        canvas.create_text(get_x_coordinate(CANVAS_WIDTH, y)+TEXT_DX, CANVAS_HEIGHT-GRAPH_MARGIN_SIZE, text=YEARS[y], anchor=tkinter.NW)


def draw_names(canvas, name_data, lookup_names):
    """
    Given a dict of baby name data and a list of name, plots
    the historical trend of those names onto the canvas.

    Input:
        canvas (Tkinter Canvas): The canvas on which we are drawing.
        name_data (dict): Dictionary holding baby name data
        lookup_names (List[str]): A list of names whose data you want to plot

    Returns:
        This function does not return any value.
    """
    draw_fixed_lines(canvas)        # draw the fixed background grid

    # Draw the names and their ranking trend line
    for i in range(len(lookup_names)):
        for j in range(len(YEARS)):
            name = lookup_names[i]
            if str(YEARS[j]) in name_data[lookup_names[i]]:
                rank = name_data[lookup_names[i]][str(YEARS[j])]
            else:
                rank = 1000

            if j+1 < len(YEARS):
                if str(YEARS[j+1]) in name_data[lookup_names[i]]:
                    rank_n = name_data[lookup_names[i]][str(YEARS[j+1])]
                else:
                    rank_n = 1000

            rank_unit = (CANVAS_HEIGHT - GRAPH_MARGIN_SIZE*2)/1000
            # Draw the name on the corresponding spot of its ranking
            if rank == 1000:
                canvas.create_text(get_x_coordinate(CANVAS_WIDTH, j)+TEXT_DX, rank_unit*int(rank)+GRAPH_MARGIN_SIZE, text=name+' '+'*', anchor=tkinter.SW, fill=COLORS[i])
            else:
                canvas.create_text(get_x_coordinate(CANVAS_WIDTH, j)+TEXT_DX, rank_unit*int(rank)+GRAPH_MARGIN_SIZE, text=name+' '+str(rank), anchor=tkinter.SW, fill=COLORS[i])

            # Draw the trend line of the name's ranking
            if j+1 < len(YEARS):
                if rank == 1000:
                    canvas.create_line(get_x_coordinate(CANVAS_WIDTH, j), rank_unit * int(rank) + GRAPH_MARGIN_SIZE,
                                       get_x_coordinate(CANVAS_WIDTH, j + 1), rank_unit * int(rank_n) + GRAPH_MARGIN_SIZE,
                                       width=LINE_WIDTH, fill=COLORS[i])
                else:
                    canvas.create_line(get_x_coordinate(CANVAS_WIDTH, j), rank_unit * int(rank) + GRAPH_MARGIN_SIZE,
                                       get_x_coordinate(CANVAS_WIDTH, j + 1), rank_unit * int(rank_n) + GRAPH_MARGIN_SIZE,
                                       width=LINE_WIDTH, fill=COLORS[i])


# main() code is provided, feel free to read through it but DO NOT MODIFY
def main():
    # Load data
    name_data = babynames.read_files(FILENAMES)

    # Create the window and the canvas
    top = tkinter.Tk()
    top.wm_title('Baby Names')
    canvas = gui.make_gui(top, CANVAS_WIDTH, CANVAS_HEIGHT, name_data, draw_names, babynames.search_names)

    # Call draw_fixed_lines() once at startup so we have the lines
    # even before the user types anything.
    draw_fixed_lines(canvas)

    # This line starts the graphical loop that is responsible for
    # processing user interactions and plotting data
    top.mainloop()


if __name__ == '__main__':
    main()
