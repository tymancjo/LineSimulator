import tkinter as tk
from lineAlg import *

def main():

    # Drawing the shape of the line grid
    liniaBck = np.zeros((5,16))
    liniaBck[2,1:15] = 1

    liniaBck[1,2] = 1
    liniaBck[1,4] = 5
    liniaBck[1,6] = 1

    liniaBck[3,3] = 1
    liniaBck[3,7:12:2] = 1


    root = tk.Tk()
    app = mainApp(root, liniaBck)
    canvas = app.getCanvas()

    Adam = manipulator(liniaBck[:, 5:], 3, 4 , 'Adam', 10, 'red')
    Ewa = manipulator(liniaBck, 3, 7, 'Ewa', 20, 'green')
    Zdzich = manipulator(liniaBck, 3, 11, 'Zdzich', 30, 'orange')

    app.draw_window()
    root.mainloop()


if __name__ == '__main__':

    main()
