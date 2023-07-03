# Import tkinter to retrieve Pet's information
import tkinter as tk

# Creating the class Pet
class Pet:
    # Defining the objects for the Pet Class
    def __init__(self):
        self.__name = ""
        self.__animal_type = ""
        self.__age = 0

    def set_name(self, name):
        self.__name = name

    def set_animal_type(self, animal_type):
        self.__animal_type = animal_type

    def set_age(self, age):
        self.__age = age

    def get_name(self):
        return self.__name

    def get_animal_type(self):
        return self.__animal_type

    def get_age(self):
        return self.__age
    
def display_pet_info():
    # Retrieve the pet information from the entry fields
    name = name_entry.get()
    animal_type = animal_type_entry.get()
    age = age_entry.get()

    # Create a Pet object and set the information
    pet = Pet()
    pet.set_name(name)
    pet.set_animal_type(animal_type)
    pet.set_age(age)