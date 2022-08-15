# Numeric Puzzle

# GUI dependencies
from tkinter import *
import tkinter
import tkinter as tk
from tkinter import messagebox

# file exists validation 
import os

import random

# count seconds dependencies
from datetime import datetime

def main():
    # principal interface features
    mainWindow = tk.Tk()
    mainWindow.title('Numeric Puzzle')
    mainWindow.config(width = 380, height=380)
    mainWindow.resizable(False, False)

    # read the file with the best time 
    with open("RecordsList.txt") as f: 
        lines = f.readlines()

    # format time /minute:seconds/
    def format_time(seconds):
        hour = int(seconds / 60 / 60)
        seconds -= hour*60*60
        minutes = int(seconds/60)
        seconds -= minutes*60
        return f"{minutes:02d}:{seconds:02d}"

    def refresh_time():
        global begin
        global actual_time
        currentSeconds = (datetime.now() - begin).total_seconds()
        actual_time = format_time(int(currentSeconds))
        tk.Label(text = 'Time: ' + str(actual_time), font = ('Arial', 15), fg='#7F8C8D').place(x=5, y= 5)
        mainWindow.after(500, refresh_time)
    
    # check when 
    def validate_endposition():
        correctPos = 0
        # where buttons are locate
        positionList = ['20,60','110,60','200,60', '290,60','20,140','110,140','200,140', '290,140','20,220','110,220','200,220', '290,220','20,300','110,300','200,300', '290,300'] 
        i = 0
        num = 1
        while(i < len(positionList)):
            pos = positionList[i].split(',')
            x = pos[0]
            y = pos[1]
            botonName = mainWindow.nametowidget('boton' + str(num))
            buttonInfo = botonName.place_info()
            actualx, actualy = buttonInfo['x'], buttonInfo['y'] 
            if(actualx == pos[0] and actualy == pos[1]):
                correctPos += 1
            else:
                break
            i += 1
            num += 1
        mainWindow.after(500, validate_endposition)
        if(correctPos>=15):
            print(str(actual_time))
            fileExists = os.path.exists('RecordsList.txt')
            # check if records file txt exists
            # write a new record 
            if (fileExists == True):
                with open("RecordsList.txt", "w+") as f: f.write(str(actual_time)+'\n')
            else:
                with open("RecordsList.txt", "w+") as f: f.write(str(actual_time)+'\n')
            f.close()
            mainWindow.destroy()
            main()
            quit()    

    # starting the game
    def shuffle_blocks(botonStart, botonScores):
        global positionList
        # List screen elements position
        positionList = ['20,60','110,60','200,60', '290,60','20,140','110,140','200,140', '290,140','20,220','110,220','200,220', '290,220','20,300','110,300','200,300', '290,300']
        botonStart = mainWindow.nametowidget(botonStart)
        botonScores = mainWindow.nametowidget(botonScores)
        # Delete Score bar/Window Title/Start Button
        windowTitle.place_forget()
        botonStart.place_forget()
        botonScores.place_forget()
        newPositionList = [None]*16
        global begin 
        global actual_time
        # Start the time count
        begin = datetime.now()
        refresh_time()
        num = 1
        i = 0	
        # Create list of elements screen position
        while(i < len(positionList)):
            botonName = mainWindow.nametowidget('boton' + str(num))
            a = botonName.place_info()
            newPositionList
            newPosition = random.randint(0,15)
            if(positionList[newPosition] != None):
                position = positionList[newPosition]
                positionList[newPosition] = None
                newx, newy = position.split(',')
                newx = int(newx)
                newy = int(newy)
                botonName.place_forget()
                botonName.place(x = newx, y = newy)
                botonName.config(state = 'normal')
            else:
                while(positionList[newPosition] == None):
                    newPosition = random.randint(0,15)
                position = positionList[newPosition] 
                newx,newy = position.split(',')
                newx = int(newx)
                newy = int(newy)
                botonName.place_forget()
                botonName.place(x = newx, y = newy)
                botonName.config(state = 'normal')
            positionList[newPosition] = None 
            num+=1
            i+=1
        validate_endposition()     

    def move_block(clickedButton): 
        # Get the info of clicked button
        clickedButtonName = mainWindow.nametowidget('boton' + str(clickedButton))
        clickedButtonInfo = clickedButtonName.place_info()
        # Get empty button info
        emptyButtonName = mainWindow.nametowidget('boton' + str(16))
        emptyButtonInfo = emptyButtonName.place_info()
        # Clicked Button position declaration
        clickedButtonXPosition = int(clickedButtonInfo['x'])
        clickedButtonYPosition = int(clickedButtonInfo['y'])
        # Empty Button position declaration
        emptyButtonXPosition = int(emptyButtonInfo['x'])
        emptyButtonYPosition = int(emptyButtonInfo['y'])
        # Movement Validation
        if(emptyButtonXPosition == clickedButtonXPosition):
            # if a button can move to up position
            if(emptyButtonYPosition + 80 == clickedButtonYPosition):
                emptyButtonName.place_forget()
                clickedButtonName.place_forget()
                emptyButtonName.place(x = clickedButtonXPosition, y = clickedButtonYPosition)
                clickedButtonName.place(x = emptyButtonXPosition, y = emptyButtonYPosition)
            # if a button can move to down position
            elif(emptyButtonYPosition - 80 == clickedButtonYPosition):
                emptyButtonName.place_forget()
                clickedButtonName.place_forget()
                emptyButtonName.place(x = clickedButtonXPosition, y = clickedButtonYPosition)
                clickedButtonName.place(x = emptyButtonXPosition, y = emptyButtonYPosition)
            # if a button can move to left position
        elif(emptyButtonYPosition == clickedButtonYPosition):
            if(emptyButtonXPosition - 90 == clickedButtonXPosition):
                emptyButtonName.place_forget()
                clickedButtonName.place_forget()
                emptyButtonName.place(x = clickedButtonXPosition, y = clickedButtonYPosition)
                clickedButtonName.place(x = emptyButtonXPosition, y = emptyButtonYPosition)
            # if a button can move to right position
            if(emptyButtonXPosition + 90 == clickedButtonXPosition):
                emptyButtonName.place_forget()
                clickedButtonName.place_forget()
                emptyButtonName.place(x = clickedButtonXPosition, y = clickedButtonYPosition)
                clickedButtonName.place(x = emptyButtonXPosition, y = emptyButtonYPosition)
    # Title of th screen
    tk.Button(mainWindow, width = 54,height = 23, bg='#B2BABB', state = 'disabled', bd = 0).place(x = 0, y = 40)
    windowTitle = tk.Label(text = 'Numeric Puzzle', font = ('Arial', 15), fg = '#7F8C8D')
    windowTitle.place(x = 5, y= 5)
    # Inicial position of the buttons
    xpos = 20 
    ypos = 60
    i = 1
    j=1
    numCasillas = 16
    while(i < numCasillas):
        while(j < 5):
            if(i==16):
                tk.Button(mainWindow, text = ' ', name = 'boton' + str(i), width=10, height=4, bd = 0, bg='#ffffff', state='disabled', font=('Helvetica', 9)).place(x = xpos, y = ypos)
            else:
                tk.Button(mainWindow, text = i, name = 'boton' + str(i), width=10, height=4, bd = 0, bg='#ffffff', command = lambda clickedButton = i: move_block(clickedButton), state='disabled', font=('Helvetica', 9)).place(x = xpos, y = ypos)
            xpos += 90
            i += 1
            j += 1
        xpos = 20
        ypos += 80
        j = 1 
    tk.Button(mainWindow, text = 'Best Scores:' + '\n' + str(lines), name = 'botonScores', width = 25, height=10, anchor = tkinter.N, state='disabled').place(relx = .5, rely=.5, anchor = CENTER)
    tk.Button(mainWindow, text = 'Start the Game!', name = 'botonStart', width = 15, height = 2, command = lambda botonStart = 'botonStart', botonScores = 'botonScores': shuffle_blocks(botonStart, botonScores)).place(relx = .5, rely = .6,anchor = CENTER)
    mainWindow.mainloop()
main()
