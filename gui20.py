import tkinter as tk
from lineAlg import *

def creataManipulator(root,array, row, col, name, iD, canvas, color):
    newManipulator = manipulator(array, row, col, name, iD, color)
    newWindow = tk.Toplevel(root)
    sterNewmanipulator = controlWindow(newWindow,
                        newManipulator, array, canvas)
    return newManipulator


def main():

    # Drawing the shape of the line grid
    liniaBck = np.zeros((5,16))
    liniaBck[2,1:15] = 1

    liniaBck[1,2] = 1
    liniaBck[1,4] = 1
    liniaBck[1,6] = 1

    liniaBck[3,3] = 1
    liniaBck[3,7:12:2] = 1


    root = tk.Tk()
    app = mainApp(root, liniaBck)
    canvas = app.getCanvas()

    Adam = creataManipulator(root,liniaBck,2,1,'Adam',10, canvas, 'red')
    Ewa  = creataManipulator(root,liniaBck,3,7,'Ewa',20, canvas, 'green')
    Zdzich  = creataManipulator(root,liniaBck,3,11,'Zdzich',30, canvas, 'orange')


    app.draw_window()
    root.mainloop()


if __name__ == '__main__':

    main()
