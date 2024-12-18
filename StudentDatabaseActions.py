# Programmers: Joseph Rydberg and Teresa Fischer
# Date: 12-19-2024
# Python Final Project Page 2

import sqlite3
import tkinter

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

    # display the information in the database
    database_label = tkinter.Label(frame1, text='Student Database', font=('Times New Roman', 18, 'bold') )
    dividing_line = tkinter.Label(frame2, text='-------------------------------------------------------')
    show_database_button = tkinter.Button(frame3, text='Show Current Database Info', command=show_database)

    # display actions user can take
    add_button = tkinter.Button(frame4, text='Add Info', command=add_info)
    edit_button = tkinter.Button(frame5, text='Edit Info', command=edit_info)
    delete_button = tkinter.Button(frame6, text='Delete Info', command=delete_info)
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
    # create window
    data_window = tkinter.Tk()
    data_window.title('Student Database')

    frame1 = tkinter.Frame(data_window)
    frame2 = tkinter.Frame(data_window)

    title = tkinter.Label(frame1, text='Student Database', font=('Normal', 14))

    conn = sqlite3.connect('studentDatabase.db')
    cur1 = conn.cursor()
    cur1.execute("SELECT * FROM studentInfo")
    rows = cur1.fetchall()
    for row in rows:
        label_test = tkinter.Label(frame2, text=f'{row[0]:}:{row[1]:10}{row[2]:10}{row[3]:10}{row[4]:10}{row[5]:15}{row[6]:10}')

    title.pack(side='left')
    label_test.pack(side='left')

    frame1.pack()
    frame2.pack()


# Add info function - allows user to add info to the database
def add_info():
    # *add: have 7 text inputs that are requesting the info then when the “add” button is pressed add inputs into the student info class to then be added to the database
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
    window3 = tkinter.Tk()
    window3.title('Edit Info')

    frame1 = tkinter.Frame(window3)
    frame2 = tkinter.Frame(window3)
    frame3 = tkinter.Frame(window3)
    frame4 = tkinter.Frame(window3)
    frame5 = tkinter.Frame(window3)

    main_label = tkinter.Label(frame1, text='Edit Information', font=('Normal', 14))
    row_label = tkinter.Label(frame2, text='Row')
    row_entry = tkinter.Entry(frame2)
    column_label = tkinter.Label(frame3, text='Column')
    column_entry = tkinter.Entry(frame3)
    edit_label = tkinter.Label(frame4, text='Enter Information')
    edit_entry = tkinter.Entry(frame4)
    edit = tkinter.Button(frame5, text='Edit')

    main_label.pack(side='left')
    row_label.pack(side='left')
    row_entry.pack(side='left')
    column_label.pack(side='left')
    column_entry.pack(side='left')
    edit_label.pack(side='left')
    edit_entry.pack(side='left')
    edit.pack(side='left')

    frame1.pack()
    frame2.pack()
    frame3.pack()
    frame4.pack()
    frame5.pack()

# Delete info function - allows user to delete information in the database
def delete_info():
    window4 = tkinter.Tk()
    window4.title('Edit Info')

    frame1 = tkinter.Frame(window4)
    frame2 = tkinter.Frame(window4)
    frame3 = tkinter.Frame(window4)

    main_label = tkinter.Label(frame1, text='Delete Student', font=('Normal', 14))
    row_label = tkinter.Label(frame2, text='Row ID')
    row_entry = tkinter.Entry(frame2)
    delete = tkinter.Button(frame3, text='Delete')

    main_label.pack(side='left')
    row_label.pack(side='left')
    row_entry.pack(side='left')
    delete.pack(side='left')

    frame1.pack()
    frame2.pack()
    frame3.pack()


if __name__ == '__main__':
    main()

    