"""
The Python Capstone Project.

CSSE 120 - Introduction to Software Development.
Team members: Brendan Goldacker, Scott Reiter, and Alan Yates.

The primary author of this module is: Alan Yates.
"""
# DONE: Put the names of ALL team members in the above where indicated.
#       Put YOUR NAME in the above where indicated.

import m0
import m1
import m2
import m4

import tkinter
from tkinter import ttk
import new_create
import time
import math
import random

def main():
    """
    Tests functions in this module.
    Intended to be used internally by the primary author of this module.
    """
    print('-------------------------------')
    print('Testing functions in module m3:')
    print('-------------------------------')

    root = tkinter.Tk()
    dc = m0.DataContainer

    frame1 = m1.my_frame(root, dc)
    frame1.grid(column=0, row=0)

    frame2 = m2.my_frame(root, dc)
    frame2.grid(column=1, row=0)

    frame3 = my_frame(root, dc)
    frame3.grid(column=2, row=0)

    hours = hours_frame(root, dc)
    hours.grid(column=1, row=1)

    root.mainloop()

def my_frame(root, dc):
    """
    Constructs and returns a Frame (on the given root window)
    that contains this module's widgets.
    Also sets up callbacks for this module's widgets.

    Preconditions:
      :type root: tkinter.Tk
      :type dc: m0.DataContainer
      :type speed_entry: int
    """
    frame = ttk.Frame(root, padding=30, relief='raised')

    speed_label = ttk.Label(frame, text='robot speed:')
    speed_entry = ttk.Entry(frame, width=10)
    dist_label = ttk.Label(frame, text='N centimeters:')
    dist_entry = ttk.Entry(frame, width=10)
    speed_label.grid(column=0, row=0)
    speed_entry.grid(column=1, row=0)
    dist_label.grid(column=0, row=1)
    dist_entry.grid(column=1, row=1)
    radius_entry = ttk.Entry(frame, width=5)
    radius_entry.grid(column=2, row=1)
    radius_label = ttk.Label(frame, text='Radius:')
    radius_label.grid(column=2, row=0)

    left_button = ttk.Button(frame, text='Left')
    left_button.grid(column=0, row=3)
    left_button['command'] = lambda: move_left(speed_entry, dist_entry, dc)

    right_button = ttk.Button(frame, text='Right')
    right_button.grid(column=2, row=3)
    right_button['command'] = lambda: move_right(speed_entry, dist_entry, dc)

    forward_button = ttk.Button(frame, text='Forward')
    forward_button.grid(column=1, row=2)
    forward_button['command'] = lambda: move_N_cm(speed_entry, dist_entry, dc)

    backwards_button = ttk.Button(frame, text='Backward')
    backwards_button.grid(column=1, row=4)
    backwards_button['command'] = lambda: move_backwards(speed_entry, dist_entry, dc)

    turn_around_button = ttk.Button(frame, text='Turn Around')
    turn_around_button.grid(column=1, row=3)
    turn_around_button['command'] = lambda: turn_around_and_move(speed_entry, dist_entry, dc)

    stop_button = ttk.Button(frame, text='Stop')
    stop_button.grid(column=0, row=4)
    stop_button['command'] = lambda: stop_func(dc)

    CW_circle_button = ttk.Button(frame, text='CW Circle w/Radius')
    CW_circle_button.grid(column=2, row=4)
    CW_circle_button['command'] = lambda: circle(dc, radius_entry, speed_entry, 'CW')

    CCW_circle_button = ttk.Button(frame, text='CCW Circle w/Radius')
    CCW_circle_button.grid(column=2, row=5)
    CCW_circle_button['command'] = lambda: circle(dc, radius_entry, speed_entry, 'CCW')

    figure_8_button = ttk.Button(frame, text='Figure 8 pattern w/Radius')
    figure_8_button.grid(column=2, row=2)
    figure_8_button['command'] = lambda: figure_8_pat(dc, radius_entry, speed_entry)
#----------------------------------

#-----Waypoints--------------------
    waypoints_label = ttk.Label(frame, text='Enter waypoint:')
    waypoints_entry_button = ttk.Button(frame, text='Enter')
    waypoints_x_entry = ttk.Entry(frame, width=5)
    waypoints_x_label = ttk.Label(frame, text='x coordinate:')
    waypoints_y_entry = ttk.Entry(frame, width=5)
    waypoints_y_label = ttk.Label(frame, text='y coordinate:')
    waypoints_label.grid(column=0, row=7)
    waypoints_entry_button.grid(column=0, row=8)
    waypoints_x_entry.grid(column=1, row=9)
    waypoints_x_label.grid(column=0, row=9)
    waypoints_y_entry.grid(column=1, row=10)
    waypoints_y_label.grid(column=0, row=10)
    waypoints = [(0, 0)]
    waypoints_entry_button['command'] = lambda: enter_waypoints(waypoints_x_entry, waypoints_y_entry, waypoints)
    follow_wp_button = ttk.Button(frame, text='Follow Waypoints')
    follow_wp_button.grid(column=1, row=5)
    follow_wp_button['command'] = lambda: follow_wp(dc, waypoints, speed_entry)
    clear_wp_button = ttk.Button(frame, text='Clear Waypoints')
    clear_wp_button.grid(column=0, row=12)
    clear_wp_button['command'] = lambda: clear_wp(waypoints, waypoints_label)

