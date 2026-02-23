"""
Author:         Syntax Savvy Duo (Wendy Gatica, Jeff Vukovits)
Date written:   2/19/26 
Assignment:     Final Project
Short Desc:     class definition of the Thermosafe system
"""

import time
import tkinter as tk
from tkinter import PhotoImage

#new code*************************
class Thermosafe:
     temperature = 0
     clock = time.strftime("%H:%M")

     def updateClock(self):
          clock = time.strftime("%H:%M")

print ("Current time: " + Thermosafe.clock)

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


