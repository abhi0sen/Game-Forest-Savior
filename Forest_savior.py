"""Coded by - Abhisar Sen
Name of Game - Forest Savior F/S
Moto - Let's Save Trees and Live More
Date - 3rd June 2021
Version - 1.0"""


import tkinter as tk        # For the design of: front window; game mechanism
import math                # For some methamatical calculation
import time                 # For giving a pause in running screen so that user can see the movement.
from pygame import mixer   # For playing background music
mixer.init()
def music():
    """Adding background music"""
    mixer.music.load("music.mp3")
    mixer.music.play()
    
def tutorial():
    """Game tutorial"""
    new_win = tk.Tk()       # To make a new window for game tutorial
    new_win.title("Game Tutorial")
    new_win.resizable(0,0)
    new_win.geometry("300x200")
    information = '''!!How to Play!! \n
    right arrow (-->) = move right
    left arrow (<--) = move left
    space bar = shoot walls
    to win = defeat all the woodcutters
    to defeat = press 'space bar'
    for advance level-
    to defeat powerful wood cutter = hit 'space bar' twice!! 
    '''
    Game = tk.Label(new_win, text = information, fg = 'Brown', bg='light green')
    Game.pack()

base = tk.Tk()      # New window for game purpose
screen = tk.Canvas(base, width = 500, height = 500, bg = "black")   # To make game canvas screen
screen.pack()
count = 0       # Score counting
base.resizable(0,0)     # Fixing the size of game screen

