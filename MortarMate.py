import time
import pydirectinput
import pyautogui

import sys
import time
import glob
import csv
import math
import time
from tkinter import *
import tkinter as tk
from PIL import Image, ImageTk
from itertools import count, cycle

win=tk.Tk()
win.configure(bg='#282C34')
win.title('MortarMate')
win.geometry("1400x1000")
win.resizable(width=False, height=False)

map = Canvas(win, width=1000, height= 1000)
map.grid(row=1,column=1, rowspan= 8)
current_position = [0,0]
home_position = [0,0]
first_position = [0,0]
polar_strike_coordinates = [[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0]]
point_index = 0
distances = [0,0,0,0,0,0,0,0,0,0,0,0]

a1 = Image.open('North Region Maps\Grid Maps\B2.png')
a2 = Image.open('North Region Maps\Grid Maps\B3.png')
a3 = Image.open('North Region Maps\Grid Maps\B4.png')
b1 = Image.open('North Region Maps\Grid Maps\C2.png')
b2 = Image.open('North Region Maps\Grid Maps\C3.png')
b3 = Image.open('North Region Maps\Grid Maps\C4.png')
c1 = Image.open('North Region Maps\Grid Maps\D2.png')
c2 = Image.open('North Region Maps\Grid Maps\D3.png')
c3 = Image.open('North Region Maps\Grid Maps\D4.png')
d1 = Image.open('South Region Maps\Grid Maps\B2.png')
d2 = Image.open('South Region Maps\Grid Maps\B3.png')
d3 = Image.open('South Region Maps\Grid Maps\B4.png')
e1 = Image.open('South Region Maps\Grid Maps\C2.png')
e2 = Image.open('South Region Maps\Grid Maps\C3.png')
e3 = Image.open('South Region Maps\Grid Maps\C4.png')
f1 = Image.open('South Region Maps\Grid Maps\D2.png')
f2 = Image.open('South Region Maps\Grid Maps\D3.png')
f3 = Image.open('South Region Maps\Grid Maps\D4.png')


resized_a1= a1.resize((1000,1000))
A1_LARGE = ImageTk.PhotoImage(resized_a1)
resized_a2= a2.resize((1000,1000))
A2_LARGE  = ImageTk.PhotoImage(resized_a2)
resized_a3= a3.resize((1000,1000))
A3_LARGE  = ImageTk.PhotoImage(resized_a3)
resized_b1= b1.resize((1000,1000))
B1_LARGE  = ImageTk.PhotoImage(resized_b1)
resized_b2= b2.resize((1000,1000))
B2_LARGE  = ImageTk.PhotoImage(resized_b2)
resized_b3= b3.resize((1000,1000))
B3_LARGE  = ImageTk.PhotoImage(resized_b3)
resized_c1= c1.resize((1000,1000))
C1_LARGE  = ImageTk.PhotoImage(resized_c1)
resized_c2= c2.resize((1000,1000))
C2_LARGE  = ImageTk.PhotoImage(resized_c2)
resized_c3= c3.resize((1000,1000))
C3_LARGE  = ImageTk.PhotoImage(resized_c3)
resized_d1= d1.resize((1000,1000))
D1_LARGE  = ImageTk.PhotoImage(resized_d1)
resized_d2= d2.resize((1000,1000))
D2_LARGE  = ImageTk.PhotoImage(resized_d2)
resized_d3= d3.resize((1000,1000))
D3_LARGE  = ImageTk.PhotoImage(resized_d3)
resized_e1= e1.resize((1000,1000))
E1_LARGE  = ImageTk.PhotoImage(resized_e1)
resized_e2= e2.resize((1000,1000))
E2_LARGE  = ImageTk.PhotoImage(resized_e2)
resized_e3= e3.resize((1000,1000))
E3_LARGE  = ImageTk.PhotoImage(resized_e3)
resized_f1= f1.resize((1000,1000))
F1_LARGE  = ImageTk.PhotoImage(resized_f1)
resized_f2= f2.resize((1000,1000))
F2_LARGE  = ImageTk.PhotoImage(resized_f2)
resized_f3= f3.resize((1000,1000))
F3_LARGE  = ImageTk.PhotoImage(resized_f3)




def switchMap(img):
    global image_container
    map.itemconfig(image_container,image=img)

def clear_points():
    global image_container
    global point_index
    global polar_strike_coordinates
    point_index = 0
    map.delete("all")
    polar_strike_coordinates = [[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0]]
    polar_strike_coordinates_storm = [[0,0],[0,0],[0,0],[0,0],[0,0]]
    image_container = map.create_image(20,20, anchor="nw",image=A1_LARGE,)

