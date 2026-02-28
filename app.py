"""
Author:         Syntax Savvy Duo (Wendy Gatica, Jeff Vukovits)
Date written:   2/19/26 
Assignment:     Final Project
Short Desc:     class definition of the Thermosafe system
"""

import time
import tkinter as tk
from tkinter import PhotoImage

class Thermosafe:
     temperature = 0
     clock = time.strftime("%H:%M %p")

     def updateClock(self):
          self.clock = time.strftime("%H:%M %p")

print ("Current time: " + Thermosafe.clock)

setting = input("Choose a setting (1-3): \n1. Cool Down \n2. Deep Freeze \n3. Timed Freeze \n")

class Cool_Down:
     food_types = {
          "Liquid":["Water", "Juice", "Ice Cream", "Popsicles"],
          "Meat":["Chicken","Pork","Hamburger","Steak"],
          "Vegetables":["Potatoes","Strawberries","Corn",
                        "Green Beans","Lettuce","Blueberries"],}

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

if setting == "1":
     Cool_Down()
elif setting == "2":
     DeepFreeze()
elif setting == "3":
     Timed_Freeze()
