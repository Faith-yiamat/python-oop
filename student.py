class Student:
 school = "AkiraChix"
 def __init__(self,first_name,last_name, age,country, code):
            self.first_name = first_name
            self.last_name = last_name
            self.age = age
            self.country = country
            self.code = code
 def greet_student(self):
       greeting = f"Hello {self.first_name} welcome to {self.school}. Your code is {self.code}" 
       return greeting 
 def display_student_Full_Name(self):
       full_name = f"Your name is {self.first_name} {self.last_name}" 
       return full_name
 def  enrol_student(self):
       enrol =  f"Hello {self.first_name} {self.last_name}welcome to {self.school}. Your code is {self.code}"  
       return enrol
 def initials (self):
       initials = f"Hello {self.first_name[0]} {self.last_name[0]}"
       return initials
         
       
 
    # instance variables enabkes us to create a multiple instances of a class each with its own dynamic/unique data.
    #  for a class to accepts instance variables you add a constructor. and the constructor is created by add image  __init__ method
    # __init __ method is a short form of initiate
    # the first argument for the __init_ method is always self followed by arguments representing the instance variables
    # Class Methods
    # They are used to define the behavour of a class object
    # They are defined as functions inside the body of the class 
    # The first argument ai usually self



    
     


            



