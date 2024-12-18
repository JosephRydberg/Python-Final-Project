# Programmers: Joseph Rydberg and Teresa Fischer
# Date: 12-19-2024
# Python Final Project

import sqlite3


# mainline for displaying information and allowing user to edit the database
def main():
    # Connect to the database.
    connection = sqlite3.connect('studentDatabase.db')

    # Get a database cursor.
    cursor = connection.cursor()

    # Add the StudentInfo table.
    add_info_table(cursor)

    # Add rows to the StudentInfo table.
    add_info(cursor)

    # read the info
    read_info(cursor)

    # Commit the changes.
    connection.commit()

    # Close the connection.
    connection.close()

#Reads files checking for info deleting previous and creating a new one with parameters
def add_info_table(cursor):
    cursor.execute('DROP TABLE IF EXISTS studentInfo')
    cursor.execute('CREATE TABLE studentInfo (ID INTEGER, First TEXT, Last TEXT, Email TEXT, Age INTEGER, Birth TEXT, Location TEXT)')

#Adds predefined information
def add_info(cursor):
    student_info_list = [(200, 'Mary', 'Smith', 'mary.smith@notrealmail.com', 18, '02-17-2006', 'Glencoe, MN'),
                         (201, 'John', 'Doe', 'john.doe@notrealmail.com', 17, '10-06-2007', 'Minneapolis, MN'),
                         (202, 'James', 'Brown', 'james.brown@notrealmail.com',  19, '11-16-2005', 'Montevideo, MN'),
                         (203, 'Leah', 'Martin', 'leah.martin@notrealmail.com', 18, '07-30-2006', 'Rochester, MN'),
                         (204, 'Noah', 'Wilson', 'noah.wilson@notrealmail.com', 18, '05-20-2006', 'Lakeville, MN'),
                         (205, 'Amy', 'Johnson', 'amy.johnson@notrealmail.com', 19, '12-02-2005', 'Edina, MN'),
                         (206, 'William', 'Taylor', 'william.taylor@notrealmail.com', 17, '09-18-2007', 'Duluth, MN'),
                         (207, 'Jacob', 'Jones', 'jacob.jones@notrealmail.com', 18, '05-05-2006', 'Mankato, MN'),
                         (208, 'Emma', 'Jackson', 'emma.jackson@notrealmail.com', 17, '06-01-2007', 'Anoka, MN'),
                         (209, 'Henry', 'Miller', 'henry.miller@notrealmail.com', 18, '10-23-2006', 'Minnetonka, MN')]
    #Adds information into the database
    for row in student_info_list:
        # insert info into the database
        cursor.execute('''INSERT INTO studentInfo (ID, First, Last, Email, Age, Birth, Location) VALUES (?, ?, ?, ?, ?, ?, ?)''', (row[0], row[1], row[2], row[3], row[4], row[5], row[6]))

#Reads information into print statement
def read_info(cursor):
    cursor.execute('SELECT * FROM studentInfo')
    results = cursor.fetchall()
    for row in results:
        print(f'{row[0]:}:{row[1]:10}{row[2]:10}{row[3]:10}{row[4]:10}{row[5]:15}{row[6]:10}')

# execute the main function
if __name__ =='__main__':
    main()