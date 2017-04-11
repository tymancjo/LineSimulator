import numpy as np
import matplotlib
import pandas as pd

import tkinter as tk

def printArray(theArray, theCanvas):
    # col = theArray.shape[1]
    # print(theArray)
    #
    # for x in range(col):
    #     print('\r')

    n_printTheArray(dataArray=theArray, canvas=theCanvas)



# Procedure that plot the array to canvas
def n_printTheArray(dataArray, canvas):
    '''
    This procedure allows to print the array back to the graphical board
    usefull for redraw or draw loaded data
    Inputs:
    dataArray -  the array to display on canvas
    canvas - tkinter canvas object
    '''

    # Let's check the size
    elementsInY = dataArray.shape[0]
    elementsInX = dataArray.shape[1]

    # canvasHeight = 600
    # canvasWidth  = 800
    canvasWidth  = canvas.winfo_width()
    if canvasWidth == 1:
        canvasWidth = 800
    canvasHeight = canvas.winfo_height()
    if canvasHeight ==1:
        canvasHeight = 600

    dX = canvasWidth / elementsInX
    dY = canvasHeight / elementsInY

    # Cleaning up the whole canvas space by drawing a white rectangle
    canvas.create_rectangle(0, 0, canvasWidth, canvasHeight, fill="navy", outline="gray")

    for Row in range(elementsInY):
        for Col in range(elementsInX):
            if dataArray[Row][Col] == 1:
                fillColor = "gray"
                canvas.create_rectangle((Col)*dX, (Row)*dY,
                    (Col)*dX+dX, (Row)*dY+dY, fill=fillColor, outline="white")

            elif dataArray[Row][Col] >= 10:

                fillColor = 'black'

                iD = dataArray[Row][Col]
                for mani in manipulator.listOfManipulators:
                    if iD == mani.iD:
                        fillColor = mani.color

                canvas.create_rectangle((Col)*dX, (Row)*dY,
                    (Col)*dX+dX, (Row)*dY+dY, fill=fillColor, outline="white")

# ####################
# From here Classes ;)
# ####################




class mainApp:
    '''Tgis is the class for the Main window of the App'''
    canvas = None
    moveArray = None

    def __init__(self, master, moveArray):
        self.master = master
        self.moveArray = moveArray
        self.frame = tk.Frame(self.master)
        self.button1 = tk.Button(self.frame, text = 'Quit All!', width = 25, command = self.new_window)
        self.button1.pack()
        self.button1 = tk.Button(self.frame,
                text = 'Draw', width = 25, command = self.draw_window)
        self.button1.pack()

        self.canvas = tk.Canvas(master,
                   width=800,
                   height=600)
        self.canvas.configure(background='navy')
        self.canvas.pack()
        self.master.tk_setPalette(background='#ececec')
        self.master.title('Transport Simulator - v00')

        self.frame.pack()

    def new_window(self):
        self.master.destroy()

    def draw_window(self):
        n_printTheArray(self.moveArray, self.canvas)


    def getCanvas(self):
        return self.canvas

class controlWindow:
    '''This is a control window object for manipulators'''
    manipulator = None
    moveArray = None

    def __init__(self, master, manipulator, moveArray, canvas):
        self.manipulator = manipulator
        self.moveArray = moveArray
        self.master = master
        self.canvas = canvas

        self.frame = tk.Frame(self.master, bg=self.manipulator.color)

        self.nButton = tk.Button(self.frame,
                            text = 'North', width = 5,
                            command = self.moveN ).grid(column=1, row=0)
        self.wButton = tk.Button(self.frame,
                            text = 'West', width = 5,
                            command = self.moveW).grid(column=0, row=1)

        self.eButton = tk.Button(self.frame,
                            text = 'East', width = 5,
                            command = self.moveE).grid(column=2, row=1)
        self.sButton = tk.Button(self.frame,
                            text = 'South', width = 5,
                            command = self.moveS).grid(column=1, row=2)

        self.master.title('{} ({})'.
                    format(self.manipulator.name, self.manipulator.iD ))

        self.frame.pack(padx=10, pady=10)

    def moveN(self):
        self.manipulator.move('N', self.moveArray)
        printArray(self.moveArray, self.canvas)

    def moveW(self):
        self.manipulator.move('W', self.moveArray)
        printArray(self.moveArray, self.canvas)

    def moveS(self):
        self.manipulator.move('S', self.moveArray)
        printArray(self.moveArray, self.canvas)

    def moveE(self):
        self.manipulator.move('E', self.moveArray)
        printArray(self.moveArray, self.canvas)

class manipulator:
    '''This class will cover all manipulator behaviours'''
    currentPositionRow=0
    currentPositionCol=0
    listOfManipulators = []

    directions = ['N','S','E','W']

    def __init__(self, envMatrix, posRow, posCol, name, iD, color='red'):
        '''This will set up our manipulator and place it on position'''

        manipulator.listOfManipulators.append(self)

        self.name = name
        self.iD = iD
        self.color = color

        if envMatrix[posRow,posCol] == 1:
            self.currentPositionRow = posRow
            self.currentPositionCol = posCol
            envMatrix[self.currentPositionRow, self.currentPositionCol] = self.iD
        else:
            print('Cannot place {} at position {} {}'
                    .format(name, posCol, posRow ))
            print('Object not created!')
            raise ValueError

    def __str__(self):
        return 'manipulator: {} is at row:{} col:{}'.format(self.name,
        self.currentPositionRow, self.currentPositionCol)

    def where(self):
        '''Just return a current position in matrix'''
        return self.currentPositionRow, self.currentPositionCol

    def checkMove(self,direction,envMatrix):
        if direction in self.directions:
            if direction == 'N':
                if envMatrix[self.currentPositionRow-1,
                             self.currentPositionCol] == 1:
                    return True
                else:
                    return False

            elif direction == 'S':
                if envMatrix[self.currentPositionRow+1,
                             self.currentPositionCol] == 1:
                    return True

                else:
                    return False

            elif direction == 'E':
                if envMatrix[self.currentPositionRow,
                             self.currentPositionCol+1] == 1:
                    return True
                else:
                    return False

            elif direction == 'W':
                if envMatrix[self.currentPositionRow,
                             self.currentPositionCol-1] == 1:
                    return True
                else:
                    return False
        else:
            return False

    def move(self, direction, envMatrix):
        '''This procedure moves the manipulator to new position if possible'''
        # Verified that we can move
        if self.checkMove(direction, envMatrix):
            # Placing 1 to background array in current position
            envMatrix[self.currentPositionRow, self.currentPositionCol] = 1

            if direction == 'N':
                self.currentPositionRow -=1

            elif direction == 'S':
                self.currentPositionRow +=1

            elif direction == 'E':
                self.currentPositionCol +=1

            elif direction == 'W':
                self.currentPositionCol -=1

            # Entering the name into new position
            envMatrix[self.currentPositionRow,
                        self.currentPositionCol] = self.iD

            return True
        else:
            return False



if __name__ == '__main__':
    '''This is the main loof executed if run directly'''

    # Drawing the shape of the line grid
    liniaBck = np.zeros((5,14))
    liniaBck[2,1:13] = 1

    liniaBck[1,2] = 1
    liniaBck[1,4] = 1
    liniaBck[1,6] = 1

    liniaBck[3,3] = 1
    liniaBck[3,7:10] = 1



    print(liniaBck)

    man01 = manipulator(liniaBck,3,3,'Adam')

    print(man01)
    print(man01.where())

    man01.move('W', liniaBck)
    print(man01)

    man01.move('N', liniaBck)
    print(man01)
    man01.move('E', liniaBck)
    print(man01)