def basic_level():
    """Functioning of basic level"""
    tk.Label(screen, text = "Press (-->) <=> move right",fg = "white", bg = "black").place(x = 350, y = 20)
    tk.Label(screen, text = "Press (<--) <=> move left",fg = "white", bg = "black").place(x = 5, y = 20)
    base.title("Forest savior- Basic Level")
    wood_cutter = "lumberjack.png"
    x_cod_wc = [355,100,200,250,140, 390,450, 290, 50, 190]     # List of different coordinate to place woodcutters at

    enemy = tk.PhotoImage(file = wood_cutter)
    enemy_pos = screen.create_image(x_cod_wc[1], 20, image = enemy)
    enemy_pos1 = screen.create_image(x_cod_wc[2], 10, image = enemy)
    enemy_pos2 = screen.create_image(x_cod_wc[3], 15, image = enemy)
    enemy_pos3 = screen.create_image(x_cod_wc[4], 5, image = enemy)
    enemy_pos4 = screen.create_image(x_cod_wc[5], 9, image = enemy)
    enemy_pos5 = screen.create_image(x_cod_wc[6], 25, image = enemy)

    forest = tk.PhotoImage(file = "grass_front.png")
    screen.create_image(250, 480, image = forest)
    hero = "wck.png"
    photo = tk.PhotoImage(file = hero)
    item = screen.create_image(250, 460, image = photo)

    def move_left(temp):    # to avoid the positional error "temp" is an temporary veriable
        """For moving the savior left side"""
        if pos[0]>10:
            screen.move(item, -20,0)
    def move_right(temp):
        """For moving the savior Right side"""
        if pos[0]<475:
            screen.move(item, 20,0)
    crash = False
    while True:     # Functioning of Woodcutters
        pos = screen.coords(item)
        wc_pos = screen.coords(enemy_pos)
        wc_pos1 = screen.coords(enemy_pos1)
        wc_pos2 = screen.coords(enemy_pos2)
        wc_pos3 = screen.coords(enemy_pos3)
        wc_pos4 = screen.coords(enemy_pos4)
        wc_pos5 = screen.coords(enemy_pos5)
        
        if wc_pos[1] <=470:
            screen.move(enemy_pos, 0, 10)
        elif wc_pos[1]>470 and count<210:
            crash = True
        if wc_pos1[1] <=470:
            screen.move(enemy_pos1, 0, 12)
        if wc_pos2[1] <=470:
            screen.move(enemy_pos2, 0, 15)
        if wc_pos3[1] <=470:
            screen.move(enemy_pos3, 0, 17)
        if wc_pos4[1] <=470:
            screen.move(enemy_pos4, 0, 25)
        if wc_pos5[1] <=470:
            screen.move(enemy_pos5, 0, 20)

        time.sleep(0.5)
        screen.bind_all("<KeyPress-Left>", move_left)   # To move savior in the left direction
        screen.bind_all("<KeyPress-Right>", move_right) # To move savior in the right direction
        
        def wall(temp):
            """For creating the wall so that savior can defend the trees"""
            global count
            rect = screen.create_rectangle(pos[0]-16, pos[1], pos[0]+16, pos[1]-15, fill = "brown")
            while True: # For the functioning of walls
                rect_pos = screen.coords(rect)

                if rect_pos[3]>=10:
                    screen.move(rect, 0, -10)
                    screen.update()
                    time.sleep(0.1)
                    
                    dist = math.sqrt(pow((rect_pos[0]-wc_pos[0]), 2)+pow((rect_pos[1]-wc_pos[1]), 2))//1         #Noticing the distance between woodcutter and walls
                    if dist<32:
                        screen.itemconfigure(rect, state = tk.HIDDEN)   # Hidding of walls and woodcutter after hitting each other
                        screen.itemconfigure(enemy_pos, state = tk.HIDDEN)
                        count +=20
                        break
                    
                    dist = math.sqrt(pow((rect_pos[0]-wc_pos1[0]), 2)+pow((rect_pos[1]-wc_pos1[1]), 2))//1
                    if dist<32:
                        screen.itemconfigure(rect, state = tk.HIDDEN)
                        screen.itemconfigure(enemy_pos1, state = tk.HIDDEN)
                        count+=20
                        break
                    
                    dist = math.sqrt(pow((rect_pos[0]-wc_pos2[0]), 2)+pow((rect_pos[1]-wc_pos2[1]), 2))//1
                    if dist<32:
                        screen.itemconfigure(rect, state = tk.HIDDEN)
                        screen.itemconfigure(enemy_pos2, state = tk.HIDDEN)
                        count +=20
                        break
                    
                    dist = math.sqrt(pow((rect_pos[0]-wc_pos3[0]), 2)+pow((rect_pos[1]-wc_pos3[1]), 2))//1
                    if dist<32:
                        screen.itemconfigure(rect, state = tk.HIDDEN)
                        screen.itemconfigure(enemy_pos3, state = tk.HIDDEN)
                        count+=20
                        break
                    
                    dist = math.sqrt(pow((rect_pos[0]-wc_pos4[0]), 2)+pow((rect_pos[1]-wc_pos4[1]), 2))//1
                    if dist<32:
                        screen.itemconfigure(rect, state = tk.HIDDEN)
                        screen.itemconfigure(enemy_pos4, state = tk.HIDDEN)
                        count+=20
                        break
                    
                    dist = math.sqrt(pow((rect_pos[0]-wc_pos5[0]), 2)+pow((rect_pos[1]-wc_pos5[1]), 2))//1
                    
                    if dist<32:
                        screen.itemconfigure(rect, state = tk.HIDDEN)
                        screen.itemconfigure(enemy_pos5, state = tk.HIDDEN)
                        count+=20
                        break
                else:
                    break
        score_count = 'SCORE - ', count
        Game_score = tk.Label(base, text = score_count, fg = 'Brown', bg='light green')
        Game_score.place(x= 0, y=0)
        Game_score.config(font = ("Courier, 10"))
        
        if count>=120:       # Reward, when a user wins the game
            game_finish= tk.Label(base, text = "!!!CONGRATULATIONS!!!\n YOU ARE THE SAVIOR OF FORESTS\n NOW YOU CAN LIVE MORE", fg = 'white', bg = 'green')
            game_finish.place(x= 150, y=150)
            break
        elif count<210 and crash == True:       # Feedback, when a user lost the game
            game_end= tk.Label(base, text = "!!!YOU LOST IT!!!\n FORESTS ARE NO MORE\n LIFE IS AT END ON THE EARTH", fg = 'white', bg = 'green')
            game_end.place(x= 150, y=150)
            break
        screen.bind_all("<KeyPress-space>", wall)
        base.update()   # To update the screen after certain changes in it
      
adv_pos1 = 50
adv_pos3 = 50
adv_pos5 = 50

