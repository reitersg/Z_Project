"""
The Python Capstone Project.

This file contains data SHARED by the other modules in this project.

CSSE 120 - Introduction to Software Development.
Team members: Alan Yates, Brendan Goldacker, Scott Reiter
"""
# DONE: Put the names of ALL team members in the above where indicated.

import m1
import m2
import m3
import m4

import tkinter
from tkinter import ttk

# ----------------------------------------------------------------------
# DONE: TEAM-PROGRAM this module so that it runs your entire program,
#       incorporating parts from m1 .. m4.
# ----------------------------------------------------------------------


class DataContainer():
    """ A container for the data shared across the application. """

    def __init__(self):
        """ Initializes instance variables (fields). """
        # Add     self.FOO = BLAH     here as needed.
        self.robot = None
        self.if_key_controlled_called_already = False
        self.key_released = False
        self.stop_button_pressed = False


def main():
    """ Runs the MAIN PROGRAM. """
    print('----------------------------------------------')
    print('Integration Testing of the INTEGRATED PROGRAM:')
    print('----------------------------------------------')

    root = tkinter.Tk()
    dc = DataContainer()

    frame1 = m1.my_frame(root, dc)
    frame1.grid()

    frame2 = m2.my_frame(root, dc)
    frame2.grid()

    frame3 = m3.my_frame(root, dc)
    frame3.grid()

    hours = m3.hours_frame(root, dc)
    hours.grid()

    root.mainloop()

# ----------------------------------------------------------------------
# If this module is running at the top level (as opposed to being
# imported by another module), then call the 'main' function.
# ----------------------------------------------------------------------
if __name__ == '__main__':
    main()