image_container = map.create_image(20,20, anchor="nw",image=A1_LARGE,)

A1_Small = a1.resize((100, 100))
A2_Small = a2.resize((100, 100))
A3_Small = a3.resize((100, 100))

B1_Small = b1.resize((100, 100))
B2_Small = b2.resize((100, 100))
B3_Small = b3.resize((100, 100))

C1_Small = c1.resize((100, 100))
C2_Small = c2.resize((100, 100))
C3_Small = c3.resize((100, 100))

D1_Small = d1.resize((100, 100))
D2_Small = d2.resize((100, 100))
D3_Small = d3.resize((100, 100))

E1_Small = e1.resize((100, 100))
E2_Small = e2.resize((100, 100))
E3_Small = e3.resize((100, 100))

F1_Small = f1.resize((100, 100))
F2_Small = f2.resize((100, 100))
F3_Small = f3.resize((100, 100))


A1_button=ImageTk.PhotoImage(A1_Small)
A2_button=ImageTk.PhotoImage(A2_Small)
A3_button=ImageTk.PhotoImage(A3_Small)

B1_button=ImageTk.PhotoImage(B1_Small)
B2_button=ImageTk.PhotoImage(B2_Small)
B3_button=ImageTk.PhotoImage(B3_Small)

C1_button=ImageTk.PhotoImage(C1_Small)
C2_button=ImageTk.PhotoImage(C2_Small)
C3_button=ImageTk.PhotoImage(C3_Small)

D1_button=ImageTk.PhotoImage(D1_Small)
D2_button=ImageTk.PhotoImage(D2_Small)
D3_button=ImageTk.PhotoImage(D3_Small)

E1_button=ImageTk.PhotoImage(E1_Small)
E2_button=ImageTk.PhotoImage(E2_Small)
E3_button=ImageTk.PhotoImage(E3_Small)

F1_button=ImageTk.PhotoImage(F1_Small)
F2_button=ImageTk.PhotoImage(F2_Small)
F3_button=ImageTk.PhotoImage(F3_Small)



A1= Button(win, image=A1_button,command= lambda: switchMap(A1_LARGE), borderwidth=0)
A2= Button(win, image=A2_button,command= lambda: switchMap(A2_LARGE), borderwidth=0)
A3= Button(win, image=A3_button,command= lambda: switchMap(A3_LARGE), borderwidth=0)

B1= Button(win, image=B1_button,command= lambda: switchMap(B1_LARGE), borderwidth=0)
B2= Button(win, image=B2_button,command= lambda: switchMap(B2_LARGE), borderwidth=0)
B3= Button(win, image=B3_button,command= lambda: switchMap(B3_LARGE), borderwidth=0)

C1= Button(win, image=C1_button,command= lambda: switchMap(C1_LARGE), borderwidth=0)
C2= Button(win, image=C2_button,command= lambda: switchMap(C2_LARGE), borderwidth=0)
C3= Button(win, image=C3_button,command= lambda: switchMap(C3_LARGE), borderwidth=0)

D1= Button(win, image=D1_button,command= lambda: switchMap(D1_LARGE), borderwidth=0)
D2= Button(win, image=D2_button,command= lambda: switchMap(D2_LARGE), borderwidth=0)
D3= Button(win, image=D3_button,command= lambda: switchMap(D3_LARGE), borderwidth=0)

E1= Button(win, image=E1_button,command= lambda: switchMap(E1_LARGE), borderwidth=0)
E2= Button(win, image=E2_button,command= lambda: switchMap(E2_LARGE), borderwidth=0)
E3= Button(win, image=E3_button,command= lambda: switchMap(E3_LARGE), borderwidth=0)

F1= Button(win, image=F1_button,command= lambda: switchMap(F1_LARGE), borderwidth=0)
F2= Button(win, image=F2_button,command= lambda: switchMap(F2_LARGE), borderwidth=0)
F3= Button(win, image=F3_button,command= lambda: switchMap(F3_LARGE), borderwidth=0)

A1.grid(row=1, column=2)
A2.grid(row=1, column=3)
A3.grid(row=1, column=4)

B1.grid(row=2, column=2)
B2.grid(row=2, column=3)
B3.grid(row=2, column=4)

C1.grid(row=3, column=2)
C2.grid(row=3, column=3)
C3.grid(row=3, column=4)

D1.grid(row=4, column=2)
D2.grid(row=4, column=3)
D3.grid(row=4, column=4)

E1.grid(row=5, column=2)
E2.grid(row=5, column=3)
E3.grid(row=5, column=4)

