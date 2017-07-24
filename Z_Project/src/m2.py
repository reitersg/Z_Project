"""
The Python Capstone Project.

CSSE 120 - Introduction to Software Development.
Team members: Scott Reiter, Brendan Goldacker, Alan Yates.

The primary author of this module is: Scott Reiter.
"""
# TODO: Put the names of ALL team members in the above where indicated.
#       Put YOUR NAME in the above where indicated.

import m0
import m1
import m3
import m4

import tkinter
from tkinter import ttk
import new_create
import time
import random

def main():
    """
    Tests functions in this module.
    Intended to be used internally by the primary author of this module.
    """
    print('-------------------------------')
    print('Testing functions in module m2:')
    print('-------------------------------')
    root = tkinter.Tk()
    dc = m0.DataContainer

    frame1 = m1.my_frame(root, dc)
    frame1.grid()

    frame2 = my_frame(root, dc)
    frame2.grid()

    frame3 = m3.my_frame(root, dc)
    frame3.grid()

    root.mainloop()

def my_frame(root, dc):
    """
    Constructs and returns a Frame (on the given root window)
    that contains this module's widgets.
    Also sets up callbacks for this module's widgets.

    Preconditions:
      :type root: tkinter.Tk
      :type dc: m0.DataContainer
    """
    robot = m0.DataContainer

    frame = ttk.Frame(root, padding=20, relief='raised')

    speed_button = ttk.Button(frame, text='click to make robot go')
    speed_button.grid(column=2)
    speed_button['command'] = lambda: robot_go(dc, speed_entry, root)

    play_notes_button = ttk.Button(frame, text='Click to play notes')
    play_notes_button.grid(column=0, row=8)
    play_notes_button['command'] = lambda: random_notes(notes_entry, dc, time_entry)

    front_left_cliff_sensor_button = ttk.Button(frame, text='Click to activate the front left cliff sensor')
    front_left_cliff_sensor_button.grid(column=2, row=2)
    front_left_cliff_sensor_button['command'] = lambda: front_left_cliff_sensor(dc, darkness_entry)

    front_right_cliff_sensor_button = ttk.Button(frame, text='Click to activate the front right cliff sensor')
    front_right_cliff_sensor_button.grid(column=2, row=3)
    front_right_cliff_sensor_button['command'] = lambda: front_right_cliff_sensor(dc, darkness_entry)

    right_cliff_sensor_button = ttk.Button(frame, text='Click to activate the right cliff sensor')
    right_cliff_sensor_button.grid(column=0, row=2)
    right_cliff_sensor_button['command'] = lambda: right_cliff_sensor(dc, darkness_entry)

    left_cliff_sensor_button = ttk.Button(frame, text='Click to activate the left cliff sensor')
    left_cliff_sensor_button.grid(column=0, row=3)
    left_cliff_sensor_button['command'] = lambda: left_cliff_sensor(dc, darkness_entry)

    speed_label = ttk.Label(frame, text='Enter speed here:')
    speed_entry = ttk.Entry(frame, width=10)
    speed_label.grid(row=0, column=0)
    speed_entry.grid(row=0, column=1)

    darkness_label = ttk.Label(frame, text='Enter darkness level:')
    darkness_label.grid(row=1, column=0)
    darkness_entry = ttk.Entry(frame, width=10)
    darkness_entry.grid(row=1, column=1)

    notes_label = ttk.Label(frame, text='Enter number of random notes:')
    notes_label.grid(row=6, column=0)
    notes_entry = ttk.Entry(frame, width=10)
    notes_entry.grid(row=6, column=1)

    time_label = ttk.Label(frame, text='Enter number of seconds for notes:')
    time_label.grid(column=0, row=7)
    time_entry = ttk.Entry(frame, width=10)
    time_entry.grid(column=1, row=7)

    bot_start_button = ttk.Button(frame, text='Click to make the robot talk')
    bot_start_button.grid(column=1, row=9)
    bot_start_button['command'] = lambda: bot_talk(dc, bot_entry)

    bot_stop_button = ttk.Button(frame, text='Click to make the robot shut up')
    bot_stop_button.grid(column=1, row=10)
    bot_stop_button['command'] = lambda:bot_shut_up(dc)

    bot_listen_button = ttk.Button(frame, text='Click to make the robot listen')
    bot_listen_button.grid(column=1, row=11)
    listen = True
    bot_listen_button['command'] = lambda: bot_listen(dc, root, listen)

    bot_signal = ttk.Label(frame, text='Enter a number between 0 and 7 for the robot to talk:')
    bot_signal.grid(column=0, row=9)
    bot_entry = ttk.Entry(frame, width=10)
    bot_entry.grid(column=0, row=10)

    return frame
def robot_go(dc, speed_entry, root):
    """Causes robot to go forward with a speed set by the user
        In addition, the robot's bumps prevent it from 
        falling off the table"""
    speed = int(speed_entry.get())
    dc.robot.driveDirect(speed, speed)
    while True:
        sensor1 = new_create.Sensors.bumps_and_wheel_drops
        bump = dc.robot.getSensor(sensor1)
        root.update()
        if bump == [0, 0, 0, 1, 1] or bump == [0, 0, 0, 0, 1] or bump == [0, 0, 0, 1, 0]:
            dc.robot.stop()
            break

