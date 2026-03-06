"""
Author:         Syntax Savvy Duo (Wendy Gatica, Jeff Vukovits)
Date written:   2/19/26 
Assignment:     Final Project
Short Desc:     class definition of the Thermosafe system
"""
#imports the necessary libraries needed
import time
import tkinter as tk
from tkinter import PhotoImage
import os

#picture file path will be the same folder as the code
script_dir = os.path.dirname(os.path.abspath(__file__))
img_path = os.path.join(script_dir, "freezer.png")

class Thermosafe:
     temperature = 0
     clock = time.strftime("%H:%M %p")

     def updateClock(self):
          self.clock = time.strftime("%H:%M %p")

current_time = Thermosafe.clock
print ("Current time: " + current_time)

#user input "enter food type" and "enter weight" counts down to cool dish
class Cool_Down:
     food_types = ("Liquid", "Meat", "Vegetables")
     def __init__(self):
          self.food_types = input("Choose a type of food to cool down: \n1. Liquid \n2. Meat \n3. Vegetables \n")
          self.weight = int(input("Enter the approximate weight of the food as a whole number (in pounds): "))
          self.time_left = 0

          if self.food_types == self.food_types[0] and self.weight <= 5:
               self.time_left = 60
          elif self.food_types == self.food_types[0] and self.weight > 5:
               self.time_left = 120
          elif self.food_types == self.food_types[1] and self.weight <= 5:
               self.time_left = 120
          elif self.food_types == self.food_types[1] and self.weight > 5:
               self.time_left = 180
          elif self.food_types == self.food_types[2] and self.weight <= 5:
               self.time_left = 90
          elif self.food_types == self.food_types[2] and self.weight > 5:
               self.time_left = 120
          else:
               print("Invalid input. Please enter a valid food type and weight.")
               return

          while self.time_left != 0:
               self.time_left -= 1
               print(f"Time left: {self.time_left} seconds")
          if self.time_left == 0:
               print("Time's up! Food reached desired temperature.")
          else:
               print ("Current time: " + Thermosafe.clock)
          return
# ---- THIS IS THE BEGINNING OF WHAT I AM WORKING ON ----
#user input "enter catgory", enter item", "enter days" counts down to flash freeze for a number of days depending on category and item
class DeepFreeze:

     liquid = {
               "1": "Water", "2": "Popsicles", "3": "Ice Cream"
               }
     
     meat = {
               "1": "Beef", "2": "Chicken", "3": "Pork"
               }
     
     vegetables = {
               "1": "Greens", "2": "Carrots", "3": "Corn"
               }
     time_left = 0

     def __init__(self):
          self.category = input("Choose a category of food to flash freeze: \n1. Liquid \n2. Meat \n3. Vegetables \n")
          if self.category == "1":
               self.item = input("Choose an item to flash freeze: \n1. Water \n2. Popsicles \n3. Ice Cream \n")
          elif self.category == "2":
               self.item = input("Choose an item to flash freeze: \n1. Beef \n2. Chicken \n3. Pork \n")
          elif self.category == "3":
               self.item = input("Choose an item to flash freeze: \n1. Greens \n2. Carrots \n3. Corn \n")
          
          num_days = int(input("Enter the number of days you want to flash freeze the item for: "))
          self.time_left *= num_days

          while self.time_left != 0:
               self.time_left -= 1
               print(f"Time left: {self.time_left} seconds")
          if self.time_left == 0:
               print("Time's up! Food reached desired temperature.")
          else:
               print ("Current time: " + Thermosafe.clock)
          return
# --- THIS IS THE END OF WHAT I AM WORKING ON ---

setting = input("Choose a setting (1-3): \n1. Cool Down \n2. Deep Freeze \n3. Timed Freeze \n4. Cancel \n")

#user input "enter time" counts down
class Timed_Freeze:
     def __init__(self):
          self.time = int(input("Enter the desired cooling time (in seconds): "))
          self.time_left = self.time
          
          while self.time_left != 0:
               self.time_left -= 1
               print(f"Time left: {self.time_left} seconds")
          if self.time_left == 0:
               print("Time's up! Food reached desired temperature.")
          else:
               print ("Current time: " + Thermosafe.clock)

#define functions for buttons
def flashFreezeMain():
     DeepFreeze.flashFreeze()

if setting == "1":
     Cool_Down()
elif setting == "2":
     DeepFreeze()
elif setting == "3":
     Timed_Freeze()
else:
     print ("Current time: " + Thermosafe.clock)

print ("Current time: " + Thermosafe.clock)


#main window-----------------------------------------------------
window = tk.Tk()
window.geometry('500x300')
window.title('Thermosafe Freezer')
window.configure(bg="white")

#add image-------------------------------------------------------
img = PhotoImage(file=img_path).subsample(3, 3)
img_lbl  = tk.Label(window, image = img, borderwidth = 0).pack()

#arrange widgets--------------------------------------------------
setting_lbl_var = tk.StringVar()
setting_lbl_var.set("Setting: " + str(setting))
setting_lbl = tk.Label(window, 
                       textvariable = setting_lbl_var, 
                       width=30, fg="aqua", bg="black").pack()
clock_lbl_var = tk.StringVar()
clock_lbl_var.set("Current Time: " + str(current_time))
clock_lbl = tk.Label(window, 
                       textvariable = clock_lbl_var, 
                       width=30, fg="aqua", bg="black").pack()
#buttons---------------------------------------------------------
add_FlashFreeze_btn = tk.Button(window, text='Flash Freeze', fg="white", bg="mediumpurple4", width=12,
                          command = flashFreezeMain).pack()

footnote = tk.Label(window, text = "Code by the Syntax Savvy Duo", width=300, fg="darkorchid4", bg="white").pack(expand = True)
#run---------------------------------------------------------------
window.mainloop()

