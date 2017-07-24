"""
The Python Capstone Project.

CSSE 120 - Introduction to Software Development.
Team members: Alan, Brendan, Scott(all of them).

The primary author of this module is: Brendan Goldacker.
"""
# DONE: Put the names of ALL team members in the above where indicated.
#       Put YOUR NAME in the above where indicated.

import m0
import m2
import m3
import m4

import time
import tkinter
from tkinter import ttk
import new_create
from new_create import Sensors


def main():
    """
    Tests functions in this module.
    Intended to be used internally by the primary author of this module.
    """
    print('-------------------------------')
    print('Testing functions in module m1:')
    print('-------------------------------')
    root = tkinter.Tk()
    dc = m0.DataContainer()

    framem2 = m2.my_frame(root, dc)
    framem2.grid(row=1, column=2)

    framem3 = m3.my_frame(root, dc)
    framem3.grid(row=1, column=3)

    frame1 = my_frame(root, dc)
    frame1.grid(row=1, column=1)

    root.mainloop()

# creates frame and runs in main
def my_frame(root, dc):
    """
    Constructs and returns a Frame (on the given root window)
    that contains this module's widgets.
    Also sets up callbacks for this module's widgets.

    Preconditions:
      :type root: tkinter.Tk
      :type dc: m0.DataContainer
    """

    frame = ttk.Frame(root, padding=20, relief='raised')

    button1 = ttk.Button(frame, text='Connect to simulator')
    button1.grid()
    button1['command'] = lambda: connect_using_simulator(dc)

    entry = ttk.Entry(frame, width=8)
    entry.grid()

    button2 = ttk.Button(frame, text='connect using port')
    button2.grid()
    button2['command'] = lambda: connect_using_port(entry, dc)

    button3 = ttk.Button(frame, text='Disconnect')
    button3.grid()
    button3['command'] = lambda: disconnect(dc)

    button4 = ttk.Button(frame, text='follow black line')
    button4.grid(row=1, column=2)
    button4['command'] = lambda: follow_line(dc, root)

    button5 = ttk.Button(frame, text='Stop following line')
    button5.grid(row=2, column=2)
    button5['command'] = lambda: stop_button(dc)

    menu = tele_menu(root, dc, frame)
    menu.grid()

    return frame
# ## TASK 1: creats connect to sim, connect to port, and disconnect buttons and functions
def connect_using_simulator(dc):
    """connects to the to the irobot simulator. 
    Preconditions:
        :type dc : m0.DataContianer"""
    port = 'sim'
    dc.robot = new_create.Create(port)
    dc.robot.toFullMode()
    print('connected to the simulator')

def connect_using_port(entry, dc):
    """Connects to the robot by the given prot number. 
        Preconditions:
        :type dc : m0.DataContianer"""
    port = int(entry.get())
    dc.robot = new_create.Create(port, dc)
    dc.robot.toFullMode()

def disconnect(dc):
    """Disconnects from the robot
     Preconditions:
        :type dc : m0.DataContianer"""
    dc.robot.shutdown()
    print('robot is disconnected')


# ## TASK 2: adds a menu for tele operations options, including key controls and mouse
def tele_menu(root, dc, frame):
    """if tele controll is on, it creates a menu of possible tele controll methods
        Preconditions:
          :type root: tkinter.Tk
          :type dc: m0.DataContainer
      """
    root.option_add('*tearOff', False)
    menubar = tkinter.Menu(root)
    root['menu'] = menubar

    change_menu = tkinter.Menu(menubar)
    menubar.add_cascade(menu=change_menu, label='tele options')

    change_menu.add_command(label='Use Key controlls',
                            command=lambda: key_controller(root, dc, frame, tele_label))

    change_menu.add_command(label='do not use tele controlls', command=lambda: no_controlls(root, dc, tele_label))

    tele_label = ttk.Label(frame, text='tele options: off')
    tele_label.grid()

    return frame

def no_controlls(root, dc, label):
    """stops the robot from using tele controls
     Preconditions:
          :type root: tkinter.Tk
          :type dc: m0.DataContainer
     """
    root.bind_all('<KeyPress>', lambda: None)
    root.bind_all('<KeyRelease>', lambda: None)
    root.bind_all('<Key-w>', lambda: None)
    root.bind_all('<Key-a>', lambda: None)
    root.bind_all('<Key-d>', lambda: None)
    root.bind_all('<Key-s>', lambda: None)
    root.bind_all('<Key-x>', lambda: None)
    label['text'] = 'tele controlls: off'

