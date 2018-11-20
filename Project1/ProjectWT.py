import tkinter as tk

class Display:
	def __init__(self):
		#Step 0: Setup GUI
		self.root = tk.Tk()

		#variables
		self.genre = tk.StringVar(self.root)
		self.genre.set("Select Option")
		self.genreOptions = ["Action", "Fantasy", "Romance"]
		self.gender = tk.StringVar()
		self.title = "STORY GENERATOR"
		self.maxTrials = 3
		self.minTrials = 1
		self.maxFontSize = 100
		self.minFontSize = 10
		self.fontSize = 12
		self.enableHighContrast = 0

#**** Widgets ******************************************************************************************************************************************


		#Title
		self.titleLabel = tk.Label(self.root, text = self.title, font = ("Helvetica", 16), background = "yellow", foreground = "blue")
		self.titleLabel.grid(row = 0, column = 0, columnspan = 3, sticky = "NESW")

		#Story Settings Frame
		self.storyFrame = tk.LabelFrame(self.root, text = "Story Settings")
		self.genreLbl = tk.Label(self.storyFrame, text = "Select Genre")
		self.strtPlaceLbl = tk.Label(self.storyFrame, text = "Starting Place")
		self.genreOMenu = tk.OptionMenu(self.storyFrame, self.genre, self.genreOptions[0], self.genreOptions[1], self.genreOptions[2])
		self.strtPlaceEntr = tk.Entry(self.storyFrame)
		#************ PACKING WIDGETS *****************************************#
		self.storyFrame.grid(row = 1, column = 1)
		self.genreLbl.grid(row = 0, column = 0)
		self.strtPlaceLbl.grid(row = 0, column = 1)
		self.genreOMenu.grid(row = 1, column = 0)
		self.strtPlaceEntr.grid(row = 1, column = 1)

		#Hero's Characteristics Frame
		self.heroFrame = tk.LabelFrame(self.root, text = "Hero's Characteristics")
		self.heroNmLbl = tk.Label(self.heroFrame, text = "Hero's Name")
		self.heroNmEntr = tk.Entry(self.heroFrame)
		self.heroGenderLbl = tk.Label(self.heroFrame, text = "Hero's Gender")
		self.heroStrngthLb  = tk.Label(self.heroFrame, text = "Hero's Strengths")
		self.heroGenderMRBttn = tk.Radiobutton(self.heroFrame, text = "Male", variable = self.gender, value = "male")
		self.heroGenderFRBttn = tk.Radiobutton(self.heroFrame, text = "Female", variable = self.gender, value = "female")
		self.heroStrngthEntr1 = tk.Entry(self.heroFrame)
		self.heroStrngthEntr2 = tk.Entry(self.heroFrame)
		self.heroStrngthEntr3 = tk.Entry(self.heroFrame)
		#************ PACKING WIDGETS *****************************************#
		self.heroFrame.grid(row = 2, column = 1)
		self.heroNmLbl.grid(row = 0, column = 0, columnspan = 2)
		self.heroNmEntr.grid(row = 1, column = 0, columnspan = 2)
		self.heroGenderLbl.grid(row = 2, column = 0, columnspan = 2)
		self.heroStrngthLb.grid(row = 0, column = 2, columnspan = 2)
		self.heroGenderMRBttn.grid(row = 3, column = 0)
		self.heroGenderFRBttn.grid(row = 3, column = 1)
		self.heroStrngthEntr1.grid(row = 1, column = 2)
		self.heroStrngthEntr2.grid(row = 2, column = 2)
		self.heroStrngthEntr3.grid(row = 3, column = 2)

		#Mentor's Characteristics Frame
		self.mntrFrame = tk.LabelFrame(self.root, text = "Mentor's Characteristics")
		self.mntrNmLbl = tk.Label(self.mntrFrame, text = "Mentor's Name")
		self.mntrNmEntr = tk.Entry(self.mntrFrame)
		self.mntrGftLbl = tk.Label(self.mntrFrame, text ="Mentor's Gift")
		self.mntrGftEntr = tk.Entry(self.mntrFrame)
		#************ PACKING WIDGETS *****************************************#
		self.mntrFrame.grid(row = 3, column = 1)
		self.mntrNmLbl.grid(row = 0, column = 0)
		self.mntrNmEntr.grid(row = 1, column = 0)
		self.mntrGftLbl.grid(row = 0, column = 1)
		self.mntrGftEntr.grid(row = 1, column = 1)

		#Trials Information
		self.trialFrame = tk.LabelFrame(self.root, text = "Trials Information")	
		self.trialCntLbl = tk.Label(self.trialFrame, text = "Number of Trials")
		self.trialCntSpBx = tk.Spinbox(self.trialFrame, from_ = self.minTrials, to = self.maxTrials)
		self.trialLocLbl = tk.Label(self.trialFrame, text = "Location of Trials")
		self.trialLocEntr = tk.Entry(self.trialFrame)
		self.trialNmLbl = tk.Label(self.trialFrame, text = "Trial")
		self.trialNmEntr = tk.Entry(self.trialFrame)
		#************ PACKING WIDGETS *****************************************#
		self.trialFrame.grid(row = 4, column = 1)
		self.trialCntLbl.grid(row = 0, column = 1, columnspan = 2)
		self.trialCntSpBx.grid(row = 1, column = 1, columnspan = 2)
		self.trialLocLbl.grid(row = 2, column = 0, columnspan = 2)
		self.trialLocEntr.grid(row = 3, column = 0, columnspan = 2)
		self.trialNmLbl.grid(row = 2, column = 2, columnspan = 2)
		self.trialNmEntr.grid(row =3, column = 2, columnspan = 3)

		#Final Challenge Information
		self.fChllngeFrame = tk.LabelFrame(self.root, text = "Final Challenge Information")
		self.fChllngeLocLbl = tk.Label(self.fChllngeFrame, text = "Location of Final Challenge")
		self.fChllngeLocEntr = tk.Entry(self.fChllngeFrame)
		self.fChllngeNmLbl = tk.Label(self.fChllngeFrame, text = "Final Challenge")
		self.fChllngeNmEntr = tk.Entry(self.fChllngeFrame)
		#************ PACKING WIDGETS *****************************************#
		self.fChllngeFrame.grid(row = 5, column = 1)
		self.fChllngeLocLbl.grid(row = 0, column = 0)
		self.fChllngeLocEntr.grid(row = 1, column = 0)
		self.fChllngeNmLbl.grid(row = 0, column = 1)
		self.fChllngeNmEntr.grid(row = 1, column = 1)

		#End Stage Information
		self.endFrame = tk.LabelFrame(self.root, text = "End Story")
		self.trnsprtHmLbl = tk.Label(self.endFrame, text = "Method of Getting Home")
		self.trnsprtHmEntr = tk.Entry(self.endFrame)
		self.rsltLbl = tk.Label(self.endFrame, text = "Result of Story")
		self.rsltEntr = tk.Entry(self.endFrame)
		#************ PACKING WIDGETS *****************************************#
		self.endFrame.grid(row = 6, column = 1)
		self.trnsprtHmLbl.grid(row = 0, column = 0)
		self.trnsprtHmEntr.grid(row = 1, column = 0)
		self.rsltLbl.grid(row = 0, column = 1)
		self.rsltEntr.grid(row = 1, column = 1)

		#Accessibility Frame
		self.accFrame = tk.LabelFrame(self.root, text = "Accessibility")
		self.hCLbl = tk.Label(self.accFrame, text = "High Contrast")
		self.hCCBox = tk.Checkbutton(self.accFrame, text = "ON/OFF", variable = self.enableHighContrast)
		self.fntSizeLbl = tk.Label(self.accFrame, text = "Font Size")
		self.fntSizeSpBx = tk.Spinbox(self.accFrame, from_ = self.minFontSize, to = self.maxFontSize)
		self.playTxtToSpchBttn = tk.Button(self.accFrame, text = "Play Text to Speech", command = self.bttnClicked)
		#************ PACKING WIDGETS *****************************************#
		self.accFrame.grid(row = 1, column = 0)
		self.hCLbl.grid(row = 0, column = 0)
		self.hCCBox.grid(row = 1, column = 0)
		self.fntSizeLbl.grid(row = 0, column = 1)
		self.fntSizeSpBx.grid(row = 1, column = 1)
		self.playTxtToSpchBttn.grid(row = 2, column = 0, columnspan = 2)

		#Buttons and Output Text
		self.genStoryBttn = tk.Button(self.root, text = "Generate Story", command = self.bttnClicked)
		self.outTxt = tk.Text(self.root, height = 8, width = 50)
		self.saveBttn = tk.Button(self.root, text = "Save", command = self.bttnClicked)
		#************ PACKING WIDGETS *****************************************#
		self.genStoryBttn.grid(row = 7, column = 1)
		self.outTxt.grid(row = 8, column = 1)
		self.saveBttn.grid(row = 9, column = 1)









		#Step 3: Initialize window
		self.root.mainloop()


	def bttnClicked(self):#Check function to ensure buttons work
		print("Clicked")

d = Display()