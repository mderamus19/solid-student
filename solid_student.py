# Define a Python class named Student. This class will have 5 properties.

# First name (string)
# Last name (string)
# Age (integer)
# Cohort number (integer)
# Full name (read-only string)
# Define getters for all properties.
# Define a setter for all but the read only property.
# Ensure that only the appropriate value can be assigned to each.
# The full name property should return first name and last name separated by
# a space. It's value cannot be set.
class Student:

        '''define getter and setter for first_name'''
        @property
        def first_name(self):
            try:
                return self.__first_name
            except AttributeError:
                return "Please enter a string for the first name"
        @first_name.setter
        def first_name(self,new_first_name):
            if type (new_first_name) is str:
                self.__first_name = new_first_name
            else:
                raise TypeError("Please provide a string value for the first name")

        '''define getter and setter for last_name'''

        @property
        def last_name(self):
            try:
                return self.__last_name
            except AttributeError:
                return 0
        @last_name.setter
        def last_name(self, new_last_name):
            if type (new_last_name) is str:
                self.__last_name = new_last_name
            else:
               raise TypeError("Please provide a string value for the last name")

        '''define getter and setter for age'''

        @property
        def age(self):
            try:
                return self.__age
            except AttributeError:
                return 0

        @age.setter
        def age(self, new_age):
            if type(new_age) is int:
                self.__age = new_age
            else:
                raise TypeError("Please provide an integer value for the age")

        '''define getter and setter for cohort_num'''
        @property
        def cohort_num(self):
            try:
                return self.__cohort_num
            except AttributeError:
                return 0

        @cohort_num.setter
        def cohort_num(self, new_cohort_num):
            if type(new_cohort_num) is int:
                self.__cohort_num = new_cohort_num
            else:
                raise TypeError("Please enter an integer value for the age")

        '''define getter for full_name. Full name will be created by combining first and last name.'''
        @property
        def full_name(self):
            try:
                return f"{self.__first_name} {self.__last_name}"
            except AttributeError:
                return "Student does not have a full name"

student = Student()
student.first_name = "Misty"
student.last_name = "DeRamus"
print(f"The student's name is: ",student.full_name)
# student.full_name="Fred Jones"
student.cohort_num = 33
# student.cohort_num = "7"
print(f"{student.first_name} is in cohort:",student.cohort_num)
# student.age = "45"
student.age = 45
print(f"Mrs. {student.last_name} is: ",student.age)
