class Contact:
    def __init__(self, name, email):
        self.name = name
        self.email = email

    def get_name(self):
        return self.name

    def get_email(self):
        return self.email

    def set_name(self, name):
        self.name = name

    def set_email(self, email):
        self.email = email

# StudentContact is subclass for Contact class
class StudentContact(Contact):
    def __init__(self, name, email, major, career_interest):
        super().__init__(name, email)  # Call the parent class constructor
        self.number_of_courses = None
        self.major = major
        self.career_interest = career_interest

    def set_number_of_courses(self, num_courses):
        self.number_of_courses = num_courses

    def get_number_of_courses(self):
        return self.number_of_courses

    def get_major(self):
        return self.major

    def get_career_interest(self):
        return self.career_interest

    def set_major(self, major):
        self.major = major

    def set_career_interest(self, career_interest):
        self.career_interest = career_interest
        
        
        
# Create a Contact object
contact_person = Contact(input('Enter your Name: '), input('Enter your Email ID: '))

print("************************************************************")

# Get and print contact_person name and email
print("Name: ", contact_person.get_name())
print("Email: ", contact_person.get_email())

print("************************************************************")

# Set new name and email for contact person
contact_person.set_name(input('Enter Name to be updated: '))
contact_person.set_email(input('Enter Email ID to be updated: '))

print("************************************************************")

# Get and print the updated name and email
print("Updated Name: ", contact_person.get_name())
print("Updated Email: ", contact_person.get_email())

print("************************************************************")

# Create a StudentContact object
student_contact_person = StudentContact(contact_person.get_name(),  contact_person.get_email(), input('Enter Major: '), input('Enter Career Intrest: ')) # Name and email id is taken from Contact class and major and career intrest from the user as user input

# Set the number of courses for student_contact_person
student_contact_person.set_number_of_courses(input('Enter number of courses to be studied: '))

print("************************************************************")

# Get and print student_contact_person information
print("Student Name:", student_contact_person.get_name()) #Get name directly from Contact
print("Student Email:", student_contact_person.get_email()) #Get email directly from Contact
print("Student Major:", student_contact_person.get_major())
print("Student Career Interest:", student_contact_person.get_career_interest())
print("Number of Courses:", student_contact_person.get_number_of_courses())

print("************************************************************")

# Update student_contact_person major and career interest
student_contact_person.set_major(input('Enter major for StudentContact subclass to be updated: '))
student_contact_person.set_career_interest(input('Enter careed intrest for StudentContact subclass to be updated: '))

print("************************************************************")

# Get and print the updated student information
print("Updated Student Major:", student_contact_person.get_major())
print("Updated Student Career Interest:", student_contact_person.get_career_interest())

print("************************************************************")


#output
'''
Enter your Name: Arun
Enter your Email ID: arun@gmail.com
************************************************************
Name:  Arun
Email:  arun@gmail.com
************************************************************
Enter Name to be updated: Kumar
Enter Email ID to be updated: kumar@gmail.com
************************************************************
Updated Name:  Kumar
Updated Email:  kumar@gmail.com
************************************************************
Enter Major: Computer Science
Enter Career Intrest: Software Developer
Enter number of courses to be studied: 3
************************************************************
Student Name: Kumar
Student Email: kumar@gmail.com
Student Major: Computer Science
Student Career Interest: Software Developer
Number of Courses: 3
************************************************************
Enter major for StudentContact subclass to be updated: Information Science
Enter careed intrest for StudentContact subclass to be updated: Java Developer
************************************************************
Updated Student Major: Information Science
Updated Student Career Interest: Java Developer
************************************************************
> 
'''

'''
Explanation
A Python-based programme called the Contact Management System is used to handle contacts. Users may make and edit connections, including general contacts and targeted student contacts. This system provides as an illustration of Python's support for object-oriented programming (OOP) ideas and inheritance.

Features:
1. Contact Class
The Contact class is the parent class, representing basic contacts.
It includes methods to get and set the contact's name and email.

2. StudentContact Class
The StudentContact class is a subclass of Contact, designed for student contacts.
It extends the Contact class and includes additional attributes such as major, career interest, and the number of courses.
Methods are provided to get and set these attributes.

'''