import numpy as np
import matplotlib
import pandas as pd

import tkinter as tk

def printArray(theArray, theCanvas):
    '''Wrapper around graphic proint to give possibility for
     terminal feedback'''

    # col = theArray.shape[1]
    # print(theArray)

    # for x in range(col+1):
    #     print('\r')

    # n_printTheArray(dataArray=theArray, canvas=theCanvas)
    display(theArray, theCanvas)

def display(dataArray, canvas):
    colors = { 10: 'red', 20: 'green', 30: 'blue', 40: 'orange', 50: 'yellow' }
    bckColor = 'navy'

    # Let's check the size
    elementsInY = dataArray.shape[0]
    elementsInX = dataArray.shape[1]

    canvasWidth  = canvas.winfo_width()

    if canvasWidth == 1:
        canvasWidth = 800

    canvasHeight = canvas.winfo_height()

    if canvasHeight ==1:
        canvasHeight = 600

    dX = canvasWidth / elementsInX
    dY = canvasHeight / elementsInY

    # Cleaning up the whole canvas space by drawing a white rectangle
    canvas.create_rectangle(0, 0, canvasWidth, canvasHeight,
                                fill=bckColor)

    color = 'black' # jus to have it defined somehow

    for Row in range(elementsInY):
        for Col in range(elementsInX):

            currentElement = dataArray[Row][Col]
            lineZ = False
            lineX = False

            # Obsluga tla linii
            # Lets figure out the color first
            if currentElement > 0: # to not draw aything if zero

                if currentElement == 1:
                    color = 'silver' # this will be empty line space
                elif currentElement < 10: # this mean we are zawieszka
                    lineZ = True
                    color = 'gray'
                elif currentElement <100:
                    # here we are in range of manipulators
                    color = 'lime' # to have initially selected color
                    if currentElement % 10 > 0:
                        lineZ=True

                    currentElement = (currentElement // 10)*10
                    print('element: {}'.format(currentElement))
                    color = colors[currentElement]


                # Now we need to decode whts here really is
                # First lets check if we need to decode anything
                else: #if thats true we are caaying zawieszka
                    lineX = True
                    currentElement -= 100
                    currentElement = (currentElement // 10)*10
                    print('element: {}'.format(currentElement))
                    color = colors[currentElement]

                canvas.create_rectangle((Col)*dX, (Row)*dY,
                    (Col)*dX+dX, (Row)*dY+dY, fill=color,
                     outline="white")

                if lineZ:
                    canvas.create_line((Col)*dX, (Row)*dY,
                     (Col)*dX+dX, (Row)*dY+dY, fill='white', width=2)

                if lineX:
                    canvas.create_line((Col)*dX, (Row)*dY,
                     (Col)*dX+dX, (Row)*dY+dY, fill='white', width=2)
                    canvas.create_line((Col)*dX+dX, (Row)*dY,
                     (Col)*dX, (Row)*dY+dY, fill='white', width=2)



# ####################
# From here Classes ;)
# ####################
class recorder:
    '''This is a class to take care of displayin, recording and playing the
    main matrix of all elements'''

    colors = { 10: 'red', 20: 'green', 30: 'blue', 40: 'orange', 50: 'yellow' }


    def __init__(self, matrix, canvas):
        '''This function prepare the recorder object.
        Input:
        matrix - the array that keep the main data of the background system (line)
        canvas - tkinter canvas object that is used to draw the data (picture)
        '''
        self.bckColor = 'navy'
        self.dataArray = matrix
        self.canvas = canvas
        self.colors = recorder.colors




class mainApp:
    '''Tgis is the class for the Main window of the App'''
    canvas = None
    moveArray = None
    recorder = None

    def __init__(self, master, moveArray):
        self.master = master
        self.moveArray = moveArray
        self.frame = tk.Frame(self.master)
        self.button1 = tk.Button(self.frame, text = 'Quit All!',
                                    width = 25, command = self.new_window)
        self.button1.pack(side='left')
        self.button2 = tk.Button(self.frame,
                text = 'Redraw', width = 25, command = self.drawWindow)
        self.button2.pack(side='left')

        self.button3 = tk.Button(self.frame,
                text = 'Bring Controls', width = 25, command = self.showControls)
        self.button3.pack(side='left')

        self.cframe = tk.Frame(self.master)
        self.canvas = tk.Canvas(self.cframe,
                   width=800,
                   height=600)
        self.canvas.configure(background='navy')
        self.canvas.pack(fill='both', expand='yes')
        self.master.tk_setPalette(background='#ececec')
        self.master.title('Transport Simulator - v00')

        self.canvas.bind("<Configure>", self.drawWindow)

        self.cframe.pack(fill='both', expand='yes')
        self.frame.pack(fill='both', expand='no')


    def mebypass(self):
        print('Trying to prevent close')

    def new_window(self):
        self.master.destroy()

    def drawWindow(self, *arg):

        display(self.moveArray, self.canvas)

    def showControls(self):
        for window in controlWindow.listOfWindows:
            window.destroy()

        for manip in manipulator.listOfManipulators:
            manip.getControls(tk.Toplevel(self.master), self.moveArray, self.canvas )


    def getCanvas(self):
        return self.canvas

class recorederWindow:
    '''This is class for the window that will keep controls for the recorder'''

    def __init__(self, recorder):
        pass


class controlWindow:
    '''This is a control window object for manipulators'''
    manipulator = None
    moveArray = None
    listOfWindows = []

    def __init__(self, master, manipulator, moveArray, canvas):

        controlWindow.listOfWindows.append(self)

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

        self.gButton = tk.Button(self.frame,
                            text = 'Grab', width = 5,
                            command = self.grab).grid(column=1, row=1)

        self.master.title('{} ({})'.
                    format(self.manipulator.name, self.manipulator.iD ))

        self.frame.pack(padx=10, pady=10)

    def destroy(self):
        self.master.destroy()

    def mebypass(self):
        print('Trying to prevent close')

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

    def grab(self):
        self.manipulator.grab()
        printArray(self.moveArray, self.canvas)

class manipulator:
    '''This class will cover all manipulator behaviours'''
    currentPositionRow=0
    currentPositionCol=0
    listOfManipulators = []
    isGrab = False
    buforBck = 1

    directions = ['N','S','E','W']
    colors = { 10: 'red', 20: 'green', 30: 'blue', 40: 'orange', 50: 'yellow' }

    def __init__(self, envMatrix, posRow, posCol, name, iD, *arg):
        '''This will set up our manipulator and place it on position'''

        manipulator.listOfManipulators.append(self)
        self.envMatrix = envMatrix

        self.name = name
        self.iD = iD
        self.color = manipulator.colors[self.iD]

        if self.envMatrix[posRow,posCol] == 1:
            self.currentPositionRow = posRow
            self.currentPositionCol = posCol
            self.envMatrix[self.currentPositionRow, self.currentPositionCol] = self.iD
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

    def grab(self):
        if self.isGrab:
            self.isGrab = False
            self.iD -= self.buforBck

        else:
            if self.buforBck != 1:
                self.isGrab = True
                self.iD += self.buforBck
                print(self.iD)

        self.markPosition()

    def checkMove(self,direction,envMatrix):
        if direction in self.directions:
            # to prevent move with grab to othe place with zawieszka
            if self.isGrab:
                myRange = range(1,2)
            else:
                myRange = range(1,10)

            if direction == 'N':
                if envMatrix[self.currentPositionRow-1,
                             self.currentPositionCol] in myRange:
                    return True
                else:
                    return False

            elif direction == 'S':
                if envMatrix[self.currentPositionRow+1,
                             self.currentPositionCol] in myRange:
                    return True

                else:
                    return False

            elif direction == 'E':
                if envMatrix[self.currentPositionRow,
                             self.currentPositionCol+1] in myRange:
                    return True
                else:
                    return False

            elif direction == 'W':
                if envMatrix[self.currentPositionRow,
                             self.currentPositionCol-1] in myRange:
                    return True
                else:
                    return False
        else:
            return False

    def move(self, direction, *arg):
        '''This procedure moves the manipulator to new position if possible'''
        # Verified that we can move
        if self.checkMove(direction, self.envMatrix):

            # Placing buffored value to background array in current position
            if self.isGrab:
                self.envMatrix[self.currentPositionRow,
                            self.currentPositionCol] = 1
            else:
                self.envMatrix[self.currentPositionRow,
                            self.currentPositionCol] = self.buforBck

            if direction == 'N':
                self.currentPositionRow -=1

            elif direction == 'S':
                self.currentPositionRow +=1

            elif direction == 'E':
                self.currentPositionCol +=1

            elif direction == 'W':
                self.currentPositionCol -=1

            # Putting existing value in buffored
            if not(self.isGrab):
                self.buforBck = self.envMatrix[self.currentPositionRow,
                        self.currentPositionCol]

            # Entering the name into new position
            self.markPosition()

            return True
        else:
            return False

    def markPosition(self):
        '''Entering the name into new position
        Its doing it with the following logic:
        when the place was 1 - it puts just the manipulator iD
        if it was 2-9 (zawieszka) then it puts iD + wat it was
        if we have grab of zawieszka then we return iD manipulator
        + iD zawieszka + 100 '''

        if not(self.isGrab):
            if self.buforBck == 1:
                self.envMatrix[self.currentPositionRow,
                    self.currentPositionCol] = self.iD
            else:
                self.envMatrix[self.currentPositionRow,
                    self.currentPositionCol] = self.iD+self.buforBck
        else:
            self.envMatrix[self.currentPositionRow,
                    self.currentPositionCol] = self.iD+100


    def getControls(self, master, moveArray, canvas):
        return controlWindow(master, self, moveArray, canvas)


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
