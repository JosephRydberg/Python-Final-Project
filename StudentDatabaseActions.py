# Programmers: Joseph Rydberg and Teresa Fischer
# Date: 12-19-2024
# Python Final Project

import sqlite3
import tkinter
import tkinter.messagebox

# create a GUI to display the information
def info_gui():
    # creates main window
    main_window = tkinter.Tk()
    main_window.title('Student Database')
    # display the information in the database (in a messagebox?)
    # display actions user can take
    # add: have 7 text inputs that are requesting the info then when the “add” button is pressed add inputs into the student info class to then be added to the database
    # edit: 3 text inputs with button selecting the row id and column that’s being changed and then the new value they want it to be, update the database
    # delete: 1 text input with button that chooses which id row, and then removing it from the database