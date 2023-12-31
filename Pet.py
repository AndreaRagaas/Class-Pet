# Import tkinter to retrieve Pet's information
import tkinter as tk

# Import messagebox to show Pet's information
from tkinter import messagebox

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

    # Display the pet's information in a message box
    messagebox.showinfo("Pet Information", f"Name: {pet.get_name()}\nAnimal Type: {pet.get_animal_type()}\nAge: {pet.get_age()}")

# Create the main window
window = tk.Tk()
window.title("Pet Information")

# Create labels and entry fields for name, animal type, and age
name_label = tk.Label(window, text="Name:")
name_label.pack()
name_entry = tk.Entry(window)
name_entry.pack()

animal_type_label = tk.Label(window, text="Animal Type:")
animal_type_label.pack()
animal_type_entry = tk.Entry(window)
animal_type_entry.pack()

age_label = tk.Label(window, text="Age:")
age_label.pack()
age_entry = tk.Entry(window)
age_entry.pack()

# Create a button to display the pet information
submit_button = tk.Button(window, text="Submit", command=display_pet_info)
submit_button.pack()

# Create an instance to run the main window's event loop
window.mainloop()