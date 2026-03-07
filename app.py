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

#This class' object will be used in the tkinter window
class Thermosafe:
     def __init__(self):
          self.temperature = 0
          self.clock = time.strftime("%I:%M:%S %p")

     def updateClock(self):
          self.clock = time.strftime("%I:%M:%S %p")

#user input "enter time" counts down
class Timed_Freeze:
    def __init__(self, seconds):
        self.seconds = seconds
     #this function sets the timer off                   
    def go(self):
        print(time.strftime("%I:%M:%S %p")+" - Timer started")
        while self.seconds > 0:
            time.sleep(1)
            print(self.seconds)
            self.seconds -= 1
        print(time.strftime("%I:%M:%S %p")+" - Timer ended")

#user input "enter food type" and "enter weight" counts down to cool dish
class Cool_Down:
     food_types = [
          ["Liquid","Meat","Vegetables"],
          [60,120,90],   #under 5
          [120,180,120]] #over 5lbs

     def __init__(self, food, weight):
          self.food = food
          self.weight = weight
          self.time_left = 0
          
          #find the index of the food type, time left depends on if weight is more or less than 5 lbs
          f_indx = self.food_types[0].index(food)
          w_indx = 1 if weight <= 5 else 2

          #set time left by finding in arry
          self.time_left = self.food_types[w_indx][f_indx]

          print(self.food_types[0][f_indx]+" | Weight: "+str(weight)+" | Time: "+str(self.food_types[w_indx][f_indx]))
          self.coolString = "Food: "+self.food_types[0][f_indx]+"\nWeight: "+str(weight)+"\nTime: "+str(self.time_left)+" seconds"


#user input "enter catgory", enter item", "enter days" counts down to flash freeze for a number of days depending on category and item
class Deep_Freeze:
     liquid = {
          1: "Water", 
          2: "Popsicles", 
          3: "Ice Cream"}
     meat = {
          1: "Beef", 
          2: "Chicken", 
          3: "Pork"}
     vegetables = {
          1: "Greens", 
          2: "Carrots", 
          3: "Corn"}
     
     def __init__(self, category, item, num_days):
          self.category = category
          self.item = item
          self.num_days = num_days

          if category == "liquid":
               print("Liquid item chosen: "+self.liquid[item]+"\nDays frozen: "+num_days)
          elif category == "meat":
               print("Meat item chosen: "+self.meat[item]+"\nDays frozen: "+num_days)
          else:
               print("Vegetable item chosen: "+self.vegetables[item]+"\nDays frozen: "+num_days)
     #def begin():


#Create Thermosafe class instances for main window
thermo = Thermosafe()
current_time_str = "Current Time: " + thermo.clock + "\n"

#define functions for buttons---------------------------------
def timedFreeze():
#User will enter how many seconds and then clock will update
     secs = tkinter.simpledialog.askinteger("Q", "How many seconds?")
     if secs is not None:
          timer1 = Timed_Freeze(secs)
          timer1.go()
          messagebox.showinfo("End", "Time's up!")
     thermo1 = Thermosafe()
     thermo1.updateClock()
     new_clock_str = "Current Time: " + thermo1.clock + "\n"
     clock_var.set(new_clock_str)
def deepFreeze():
#user will be prompted for liquid, meat, or veg. will select item 1-3, and days frozen
     optionsTuple = (1,2,3)
     cat = tkinter.simpledialog.askstring("Q", "TYPE a category of food to flash freeze: \nLiquid \nMeat \nVegetables").lower()
     #different options in the prompt depending on what category chosen/typed
     if cat == "liquid":
          itm = tkinter.simpledialog.askinteger("Q", "Choose an item "+str(optionsTuple)+" to flash freeze: \n1. Water \n2. Popsicles \n3. Ice Cream")
     elif cat == "meat":
          itm = tkinter.simpledialog.askinteger("Q", "Choose an item "+str(optionsTuple)+" to flash freeze: \n1. Beef \n2. Chicken \n3. Pork")
     else: #"vegetables"
          itm = tkinter.simpledialog.askinteger("Q", "Choose an item "+str(optionsTuple)+" to flash freeze: \n1. Greens \n2. Carrots \n3. Corn")
     
     days = tkinter.simpledialog.askstring("Q", "Enter the number of days you\nwant to flash freeze the item for: ")
     #create class instance
     deep1 = Deep_Freeze(cat,itm,days)
     if cat == "liquid":
          messagebox.showinfo("End", "Time's up!\n"+ deep1.liquid[itm]+" frozen for "+days+" days!")
     elif cat == "meat":
          messagebox.showinfo("End", "Time's up!\n"+ deep1.meat[itm]+" frozen for "+days+" days!")
     else:
          messagebox.showinfo("End", "Time's up!\n"+ deep1.vegetables[itm]+" frozen for "+days+" days!")
def coolDown():
     userFood = tkinter.simpledialog.askstring("Q", "TYPE a category of food to cool down: \nLiquid \nMeat \nVegetables").capitalize()
     userWeight = tkinter.simpledialog.askinteger("Q", "Enter the approximate weight of the food as a whole number (in pounds): ")
     #create class instance
     cool1 = Cool_Down(userFood,userWeight)
     messagebox.showinfo("End","Time's up! Food reached desired temperature.\n"+cool1.coolString)


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
clock_lbl = tk.Label(window, textvariable = clock_var, width=30, fg="darkorchid4").pack()

#buttons---------------------------------------------------------
timeFreeze_btn = tk.Button(window, text='Timed Freeze', fg="white", bg="mediumpurple4", width=12, command = timedFreeze).pack()
deepFreeze_btn = tk.Button(window, text='Deep Freeze', fg="white", bg="mediumpurple4", width=12, command = deepFreeze).pack()
coolDown_btn = tk.Button(window, text='Cool Down', fg="white", bg="mediumpurple4", width=12, command = coolDown).pack()

#text footnote-----------------------------------------------------
footnote = tk.Label(window, text = "Code by the Syntax Savvy Duo", width=300, fg="darkorchid4", bg="gray94").pack(expand = True)

#run---------------------------------------------------------------
window.mainloop()