def advance_level():
    """Functioning of advance level"""
    tk.Label(screen, text = "Press (-->) <=> move right",fg = "white", bg = "black").place(x = 350, y = 20)
    tk.Label(screen, text = "Press (<--) <=> move left",fg = "white", bg = "black").place(x = 5, y = 20)
    base.title("Forest savior- Advance Level")
    strong_man = "strong.png"
    wood_cutter = "lumberjack.png"
    x_cod_wc = [355,100,200,250,140, 390,450, 290, 50, 190]

    enemy = tk.PhotoImage(file = wood_cutter)
    strong_man = tk.PhotoImage(file = strong_man)
    enemy_pos = screen.create_image(x_cod_wc[1], 20, image = enemy)
    enemy_pos1 = screen.create_image(x_cod_wc[2], 10, image = strong_man)
    enemy_pos2 = screen.create_image(x_cod_wc[3], 15, image = enemy)
    enemy_pos3 = screen.create_image(x_cod_wc[4], 5, image = strong_man)
    enemy_pos4 = screen.create_image(x_cod_wc[5], 9, image = enemy)
    enemy_pos5 = screen.create_image(x_cod_wc[6], 25, image = strong_man)

    forest = tk.PhotoImage(file = "grass_front.png")
    screen.create_image(250, 480, image = forest)
    hero = "wck.png"
    photo = tk.PhotoImage(file = hero)
    item = screen.create_image(250, 460, image = photo)

    def move_left(temp):
        """For moving the savior Left side"""
        if pos[0]>10:
            screen.move(item, -20,0)
    def move_right(temp):
        """For moving the savior Right side"""
        if pos[0]<475:
            screen.move(item, 20,0)
    crash = False
    while True:      # Functioning of Woodcutters
        pos = screen.coords(item)
        wc_pos = screen.coords(enemy_pos)
        wc_pos1 = screen.coords(enemy_pos1)
        wc_pos2 = screen.coords(enemy_pos2)
        wc_pos3 = screen.coords(enemy_pos3)
        wc_pos4 = screen.coords(enemy_pos4)
        wc_pos5 = screen.coords(enemy_pos5)
        
        if wc_pos[1] <=470:
            screen.move(enemy_pos, 0, 10)
        elif wc_pos[1]>470 and count<210:
            crash = True
        if wc_pos1[1] <=470:
            screen.move(enemy_pos1, 0, 12)
        if wc_pos2[1] <=470:
            screen.move(enemy_pos2, 0, 15)
        if wc_pos3[1] <=470:
            screen.move(enemy_pos3, 0, 17)
        if wc_pos4[1] <=470:
            screen.move(enemy_pos4, 0, 25)
        if wc_pos5[1] <=470:
            screen.move(enemy_pos5, 0, 20)

        time.sleep(0.5)
        screen.bind_all("<KeyPress-Left>", move_left)       # To move savior in the left direction
        screen.bind_all("<KeyPress-Right>", move_right)     # To move savior in the right direction
        def wall(temp):
            """For creating the wall so that savior can defend the trees"""
            global count
            global adv_pos1, adv_pos3, adv_pos5
            rect = screen.create_rectangle(pos[0]-16, pos[1], pos[0]+16, pos[1]-15, fill = "brown")
            while True:
                rect_pos = screen.coords(rect)
                if rect_pos[3]>=10:
                    screen.move(rect, 0, -10)
                    screen.update()
                    time.sleep(0.1)
                    
                    dist = math.sqrt(pow((rect_pos[0]-wc_pos[0]), 2)+pow((rect_pos[1]-wc_pos[1]), 2))//1      #Noticing the distance between woodcutter and walls
                    if dist<32:
                        screen.itemconfigure(rect, state = tk.HIDDEN)        # Hidding of walls and woodcutter after hitting each other
                        screen.itemconfigure(enemy_pos, state = tk.HIDDEN)
                        count +=20
                        break
                    
                    dist = math.sqrt(pow((rect_pos[0]-wc_pos1[0]), 2)+pow((rect_pos[1]-wc_pos1[1]), 2))//1
                    if dist<32 and adv_pos1 <=0:
                        screen.itemconfigure(rect, state = tk.HIDDEN)
                        screen.itemconfigure(enemy_pos1, state = tk.HIDDEN)
                        count+=30
                        break
                    elif dist<32:
                        screen.itemconfigure(rect, state = tk.HIDDEN)
                        adv_pos1 -= 50
                        count += 20
                        break
                    dist = math.sqrt(pow((rect_pos[0]-wc_pos2[0]), 2)+pow((rect_pos[1]-wc_pos2[1]), 2))//1
                    if dist<32:
                        screen.itemconfigure(rect, state = tk.HIDDEN)
                        screen.itemconfigure(enemy_pos2, state = tk.HIDDEN)
                        count +=20
                        break
                    
                    dist = math.sqrt(pow((rect_pos[0]-wc_pos3[0]), 2)+pow((rect_pos[1]-wc_pos3[1]), 2))//1
                    if dist<32 and adv_pos3 <=0:
                        screen.itemconfigure(rect, state = tk.HIDDEN)
                        screen.itemconfigure(enemy_pos3, state = tk.HIDDEN)
                        count+=30
                        break
                    elif  dist<32:
                        screen.itemconfigure(rect, state = tk.HIDDEN)
                        adv_pos3 -= 50
                        count+=20
                        break
                    
                    dist = math.sqrt(pow((rect_pos[0]-wc_pos4[0]), 2)+pow((rect_pos[1]-wc_pos4[1]), 2))//1
                    
                    if dist<32:
                        screen.itemconfigure(rect, state = tk.HIDDEN)
                        screen.itemconfigure(enemy_pos4, state = tk.HIDDEN)
                        count+=20
                        break
                    
                    dist = math.sqrt(pow((rect_pos[0]-wc_pos5[0]), 2)+pow((rect_pos[1]-wc_pos5[1]), 2))//1
                    if dist<32 and adv_pos5 <=0:
                        screen.itemconfigure(rect, state = tk.HIDDEN)
                        screen.itemconfigure(enemy_pos5, state = tk.HIDDEN)
                        count+=30
                        break
                    elif dist<32:
                        screen.itemconfigure(rect, state = tk.HIDDEN)
                        adv_pos5 -= 50
                        count+=20
                        break
                        
                else:
                    break
        
        score_count = 'SCORE - ', count
        game_score = tk.Label(base, text = score_count, fg = 'Brown', bg='light green')
        game_score.place(x= 0, y=0)
        game_score.config(font = ("Courier, 10"))
        
        if count>=210:       # Reward, when a user wins the game
            game_finish= tk.Label(base, text = "!!!CONGRATULATIONS!!!\n YOU ARE THE SAVIOR OF FORESTS\n NOW YOU CAN LIVE MORE", fg = 'white', bg = 'green')
            game_finish.place(x= 150, y=150)
            break
        elif count<210 and crash == True:       # Feedback, when a user lost the game
            game_end= tk.Label(base, text = "!!!YOU LOST IT!!!\n FORESTS ARE NO MORE\n LIFE IS AT END ON THE EARTH", fg = 'white', bg = 'green')
            game_end.place(x= 150, y=150)
            break
        screen.bind_all("<KeyPress-space>", wall)
        base.update()       # To update the screen after certain changes in it


