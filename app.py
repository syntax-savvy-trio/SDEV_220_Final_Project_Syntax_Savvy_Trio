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

setting = input("Choose a setting (1-3): \n1. Cool Down \n2. Deep Freeze \n3. Timed Freeze \n")

class Cool_Down:
     food_types = {
          "Liquid":["Water", "Juice", "Ice Cream", "Popsicles"],
          "Meat":["Chicken","Pork","Hamburger","Steak"],
          "Vegetables":["Potatoes","Strawberries","Corn",
                        "Green Beans","Lettuce","Blueberries"],}

#ex: Strawberries = 2 minutes
class DeepFreeze:
     food_types = {
          "Liquid":["Water", "Juice", "Ice Cream", "Popsicles"],
          "Meat":["Chicken","Pork","Hamburger","Steak"],
          "Vegetables":["Potatoes","Strawberries","Corn",
                        "Green Beans","Lettuce","Blueberries"],}

     def flashFreeze(self, item, time, temp):
          self.item = item
          self.time = time
          self.temp = temp
     
#user input "enter time" counts down
class Timed_Freeze:
     time = 0
     time_left = 0

     def activate(self, time):
          self.time = time
          self.time_left = time
          
     def update(self):
            if self.time_left > 0:
                 self.time_left -= 1
            else:
                 print("Time's up! Food reached desired temperature.")

#define functions for buttons
def flashFreezeMain():
     DeepFreeze.flashFreeze()


if setting == "1":
     Cool_Down()
elif setting == "2":
     DeepFreeze()
elif setting == "3":
     Timed_Freeze()


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
