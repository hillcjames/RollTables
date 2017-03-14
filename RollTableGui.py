'''


Author: Christopher Hill

Print some text above/below interface if there are no tables detected.
put a shader on the table list's top/bottom when you can scroll that way.
color when rollover buttons
scrolling output label
add menu bar for help and font sizing. Colors too, why not.


args:
	-r (random)  picks a random entry without dice
	-s (size) 	 prints the size of the selected list

'''

from subprocess import call
import os
import json
import tkinter
from tkinter import *


class RandProg(tkinter.Tk):

	programName = ""


	def __init__(self):
		if os.name == "nt":
			self.programName = ".\pickRandom.exe"
		elif  os.name == "posix":
			self.programName = "./pickRandom"
		else: #?
			print("Neither windows nor linux; os name is :", os.name)
			exit(1)

		self.curFileName = ""
		self.dieValue = -1

		self.fillGUI()

		print("****")

		self.root.after(100, self.dummyFunc)
		self.root.mainloop()

	@staticmethod
	def setWidgetColorsToDefault(widget, invert = False):
		bgCol = 0xf7d2a3
		fgCol = 0xffffff - bgCol
		
		if invert:
			fgCol = bgCol
			bgCol = 0xffffff - fgCol

		try:
			widget.configure(foreground = "#" + format(bgCol, '06x'))
		except:
			()
		widget.configure(background = "#" + format(fgCol, '06x'))

	def fillGUI(self):
		self.root = tkinter.Tk()

		self.mainFrame = Frame(self.root, bd = 10)
		self.setWidgetColorsToDefault(self.mainFrame)
		self.mainFrame.pack(fill = BOTH, expand=YES )

		self.upperFrame = Frame(self.mainFrame)
		self.setWidgetColorsToDefault(self.upperFrame)
		self.upperFrame.pack( anchor = N, side = TOP, fill = X, expand=YES )

		self.lowerFrame = Frame(self.mainFrame)
		self.setWidgetColorsToDefault(self.lowerFrame)
		self.lowerFrame.pack( side = BOTTOM, fill = BOTH, expand=YES )

		self.buttonFrame = Frame(self.upperFrame)
		self.setWidgetColorsToDefault(self.buttonFrame)
		self.buttonFrame.pack( side = RIGHT, fill = BOTH, expand=YES )

		self.tableListFrame = Frame(self.upperFrame)
		self.setWidgetColorsToDefault(self.tableListFrame)
		self.tableListFrame.pack( side = LEFT, fill = BOTH, expand=YES )

		self.groupListFrame = Frame(self.upperFrame)
		self.setWidgetColorsToDefault(self.groupListFrame)
		self.groupListFrame.pack( side = LEFT, fill = BOTH, expand=YES )

		self.rollFrame = Frame(self.buttonFrame)
		self.setWidgetColorsToDefault(self.rollFrame)
		self.rollFrame.pack(fill = BOTH, expand=YES)

		self.diceEntry = Entry(self.rollFrame, width = 3)
		self.setWidgetColorsToDefault(self.diceEntry, invert = True)
		self.roll = Button(self.rollFrame, 
			text = "Roll by die", 
			command = self.rollDice)
		self.rand = Button(self.buttonFrame, 
			text = "Get random entry", 
			command = self.rollRand)

		self.setWidgetColorsToDefault(self.rand)
		self.setWidgetColorsToDefault(self.roll)

		self.diceEntry.bind('<Return>', self.rollDice)

		self.roll.pack(side = LEFT, fill = BOTH, expand=YES)
		self.diceEntry.pack(side = RIGHT)
		self.rand.pack(fill = BOTH, expand=YES)

		self.tableScrollbar = Scrollbar(self.tableListFrame)
		self.tableScrollbar.pack(side = RIGHT, fill = Y)

		self.tableList = []
		self.tbList = Listbox(self.tableListFrame, 
			exportselection = False, # stops it from unselecting self on double-click in text box
			yscrollcommand = self.tableScrollbar.set)
		self.setWidgetColorsToDefault(self.tbList)

		index = 1
		for subdir, dirs, files in os.walk(".."):
		    for file in files:
		        #print os.path.join(subdir, file)
		        
		        filepath = subdir + os.sep + file
		        if filepath.endswith(".table"):
		            self.tbList.insert(index, format(index, "02") + "  " + os.path.splitext(file)[0])
		            index += 1
		            self.tableList.append(filepath)

		self.tbList.pack(fill = BOTH, expand = YES)
		self.tbList.select_set(0)
		self.tbList.bind('<Return>', self.rollRand)

		self.tableScrollbar.config(command=self.tbList.yview)



		# self.groupScrollbar = Scrollbar(self.groupListFrame)
		# self.groupScrollbar.pack(side = RIGHT, fill = Y)

		# self.groupList = []
		# self.gpList = Listbox(self.groupListFrame, 
		# 	# exportselection = False, # stops it from unselecting self on double-click in text box
		# 	yscrollcommand = self.groupScrollbar.set)
		# self.setWidgetColorsToDefault(self.gpList)

		# index = 1
		# for subdir, dirs, files in os.walk(".."):
		#     for file in files:
		#         #print os.path.join(subdir, file)
		        
		#         filepath = subdir + os.sep + file
		#         if filepath.endswith(".table"):
		#             self.gpList.insert(index, format(index, "02") + "  " + os.path.splitext(file)[0])
		#             index += 1
		#             self.groupList.append(filepath)

		# self.gpList.pack(fill = BOTH, expand = YES)
		# self.gpList.select_set(0)
		# self.gpList.bind('<Return>', self.rollRand)

		# self.groupScrollbar.config(command=self.gpList.yview)



		# self.outputScrollbar = Scrollbar(self.tableListFrame)
		# self.outputScrollbar.pack(side = RIGHT, fill = Y)

		# outputText = Text(lowerFrame, wrap = WORD, width = 48, height = 5)
		self.outputLabelVar = StringVar()
		self.outputLabelVar.set("Select a table and click \"Rand\" or \"Roll\"")
		self.outputText = Label( self.lowerFrame, 
							textvariable=self.outputLabelVar,
							# state='readonly',
							# relief=RAISED,
							justify = LEFT, 
							wraplength = 256,
							# yscrollcommand = self.tableScrollbar.set, 
							height = 8)
		self.setWidgetColorsToDefault(self.outputText)

		self.outputText.pack(side = RIGHT, fill=BOTH, expand = 1)

		# self.outputScrollbar.config(command=self.outputText.yview)
		# print(lowerFrame.winfo_width())



	def dummyFunc(self):
		self.root.after(100, self.dummyFunc)
		# self makes the program close on keyboard interrupt in terminal
		# http://stackoverflow.com/a/10067034

	# def getDieVal(self, event):
		# self.dieValue = int(event.widget.get())


	def callC_Prog(self, progName, fileName, arg):
		# data = sys.stdin.read()
		output = os.popen(progName + " " + fileName + " " +  arg).read()[:-1]
		print(output)
		# outputText.delete("1.0", END)
		# outputText.insert(INSERT, output)
		self.outputLabelVar.set(output)
		# call([progName, fileName, arg])
		# print(data)
		print("****")

	def getCurrentSelection(self):
		if(self.tbList.curselection() == ()):
			return -1 #no table selected
		return self.tableList[self.tbList.curselection()[0]]

	def rollDice(self, event = 0):
		self.curFileName = self.getCurrentSelection()
		self.dieValue = self.diceEntry.get()
		# print("..", self.dieValue, "..")
		errorMsg = ""
		if (self.curFileName == -1):
			errorMsg = "No table selected."
		if (self.dieValue == ""):
			errorMsg += ("" if len(errorMsg)==0 else "\n") + "No die value given."
		if (self.curFileName == -1) or (self.dieValue == ""):
			print(errorMsg + "\n****")
			self.outputLabelVar.set(errorMsg)
			return
		
		# call([programName, curFileName, str(dieValue)])
		self.callC_Prog(self.programName, self.curFileName, str(self.dieValue))
		# print(x)

	def rollRand(self, event = 0):
		self.curFileName = self.getCurrentSelection()
		if (self.curFileName == -1):
			errorMsg = "No table selected."
			print(errorMsg + "\n****")
			self.outputLabelVar.set(errorMsg)
			return
		self.callC_Prog(self.programName, self.curFileName, "-r")
		# call([programName, curFileName, "-r"])
		# print(x)


w = RandProg()