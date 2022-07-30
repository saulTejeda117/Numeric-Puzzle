# Rompecabezas Numerico
from tkinter import *
import tkinter as tk

import random

import time
import tkinter

from datetime import datetime

def main():
    begin = datetime.now()
    mainWindow = tk.Tk()
    mainWindow.title('Rompecabezas Numerico')
    mainWindow.config(width = 380, height=380)
    mainWindow.resizable(False, False)
    
    def format_time(seconds):
        hour = int(seconds / 60 / 60)
        seconds -= hour*60*60
        minutes = int(seconds/60)
        seconds -= minutes*60
        print(f"{minutes:02d}:{seconds:02d}")
        return f"{minutes:02d}:{seconds:02d}"

    def get_time():
        currentSeconds = (datetime.now() - begin).total_seconds()
        print(currentSeconds)
        return format_time(int(currentSeconds))

    def refresh_time():
        actual_time.set(get_time())
        mainWindow.after(500, refresh_time)

    def shuffle_blocks(botonStart, botonScores):
        refresh_time()
        botonStart = mainWindow.nametowidget(botonStart)
        botonScores = mainWindow.nametowidget(botonScores)
        botonStart.place_forget()
        botonScores.place_forget()
        # List screen position
        positionList = ['20,60','110,60','200,60', '290,60','20,140','110,140','200,140', '290,140','20,220','110,220','200,220', '290,220','20,300','110,300','200,300', '290,300']
        newPositionList = [None]*16
        num = 1
        i = 0	
        # Create list of elements screen position
        while(i < len(positionList)):
            botonName = mainWindow.nametowidget('boton' + str(num))
            a = botonName.place_info()
            newPositionList
            # botonName.place_forget()
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

    def move_block(clickedButton): 
        tk.Label(mainWindow, )
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
            if(emptyButtonYPosition + 80 == clickedButtonYPosition):
                emptyButtonName.place_forget()
                clickedButtonName.place_forget()
                emptyButtonName.place(x=clickedButtonXPosition, y=clickedButtonYPosition)
                clickedButtonName.place(x=emptyButtonXPosition, y=emptyButtonYPosition)
            elif(emptyButtonYPosition - 80 == clickedButtonYPosition):
                emptyButtonName.place_forget()
                clickedButtonName.place_forget()
                emptyButtonName.place(x=clickedButtonXPosition, y=clickedButtonYPosition)
                clickedButtonName.place(x=emptyButtonXPosition, y=emptyButtonYPosition)
        elif(emptyButtonYPosition == clickedButtonYPosition):
            if(emptyButtonXPosition - 90 == clickedButtonXPosition):
                emptyButtonName.place_forget()
                clickedButtonName.place_forget()
                emptyButtonName.place(x=clickedButtonXPosition, y=clickedButtonYPosition)
                clickedButtonName.place(x=emptyButtonXPosition, y=emptyButtonYPosition)
            if(emptyButtonXPosition + 90 == clickedButtonXPosition):
                emptyButtonName.place_forget()
                clickedButtonName.place_forget()
                emptyButtonName.place(x=clickedButtonXPosition, y=clickedButtonYPosition)
                clickedButtonName.place(x=emptyButtonXPosition, y=emptyButtonYPosition)
    # Inicial position of the buttons
    actual_time = tk.StringVar(mainWindow, get_time()) 
    print(actual_time)
    xpos = 20 
    ypos = 60
    i = 1
    j=1
    numCasillas = 16
    
    tk.Label(text='Time: ' + str(actual_time), font=('Arial', 15), fg='#7F8C8D').place(x=5, y= 5)
    tk.Button(mainWindow, width=54,height=23, bg='#B2BABB', state='disabled', bd=0).place(x = 0, y = 40)
    while(i < numCasillas):
        while(j < 5):
            if(i==16):
                tk.Button(mainWindow, text = ' ', name = 'boton' + str(i), width=10, height=4, bd = 0, bg='#ffffff', state='disabled', font=('Helvetica', 9)).place(x = xpos, y = ypos)
            else:
                tk.Button(mainWindow, text = i, name = 'boton' + str(i), width=10, height=4, bd = 0, bg='#ffffff', command = lambda clickedButton = i: move_block(clickedButton), state='disabled', font=('Helvetica', 9)).place(x = xpos, y = ypos)
            xpos += 90
            i += 1
            j+=1
        xpos = 20
        ypos += 80
        j = 1
    def myMainLoop():
        refresh_time(mainWindow)
        mainWindow.after(1, myMainLoop)  
    tk.Button(mainWindow, text = 'Best Scores:', name= 'botonScores', width=25, height=10, command = shuffle_blocks, anchor=tkinter.N, state='disabled').place(relx=.5, rely=.5, anchor=CENTER)
    tk.Button(mainWindow, text = 'Start the Game!', name= 'botonStart', width=15, height=2, command = lambda botonStart = 'botonStart', botonScores = 'botonScores': shuffle_blocks(botonStart, botonScores)).place(relx=.5, rely=.6,anchor= CENTER)
    mainWindow.mainloop()
main()