def key_controller(root, dc, frame, label):
    """allows the robot to be controlled with the a, d, w, x, s keys to move left , right , froward, backwards,
    and spin respectivley
        Preconditions:
          :type root: tkinter.Tk
          :type dc: m0.DataContainer
          :type frame: ttk.Frame
    """
    if dc.if_key_controlled_called_already == False:
        forward_label = ttk.Label(frame, text='go foward: w')
        forward_label.grid()
        left_label = ttk.Label(frame, text='go left: a')
        left_label.grid()
        right_label = ttk.Label(frame, text='go right: d')
        right_label.grid()
        backwards_label = ttk.Label(frame, text='go backwards: x')
        backwards_label.grid()
        spin_label = ttk.Label(frame, text='spin: s')
        spin_label.grid()
        dc.if_key_controlled_called_already = True

    label['text'] = 'tele controlls: key-controlls'

    root.bind_all('<KeyPress>', lambda event: pressed_a_key(event, dc))
    root.bind_all('<KeyRelease>', lambda event: released_a_key(event, dc))
    root.bind_all('<Key-w>', lambda event: go_forward(event, dc))
    root.bind_all('<Key-a>', lambda event: go_left(event, dc))
    root.bind_all('<Key-d>', lambda event: go_right(event, dc))
    root.bind_all('<Key-s>', lambda event: spin(event, dc))
    root.bind_all('<Key-x>', lambda event: go_backwards(event, dc))

def pressed_a_key(event, dc):
    """prints a message when you press a key"""
    print('You pressed the', event.keysym, 'key')
    dc.key_released = False

def released_a_key(event, dc):
    """prints a message when a key is released"""
    print('You released the', event.keysym, 'key')
    dc.key_released = True
    dc.robot.stop()
    print('stoped')

def go_forward(event, dc):
    """has the robot go forward when a button is pressed"""
    print('You pressd the ' + event.keysym + 'key: ', end='')
    print('Go forward!')
    dc.robot.driveDirect(50, 50)

def go_left(event, dc):
    """has the robot go to the left when a certian key is pressed"""
    print('You pressed the ' + event.keysym + ' key: ', end='')
    print('Go left!')
    dc.robot.driveDirect(10, 50)

def go_right(event, dc):
    """has the robot go to the right when a certian key is pressed"""
    print('You pressd the ' + event.keysym + 'key: ', end='')
    print('Go Right!')
    dc.robot.driveDirect(50, 10)

def spin(event, dc):
    """has the robot spin when a certian key is pressed"""
    print('You pressd the ' + event.keysym + 'key: ', end='')
    print('Spin!')
    dc.robot.driveDirect(-40, 40)

def go_backwards(event, dc):
    """has the robot go backwards when a certian key is pressed"""
    print('You pressd the ' + event.keysym + 'key: ', end='')
    print('Go Backwards!')
    dc.robot.driveDirect(-50, -50)

# def mouse_controller(frame, dc):
#
#     label = ttk.Label(frame, text='Use mouse to control your robot')
#     label.grid()

# ## TASK 3: has robot follow a black line
def follow_line(dc, root):
    """when button is pressed, the robot will folow a black line until the stop button is pressed
        Preconditions:
          :type root: tkinter.Tk
          :type dc: m0.DataContainer
    """
    dc.stop_button_pressed = False
    left_light_sensor = new_create.Sensors.cliff_front_left_signal
    right_light_sensor = new_create.Sensors.cliff_front_right_signal
    while True:
        left_light = dc.robot.getSensor(left_light_sensor)
        right_light = dc.robot.getSensor(right_light_sensor)
        left_speed = left_light / 70
        right_speed = right_light / 70
        dc.robot.driveDirect(left_speed, right_speed)
        root.update()
        if dc.stop_button_pressed == True:
            dc.robot.stop()
            break

def stop_button(dc):
    """when button is pressed, the robot will stop following a line"""
    print('stop button pressed. stopping the robot')
    dc.stop_button_pressed = True

# ----------------------------------------------------------------------
# If this module is running at the top level (as opposed to being
# imported by another module), then call the 'main' function.
# ----------------------------------------------------------------------
if __name__ == '__main__':
    main()
