'''
Idea Board, User will be inserting file paths into a text document, which will help with updating
Developed by: Tomasz Brauntsch
'''
#UI building
import tkinter as tk
from tkinter import *
from tkinter import filedialog
#Moving the file
import os
#determine what os user is using
import platform

#
#Initialization window
#

def initialize_window():
	top = Toplevel()
	labelTitle = Label(top, text="Initialization").pack()
	labelSubText = StringVar()
	labelSub = Label(top, textvariable=labelSubText).pack()
	labelSubText.set("Enter the path(s) of where the file should go in the textbox below\n For more then one path, use ; inbetween paths e,g xyz;zyx\nREMEMBER: when typing in the path use \\ instead of / to not have difficulties\nThis path is case-sensitive so make sure the casing is correct!")
	#Entry and pack has to be seperate so it the function can obtain a value
	userInputEntry = Text(top, height=10,width=50)
	userInputEntry.pack()
	def recieve_input():
		userInput = userInputEntry.get("1.0", "end-1c")
		print (userInput)
		userInputEntry.destroy()
		labelSubText.set("Please wait, while we are processing your request...")
		f = open("path.txt", "w+")
		f.write(userInput)
		f.close()
		top.destroy()

	submitButton = Button(top, text="Submit", command=recieve_input).pack()

#
#Start Window
#

def start_window():
	top = Toplevel()
	labelText = StringVar()
	labelTitle = Label(top, textvariable=labelText).pack()
	labelText.set("Click the button below to transfer")

	def processing():
		filePath = filedialog.askopenfilename()
		userFile = open(filePath, "r", encoding="utf-8")
		userFilePath = "\"" + userFile.name + "\""
		print(userFilePath)
		labelText.set("Sending over the file...")
		locationFile = open("path.txt", "r")
		filePath = locationFile.read()
		path = filePath.split(";")
		for location in path:
			location = "\"" + location + "\""
			print(location)
			if (platform.system() == "Windows"):
				location = location.replace("/", "\\")
				userFilePath = userFilePath.replace("/", "\\")
				os.system('copy ' + userFilePath + ' ' + location)
			else:
				os.system('cp ' + userFilePath + ' ' + location)
		top.destroy()

	browseButton = Button(top, text="Browse...", command=processing).pack()
#
#Main Window
#

app = tk.Tk()
labelTitleText = Label(app, text="File Transportation Application").pack()
labelSubText = Label(app, text="If this is your first time click the Initialize button\n If not click the start button").pack()
firstButton = Button(app, text="Initialize", command=initialize_window).pack()
startButton = Button(app, text="Start!", command=start_window).pack()
app.mainloop()