code_base = tk.Toplevel()
code_base.title("Forest Savior")
code_base.resizable(0,0)

can = tk.Canvas(code_base, width = 450, height = 350, bg = "black")  # Game Screen
can.pack()

background = tk.PhotoImage(file = "de-for.png")
can.create_image(225,175, image = background)

"""game Label"""
game_label = tk.Label(can, text = "Forest Savior", fg = 'Brown', bg='light green')
game_label.place(x= 120, y =20)
game_label.config(font =("Courier", 20))

message = tk.Label(can, text = "Let's Save Our Planet", fg = 'White', bg = "black")
message.place(x = 160, y = 70)

"""Button options"""
game = tk.Label(can, text = "Game Level", fg = 'Brown', bg='light green')
game.place(x = 185, y = 110)

basic_game = tk.Button(can, text = "Basic", fg = "white", bg = "black",command=basic_level)
basic_game.place(x = 200, y = 145)

advanced_game = tk.Button(can, text = "Advance", fg = "white", bg = "black", command=advance_level)
advanced_game.place(x = 190, y = 175)

option_list = tk.Label(can, text = "Options", fg = 'Brown', bg='light green')
option_list.place(x = 195, y = 225)

music_bg = tk.Button(can, text = "play sound", fg = "white", bg = "black", command=music)
music_bg.place(x = 185, y = 260)

game_info = tk.Button(can, text = "Game Tutorial", fg = "white", bg = "black", command=tutorial)
game_info.place(x= 177, y=290)

code_base.update()
a = True
if a:
    code_base.mainloop()    # To keep the canvas screen visible till the user close it