#----------------------------------
#------Sing and Dance / with lights--
    w_lights = ttk.Checkbutton(frame, text='With Lights')
    w_lights.grid(column=0, row=14)
    with_lights = tkinter.IntVar()
    w_lights['variable'] = with_lights
    dance_label = ttk.Label(frame, text='Sing and Dance:')
    dance_label.grid(column=0, row=13)
    long_dance = ttk.Button(frame, text='Long')
    short_dance = ttk.Button(frame, text='Short')
    long_dance.grid(column=1, row=13)
    long_dance['command'] = lambda: sing_and_dance(dc, 30, with_lights)
    short_dance.grid(column=2, row=13)
    short_dance['command'] = lambda: sing_and_dance(dc, 15, with_lights)
#-----------------------------------
#---Polygon with N sides------------
    poly_label = ttk.Label(frame, text='Traverse Polygon with N sides of length L:')
    poly_label.grid(column=1, row=15)
    poly_sides_label = ttk.Label(frame, text='N:')
    poly_sides_label.grid(column=0, row=16)
    poly_sides = ttk.Entry(frame, width=5)
    poly_sides.grid(column=1, row=16)
    poly_length_label = ttk.Label(frame, text='L:')
    poly_length_label.grid(column=0, row=17)
    poly_length = ttk.Entry(frame, width=5)
    poly_length.grid(column=1, row=17)
    poly_go = ttk.Button(frame, text='Traverse Polygon')
    poly_go.grid(column=1, row=18)
    poly_go['command'] = lambda: follow_poly(dc, poly_sides, poly_length, speed_entry)
#-----------------------------------
    return frame
#-------Hours Worked Lists---------
def hours_frame(root, dc):
    hours_worked = ttk.Frame(root, padding=30, relief='raised')

    hours_title = ttk.Label(hours_worked, text='Number of hours worked by each team member, by sprint:')
    hours_title.grid(column=1, row=0)

    b = open('../process/hours-1.txt', 'r')
    brendan = b.read()
    b.close()
    brendan_label = ttk.Label(hours_worked, text=brendan)
    brendan_label.grid(column=0, row=1)

    s = open('../process/hours-2.txt', 'r')
    scott = s.read()
    s.close()
    scott_label = ttk.Label(hours_worked, text=scott)
    scott_label.grid(column=1, row=1)

    a = open('../process/hours-3.txt', 'r')
    alan = a.read()
    a.close()
    alan_label = ttk.Label(hours_worked, text=alan)
    alan_label.grid(column=2, row=1)

    return hours_worked
#-----------------------------------

#-----Movements-------
def move_N_cm(speed_entry, dist_entry, dc):
    """
    moves robot N centimeters at an entered speed
    """
    speed = int(speed_entry.get())
    dist = int(dist_entry.get())
    t = (dist / speed)

    dc.robot.driveDirect(speed, speed)
    time.sleep(t)
    dc.robot.stop()

def move_left(speed_entry, dist_entry, dc):
    """
    moves robot N centimeters at an entered speed after rotating to the left
    """
    dc.robot.go(0, 90)
    time.sleep(1)
    move_N_cm(speed_entry, dist_entry, dc)

def move_right(speed_entry, dist_entry, dc):
    """
    moves robot N centimeters at an entered speed after rotating to the right
    """
    dc.robot.go(0, -90)
    time.sleep(1)
    move_N_cm(speed_entry, dist_entry, dc)

def turn_around_and_move(speed_entry, dist_entry, dc):
    """
    moves robot N centimeters at an entered speed after turning around
    """
    dc.robot.go(0, -180)
    time.sleep(1)
    move_N_cm(speed_entry, dist_entry, dc)

def move_backwards(speed_entry, dist_entry, dc):
    """
    moves robot N centimeters at an entered speed after turning around
    """
    speed = -1 * int(speed_entry.get())
    dist = int(dist_entry.get())
    t = (dist / abs(speed))

    dc.robot.driveDirect(speed, speed)
    time.sleep(t)
    dc.robot.stop()

def stop_func(dc):
    dc.robot.stop()

