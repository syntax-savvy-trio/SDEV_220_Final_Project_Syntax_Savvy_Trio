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
from tkinter import messagebox
from tkinter import simpledialog
import os
import tkinter

#picture file path will be the same folder as the code
script_dir = os.path.dirname(os.path.abspath(__file__))
img_path = os.path.join(script_dir, "freezer.png")

class Thermosafe:
     def __init__(self):
          self.temperature = 0
          self.clock = time.strftime("%I:%M:%S %p")

     def updateClock(self):
          self.clock = time.strftime("%I:%M:%S %p")


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
class Timed_Freeze():
    def __init__(self, seconds):
        self.seconds = seconds
     #this function sets the timer off                   
    def go(self):
        print(time.ctime())
        while self.seconds > 0:
            time.sleep(1)
            print(self.seconds)
            self.seconds -= 1
        print(time.ctime())

#Create class instances for main window
thermo = Thermosafe()
current_time_str = "Current Time: " + thermo.clock + "\n"

#define functions for buttons---------------------------------
     #user enters food type
def deepFreezeFlash():
     DeepFreeze.flashFreeze()
     #User will enter how many seconds and then clock will update
def timedFreeze():
     secs = tkinter.simpledialog.askinteger("Q", "How many seconds?")
     if secs is not None:
          timer1 = Timed_Freeze(secs)
          timer1.go()
          messagebox.showinfo("End", "Time's up!.")
     thermo1 = Thermosafe()
     thermo1.updateClock()
     new_clock_str = "Current Time: " + thermo1.clock + "\n"
     clock_var.set(new_clock_str)


#main window-----------------------------------------------------
window = tk.Tk()
window.geometry('280x400')
window.title('Thermosafe Freezer')
window.configure(bg="gray94")

#add image-------------------------------------------------------
img = PhotoImage(file=img_path).subsample(3, 3)
img_lbl  = tk.Label(window, image = img, borderwidth = 0).pack()

#arrange widget text box-----------------------------------------
clock_var = tk.StringVar(value=current_time_str)
clock_lbl = tk.Label(window, 
                       textvariable = clock_var, 
                       width=30, fg="darkorchid4")
clock_lbl.pack()

#buttons---------------------------------------------------------
#Deep Freeze
add_FlashFreeze_btn = tk.Button(window, text='Deep Freeze', fg="white", bg="mediumpurple4", width=12,
                          command = deepFreezeFlash).pack()
#Cool Down 
add_FlashFreeze_btn = tk.Button(window, text='Cool Down', fg="white", bg="mediumpurple4", width=12).pack()
#Timed Freeze
add_FlashFreeze_btn = tk.Button(window, text='Timed Freeze', fg="white", bg="mediumpurple4", width=12, command = timedFreeze).pack()

#text footnote-----------------------------------------------------
footnote = tk.Label(window, text = "Code by the Syntax Savvy Duo", width=300, fg="darkorchid4", bg="gray94").pack(expand = True)

#run---------------------------------------------------------------
window.mainloop()

