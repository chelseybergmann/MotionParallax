# Author: Chelsey Bergmann
# Description: This program uses various shapes to create a landscape
#              that uses an offset motion for the mouse to create a motion parallax.  
#              The colors of the mountains are randomized upon start up and the use of
#              loops/wrapping is used to create the birds and grass.

from graphics import graphics
import random

def main():
    gui = graphics(600, 600, 'Landscape')
    color_string1 = color_string(gui)
    color_string2 = color_string(gui)
    color_string3 = color_string(gui)
    i = 0
    x_coord = 0
    y_coord = 0
    # Prints all shapes with their varied motions
    while True:
        gui.clear()
        gui.rectangle(-10, -10, 700, 700, 'SkyBlue2')
        print_sun(gui)
        print_mountains(gui, color_string1, color_string2, color_string3)
        print_foreground(gui)
        print_birds(gui, x_coord, y_coord)
        gui.update_frame(60)
        x_coord += 1
        if x_coord == 520:
            x_coord = -375


def color_string(gui):
    '''
    Gets a random color.
    gui: Creates canvas.
    '''
    color_string = gui.get_color_string(red = random.randint(0, 255),
    green = random.randint(0, 255), blue = random.randint(0,255))
    return color_string

def print_sun(gui):
    '''
    Prints the sun.
    x: Equals gui.mouse_x to offset motion.
    y: Equals gui.mouse_y to offset motion.
    gui: Creates canvas.
    '''
    x = gui.mouse_x
    y = gui.mouse_y
    gui.ellipse(x/100 + 405, y/100 + 85, 90, 90, 'yellow')

def print_mountains(gui, color_string1, color_string2, color_string3):
    '''
    Prints all three mountains.
    gui: Creates canvas.
    '''
    x = gui.mouse_x
    y = gui.mouse_y
    gui.triangle(x/50 + 150, y/50 + 500, x/50 + 300, y/50 + 150, x/50 + 450, y/50 + 500, color_string1)
    gui.triangle(x/35 - 50, y/35 + 500, x/35 + 150, y/35 + 270, x/35 + 330, y/35 + 500, color_string2)
    gui.triangle(x/35 + 250, y/35 + 500, x/35 + 450, y/35 + 270, x/35 + 650, y/35 + 500, color_string3)

def print_foreground(gui):
    '''
    Prints landscape, grass, and tree.
    x: Equals gui.mouse_x to offset motion.
    y: Equals gui.mouse_y to offset motion.
    gui: Creates canvas.
    '''

    x =  gui.mouse_x
    y =  gui.mouse_y
    gui.rectangle(x/25 - 50, y/25 + 500, 700, 500, 'SpringGreen2')
    i = 4
    # Prints grass
    while i < 700:
        if i % 4 == 0:
            gui.line(x/25 + i - 54, y/25 + 500, x/25 + i - 54, y/25 + 480, 'Green2', 2)
        i += 1
    # Prints tree
    gui.rectangle(x/15 + 450, y/15 + 490, 25, 50, 'firebrick4')
    gui.ellipse(x/15 + 463, y/15 + 450, 70, 100, 'green4')

def print_birds(gui, x_coord, y_coord):
    '''
    Prints birds flying across screen and allows them to wrap around.
    gui: Creates canvas.
    x_coord: x_coordinate of line to make bird
    y_coord: y_coordinate of line to make bird
    '''
    i = x_coord
    j = y_coord
    height = 0
    
    while j < 300:
        gui.line(150 + i + j, 250 + height, 110 + i + j, 260 + height, 'black', 2)
        gui.line(75 + i + j, 250 + height, 110 + i + j , 260 + height, 'black' , 2)
        j += 100
        height += 20
        
    

main()