def circle(dc, radius_entry, speed_entry, direction):
    radius = int(radius_entry.get())
    speed = int(speed_entry.get())
    t = (2 * math.pi * radius) / speed
    if direction == 'CCW':
        dc.robot.drive(speed * 10, -radius * 10, turnDir='CCW')
    elif direction == 'CW':
        dc.robot.drive(speed * 10, radius * 10, turnDir='CW')
    time.sleep(t)
    dc.robot.stop()

def figure_8_pat(dc, radius_entry, speed_entry):
    radius = int(radius_entry.get())
    speed = int(speed_entry.get())
    t = (2 * math.pi * radius) / speed
    dc.robot.drive(speed * 10, -radius * 10, turnDir='CCW')
    time.sleep(t)
    dc.robot.drive(speed * 10, radius * 10, turnDir='CW')
    time.sleep(t)
    dc.robot.stop()
#------------------------------------

def enter_waypoints(waypoints_x_entry, waypoints_y_entry, waypoints):
    waypoints.append((int(waypoints_x_entry.get()), int(waypoints_y_entry.get())))
    print('Waypoints:', waypoints)
    return waypoints

def clear_wp(waypoints):
    for k in range(len(waypoints) - 1):
        waypoints.pop()
    return waypoints

def follow_wp(dc, waypoints, speed_entry):
    speed = int(speed_entry.get())
    wpx = wp_x(waypoints)
    wpy = wp_y(waypoints)
    t_list = []
    xdiff = []
    ydiff = []
    dis = []
    for k in range(len(waypoints) - 1):
        xdiff.append(wpx[k + 1] - wpx[k])
        ydiff.append(wpy[k + 1] - wpy[k])
    angle_list = [math.atan(ydiff[0] / xdiff[0])]
    for j in range(len(xdiff)):
        dis.append(math.sqrt((xdiff[j] ** 2) + (ydiff[j] ** 2)))
    for k in range(len(waypoints) - 1):
        t = dis[k] / speed
        t_list.append(t)
        n = k
        curr_ang = 0
        for k in range(len(angle_list)):
            curr_ang = curr_ang + angle_list[k]
        if xdiff[n] == 0 and ydiff[n] > 0:
            angle = 90 - curr_ang
        elif xdiff[n] == 0 and ydiff[n] < 0:
            angle = -90 - curr_ang
        elif ydiff[n] == 0 and xdiff[n] > 0:
            angle = 0 - curr_ang
        elif ydiff[n] == 0 and xdiff[n] < 0:
            angle = 180 - curr_ang
        elif ydiff[n] != 0 and xdiff[n] != 0:
            angle = (180 / math.pi) * (math.atan(ydiff[n] / xdiff[n])) - curr_ang + 180
        angle_list.append(angle)
        print(angle_list)
        print(t_list)
    for j in range(len(t_list)):
        dc.robot.go(0, angle_list[j + 1])
        time.sleep(1)
        dc.robot.driveDirect(speed, speed)
        time.sleep(t_list[j])
    dc.robot.stop()

def wp_x(waypoints):
    wpx = []
    for k in range(len(waypoints)):
        wpx.append(waypoints[k][0])
    return wpx

def wp_y(waypoints):
    wpy = []
    for k in range(len(waypoints)):
        wpy.append(waypoints[k][1])
    return wpy
#--------------------------------
#--------------------------------
def sing_and_dance(dc, n, with_lights):
    for k in range(n):
        speed_L = int(random.randrange(-50, 50))
        speed_R = int(random.randrange(-50, 50))
        dc.robot.driveDirect(speed_L, speed_R)
        note = random.randrange(3, 127)
        dc.robot.playNote(note, 62)
        if with_lights.get() == 1:
            color = int(random.randrange(1, 255))
            intensity = int(random.randrange(1, 255))
            green_1 = random.randrange(0, 100)
            if green_1 <= 50:
                green_1 = 0
            else:
                green_1 = 1
            green_2 = random.randrange(0, 100)
            if green_2 <= 50:
                green_2 = 0
            else:
                green_2 = 1
            dc.robot.setLEDs(color, intensity, green_1, green_2)
        time.sleep(1)
    dc.robot.stop()
#----------------------------------
#----Follow polygon with N sides---
def follow_poly(dc, poly_sides, poly_length, speed_entry):
    N = int(poly_sides.get())
    L = int(poly_length.get())
    speed = int(speed_entry.get())
    t = L / speed
    angle = (180 * (N - 2)) / (N)
    if L < 0:
        print('Invalid Length of Sides!!!')
    if N < 4:
        print('Invalid Number of Sides!!!')
    if L >= 0 and N >= 4:
        for k in range(N):
            dc.robot.go(0, angle)
            time.sleep(1)
            dc.robot.driveDirect(speed, speed)
            time.sleep(t)
        dc.robot.stop()
#---------------------------------

# ----------------------------------------------------------------------
# If this module is running at the top level (as opposed to being
# imported by another module), then call the 'main' function.
# ----------------------------------------------------------------------
if __name__ == '__main__':
    main()