F1.grid(row=6, column=2)
F2.grid(row=6, column=3)
F3.grid(row=6, column=4)

CLEAR_POINTS = tk.Button(win, text ="Clear Points", command = clear_points)
CLEAR_POINTS.grid(row=7, column=4)


def getAngle(a, b, c):
    ang = math.degrees(math.atan2(c[1]-b[1], c[0]-b[0]) - math.atan2(a[1]-b[1], a[0]-b[0]))
    return ang + 360 if ang < 0 else ang

def motion(event):
    global current_position
    current_position = [event.x,event.y]


def leftclick(event):
    global current_position
    global home_position
    global first_position
    global image_container
    global point_index
    global polar_strike_coordinates
    global polar_strike_coordinates_storm

    print (current_position)
    if point_index == 0:
        map.create_oval(current_position[0] - 3, current_position[1]-3, current_position[0]+3, current_position[1]+3, fill='#FFFF00')
        map.create_oval(current_position[0] - 230, current_position[1]-230, current_position[0]+230, current_position[1]+230)
        map.create_oval(current_position[0] - 30, current_position[1]-30, current_position[0]+30, current_position[1]+30)
        home_position = current_position
        point_index = point_index + 1
    elif point_index == 1:
        map.create_oval(current_position[0] - 3, current_position[1]-3, current_position[0]+3, current_position[1]+3, fill='#FF0000')

        distances[point_index-1] = math.sqrt((home_position[0] - current_position[0])**2 + (home_position[1] - current_position[1])**2 )
        #print(distances[point_index])
        first_position = current_position
        polar_strike_coordinates[point_index-1][0] = 0
        polar_strike_coordinates[point_index-1][1] = math.sqrt((home_position[0] - current_position[0])**2 + (home_position[1] - current_position[1])**2 )
        point_index = point_index + 1
    elif point_index > 1:
        map.create_oval(current_position[0] - 3, current_position[1]-3, current_position[0]+3, current_position[1]+3, fill='#FF0000')
        distances[point_index-1] = math.sqrt((home_position[0] - current_position[0])**2 + (home_position[1] - current_position[1])**2 )
        #print(getAngle(first_position, home_position, current_position))
        azimuth_angle = getAngle(first_position, home_position, current_position)
        if azimuth_angle > 180:
            polar_strike_coordinates[point_index-1][0] = azimuth_angle -360
        elif azimuth_angle < 180:
            polar_strike_coordinates[point_index-1][0] = azimuth_angle
        polar_strike_coordinates[point_index-1][1] = math.sqrt((home_position[0] - current_position[0])**2 + (home_position[1] - current_position[1])**2 )
        first_position = current_position
        point_index = point_index + 1
        print(polar_strike_coordinates)



def toggle_rounds():
    pydirectinput.keyDown('r')
    time.sleep(0.05)
    pydirectinput.keyUp('r')
    time.sleep(1)

def fire_round():
    pydirectinput.mouseDown( button='left')
    time.sleep(0.1)
    pydirectinput.mouseUp( button='left')
    time.sleep(2)


def slide_up_angle(distance):

    pydirectinput.moveRel(0, -distance, relative=True)


def slide_up_angle_fine(distance):

    for x in range(distance):
        pydirectinput.moveRel(1, 0, relative=True)
        pydirectinput.moveRel(0, -distance, relative=True)

def mortar_sequence():
    fire_round()
    toggle_rounds()
    toggle_rounds()

def swipe_azimuth(angle):
    pydirectinput.moveRel(angle, 0, relative=True)
    #for x in range(angle):
    #    pydirectinput.moveRel(1, 0, relative=True)

def fire_sequence():
    #full 360 range for azimuth is 7855 points which means 1 degree is 7855/360 = 21.82
    time.sleep(10)
    pydirectinput.mouseDown( button='right')
    time.sleep(2)
    toggle_rounds()
    time.sleep(1)
    pydirectinput.moveRel(0, 400, relative=True)

    for x in range(point_index):
        if polar_strike_coordinates[x][1] != 0:
            slide_up_angle(int(polar_strike_coordinates[x][1]/1.275))
            swipe_azimuth(int(polar_strike_coordinates[x][0]*21.82))
            mortar_sequence()
            pydirectinput.moveRel(0, 400, relative=True)

    pydirectinput.mouseUp(button='right')



FIRE = tk.Button(win, text ="FIRE!", command = fire_sequence)
FIRE.grid(row=7, column=3)


map.bind('<Motion>', motion)
map.bind("<Button-1>", leftclick)

win.mainloop()
