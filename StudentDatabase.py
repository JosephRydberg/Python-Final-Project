# Programmers: Joseph Rydberg and Teresa Fischer
# Date: 12-19-2024
# Python Final Project

import sqlite3

'''class StudentInfo:
    def __init__(self):
        # use init function with these variables
        #student id, first name, last name, email, age, birthday, hometown (town and then state)
        # add varables to database with primary key id'''

# mainline for displaying information and allowing user to edit the database
def main():
    pass
    # Connect to the database.
    # Get a database cursor.
    # Add the StudentInfo table.
    # Add rows to the StudentInfo table.
    # Commit the changes.
    # Display the info.
    # Close the connection.

def add_info_table():
    pass

def add_info():
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

    for row in student_info_list:
        pass
        # insert info into the database



# execute the main function
if __name__ =='__main__':
    main()