def front_left_cliff_sensor(dc, darkness_entry):
    """Activates the front left cliff sensor, and detects the
        darkness set by the user"""
    front_left_cliff_sensor = dc.robot.getSensor(new_create.Sensors.cliff_front_left_signal)
    darkness = darkness_entry.get()
    if front_left_cliff_sensor >= int(darkness):
        dc.robot.stop()

def front_right_cliff_sensor(dc, darkness_entry):
    """Activates the front right cliff sensor, and detects the
        darkness set by the user"""
    front_right_cliff_sensor = new_create.Sensors.cliff_front_right_signal
    darkness = darkness_entry.get()
    if front_right_cliff_sensor >= darkness:
        dc.robot.stop()

def right_cliff_sensor(dc, darkness_entry):
    """Activates the right cliff sensor, and detects the
        darkness set by the user"""
    right_cliff_sensor = new_create.Sensors.cliff_right_signal
    darkness = darkness_entry.get()
    if right_cliff_sensor >= darkness:
        dc.robot.stop()

def left_cliff_sensor(dc, darkness_entry):
    """Activates the left cliff sensor, and detects the
        darkness set by the user"""
    left_cliff_sensor = new_create.Sensors.cliff_left_signal
    darkness = darkness_entry.get()
    if left_cliff_sensor >= darkness:
        dc.robot.stop()

def random_notes(notes_entry, dc, time_entry):
    """plays user-set number of random notes"""
    seconds = int(time_entry.get()) * 64
    number_of_notes = int(notes_entry.get())
    s = number_of_notes
    notes = []
    for k in range(s):
        notes.append(random.randrange(35, 100))
    i = 0
    while i < s:
        music_sensor = dc.robot.getSensor(new_create.Sensors.song_playing)
        if music_sensor == 0:
            dc.robot.playNote(notes[i], seconds)
            i += 1

def bot_shut_up(dc):
    """Causes the robot to be quiet (lights off)"""
    dc.robot.setLEDs(0, 0, 0, 0)
    listen = False
    return listen

def bot_talk(dc, bot_entry):
    """User chooses from 0-7, and causes the robot to 'talk'
        with its lights"""
    signal = int(bot_entry.get())
    if signal == 0:
        dc.robot.setLEDs(250, 0, 0, 1)

    elif signal == 1:
        dc.robot.setLEDs(250, 0, 1, 0)

    elif signal == 2:
        dc.robot.setLEDs(250, 250, 0, 0)

    elif signal == 3:
        dc.robot.setLEDs(250, 250, 1, 0)

    elif signal == 4:
        dc.robot.setLEDs(250, 250, 0, 1)

    elif signal == 5:
        dc.robot.setLEDs(250, 0, 1, 1)

    elif signal == 6:
        dc.robot.setLEDs(250, 250, 1, 1)

    elif signal == 7:
        bot_shut_up(dc)

def bot_listen(dc, root, listen):
    """Causes robot to 'listen' for a certain reading
    and decodes the reading to a number between
    0-7"""

    spot = 132
    clean = 136
    max_button = 133
    forward = 130
    spin_left = 139
    spin_right = 140
    pause = 137
    P = 138

    notes = []
    for k in range(8):
        notes.append(random.randrange(35, 100))
    listen = True
    while listen == True:
        sensor = new_create.Sensors.ir_byte
        right_number = dc.robot.getSensor(sensor)
        root.update()
        if right_number == spot:
            dc.robot.playNote(notes[0], 64)
            print(0)
            dc.robot.setLEDs(250, 0, 0, 1)

        elif right_number == clean:
            dc.robot.playNote(notes[1], 64)
            print(1)
            dc.robot.setLEDs(250, 0, 1, 0)

        elif right_number == max_button:
            dc.robot.playNote(notes[2], 64)
            print(2)
            dc.robot.setLEDs(250, 250, 0, 0)

        elif right_number == spin_left:
            dc.robot.playNote(notes[3], 64)
            print(3)
            dc.robot.setLEDs(250, 250, 1, 0)

        elif right_number == forward:
            dc.robot.playNote(notes[4], 64)
            print(4)
            dc.robot.setLEDs(250, 250, 0, 1)

        elif right_number == spin_right:
            dc.robot.playNote(notes[5], 64)
            print(5)
            dc.robot.setLEDs(250, 0, 1, 1)

        elif right_number == pause:
            dc.robot.playNote(notes[6], 64)
            print(6)
            dc.robot.setLEDs(250, 250, 1, 1)

        elif right_number == P:
            dc.robot.playNote(notes[7], 64)
            print(7)
            bot_shut_up(dc)



# ----------------------------------------------------------------------
# If this module is running at the top level (as opposed to being
# imported by another module), then call the 'main' function.
# ----------------------------------------------------------------------
if __name__ == '__main__':
    main()
