# Programmers: Joseph Rydberg and Teresa Fischer
# Date: 12-19-2024
# Python Final Project Page 2

import sqlite3
import tkinter
import tkinter.messagebox

# mainline
def main():
    info_gui()

# create a GUI to display the information
def info_gui():
    # create main window
    main_window = tkinter.Tk()
    main_window.title('Student Database')

    # create frames
    frame1 = tkinter.Frame(main_window)
    frame2 = tkinter.Frame(main_window)
    frame3 = tkinter.Frame(main_window)
    frame4 = tkinter.Frame(main_window)
    frame5 = tkinter.Frame(main_window)
    frame6 = tkinter.Frame(main_window)
    frame7 = tkinter.Frame(main_window)
    frame8 = tkinter.Frame(main_window)

    # display the information in the database (in a messagebox?)
    database_label = tkinter.Label(frame1, text='Student Database', font=('Times New Roman', 18, 'bold') )
    dividing_line = tkinter.Label(frame2, text='-------------------------------------------------------')
    show_database_button = tkinter.Button(frame3, text='Show Current Database Info', command=show_database)

    # display actions user can take
    add_button = tkinter.Button(frame4, text='Add Info', command=add_info)
    edit_button = tkinter.Button(frame5, text='Edit Info')
    delete_button = tkinter.Button(frame6, text='Delete Info')
    dividing_line2 = tkinter.Label(frame7, text='-------------------------------------------------------' )
    exit_button = tkinter.Button(frame8, text='Exit Program', command=main_window.destroy)
    # pack the labels and buttons
    database_label.pack(side='left')
    dividing_line.pack(side='left')
    show_database_button.pack(side='left')
    add_button.pack(side='left')
    edit_button.pack(side='left')
    delete_button.pack(side='left')
    dividing_line2.pack(side='left')
    exit_button.pack(side='left')

    #pack the frames
    frame1.pack()
    frame2.pack()
    frame3.pack()
    frame4.pack()
    frame5.pack()
    frame6.pack()
    frame7.pack()
    frame8.pack()

    # Enter the mainloop
    tkinter.mainloop()

# Show database function
def show_database():
    tkinter.messagebox.showinfo('Student Database', 'Student Database \n Databse information will be put here')

# Add info function - allows user to add info to the database
def add_info():
    # *add: have 7 text inputs that are requesting the info then when the “add” button is pressed add inputs into the student info class to then be added to the database
    # *make a new screen show up? and then the user will enter the added information
    window2 = tkinter.Tk()
    window2.title('Add Info')

    # Create frames
    frame1 = tkinter.Frame(window2)
    frame2 = tkinter.Frame(window2)
    frame3 = tkinter.Frame(window2)
    frame4 = tkinter.Frame(window2)
    frame5 = tkinter.Frame(window2)
    frame6 = tkinter.Frame(window2)
    frame7 = tkinter.Frame(window2)
    frame8 = tkinter.Frame(window2)
    frame9 = tkinter.Frame(window2)

    # Labels and entries
    main_label = tkinter.Label(frame1, text='Add Information', font=('Normal', 14))
    id_label = tkinter.Label(frame2, text='ID:')
    id_entry = tkinter.Entry(frame2)
    first_label = tkinter.Label(frame3, text='First Name:')
    first_entry = tkinter.Entry(frame3)
    last_label = tkinter.Label(frame4, text='Last Name:')
    last_entry = tkinter.Entry(frame4)
    email_label = tkinter.Label(frame5, text='Email:')
    email_entry = tkinter.Entry(frame5)
    age_label = tkinter.Label(frame6, text='Age:')
    age_entry = tkinter.Entry(frame6)
    birth_label = tkinter.Label(frame7, text='Date of Birth (mm-dd-yyyy):')
    birth_entry = tkinter.Entry(frame7)
    location_label = tkinter.Label(frame8, text='Hometown (City, State(abbr.)): ')
    location_entry = tkinter.Entry(frame8)
    submit_info = tkinter.Button(frame9, text='Enter')


    # Pack labels and entries
    main_label.pack(side='left')
    id_label.pack(side='left')
    id_entry.pack(side='left')
    first_label.pack(side='left')
    first_entry.pack(side='left')
    last_label.pack(side='left')
    last_entry.pack(side='left')
    email_label.pack(side='left')
    email_entry.pack(side='left')
    age_label.pack(side='left')
    age_entry.pack(side='left')
    birth_label.pack(side='left')
    birth_entry.pack(side='left')
    location_label.pack(side='left')
    location_entry.pack(side='left')
    submit_info.pack(side='left')

    # Pack Frames
    frame1.pack()
    frame2.pack()
    frame3.pack()
    frame4.pack()
    frame5.pack()
    frame6.pack()
    frame7.pack()
    frame8.pack()
    frame9.pack()



# Edit info function - allows user to edit information in the database
def edit_info():
    # edit: 3 text inputs with button selecting the row id and column that’s being changed and then the new value they want it to be, update the database
    # make a new screen show up? and have the user enter the id they want to change

    pass

# Delete info function - allows user to delete information in the database
def delete_info():
    # delete: 1 text input with button that chooses which id row, and then removing it from the database
    pass


if __name__ == '__main__':
    main()

    