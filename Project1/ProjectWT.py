import tkinter as tk
import tkinter.font as tkFont

class Display:
	def __init__(self):
		#Step 0: Setup GUI
		self.root = tk.Tk()

		#variables
		self.genre = tk.StringVar()
		self.genre.set("Select Option")
		self.genreOptions = ["Action", "Fantasy", "Romance"]
		self.gender = tk.StringVar()
		self.title = "STORY GENERATOR"
		self.maxTrials = 3
		self.minTrials = 1
		self.titleFont = tkFont.Font(family = "Times", size = 22, weight = "bold", underline = 1)
		self.maxFontSize = 100
		self.minFontSize = 10
		self.guiLblFont = tkFont.Font(family = "Helvitica", size = 12, weight = "normal")
		self.guiFrameFont = tkFont.Font(family = "Helvitica", size = 14, weight = "bold")
		self.enableHighContrast = 0
		self.frameBckgrndClr = "grey"
		self.lblBgrndClr = "grey"
		self.entrBgrndClr = "lightgrey"
		self.framePadY = 1
		self.framePadX = 5
		self.entrPadX = 2
		self.entrPadY = 2
		self.outTxtH = 10
		self.outTxtW = 50


#**** Widgets ******************************************************************************************************************************************


		#Title
		self.titleLabel = tk.Label(self.root, text = self.title, font = self.titleFont, background = "yellow", foreground = "blue", pady = 0)
		self.titleLabel.grid(row = 0, column = 0, columnspan = 3, sticky = "NESW")

		#Story Settings Frame
		self.storyFrame = tk.LabelFrame(self.root, text = "Story Settings", background = self.frameBckgrndClr, font = self.guiFrameFont, pady = self.framePadY, padx = self.framePadX)
		self.genreLbl = tk.Label(self.storyFrame, text = "Select Genre", background = self.lblBgrndClr, font = self.guiLblFont)
		self.strtPlaceLbl = tk.Label(self.storyFrame, text = "Starting Place", background = self.lblBgrndClr, font = self.guiLblFont)
		self.genreOMenu = tk.OptionMenu(self.storyFrame, self.genre, self.genreOptions[0], self.genreOptions[1], self.genreOptions[2])
		self.strtPlaceEntr = tk.Entry(self.storyFrame, background = self.entrBgrndClr, font = self.guiLblFont)
		#************ PACKING WIDGETS *****************************************#
		self.storyFrame.grid(row = 1, column = 0)
		self.genreLbl.grid(row = 0, column = 0)
		self.strtPlaceLbl.grid(row = 0, column = 1)
		self.genreOMenu.grid(row = 1, column = 0, padx = self.entrPadX, pady = self.entrPadY)
		self.strtPlaceEntr.grid(row = 1, column = 1, padx = self.entrPadX, pady = self.entrPadY)

		#Hero's Characteristics Frame
		self.heroFrame = tk.LabelFrame(self.root, text = "Hero's Characteristics", background = self.frameBckgrndClr, font = self.guiFrameFont, padx = self.framePadX, pady = self.framePadY)
		self.heroNmLbl = tk.Label(self.heroFrame, text = "Hero's Name", background = self.lblBgrndClr, font = self.guiLblFont)
		self.heroNmEntr = tk.Entry(self.heroFrame, background = self.entrBgrndClr, font = self.guiLblFont)
		self.heroGenderLbl = tk.Label(self.heroFrame, text = "Hero's Gender", background = self.lblBgrndClr, font = self.guiLblFont)
		self.heroStrngthLb  = tk.Label(self.heroFrame, text = "Hero's Strengths", background = self.lblBgrndClr, font = self.guiLblFont)
		self.heroGenderMRBttn = tk.Radiobutton(self.heroFrame, text = "Male", variable = self.gender, value = "male", background = self.lblBgrndClr, font = self.guiLblFont)
		self.heroGenderFRBttn = tk.Radiobutton(self.heroFrame, text = "Female", variable = self.gender, value = "female", background = self.lblBgrndClr, font = self.guiLblFont)
		self.heroStrngthEntr1 = tk.Entry(self.heroFrame, background = self.entrBgrndClr, font = self.guiLblFont)
		self.heroStrngthEntr2 = tk.Entry(self.heroFrame, background = self.entrBgrndClr, font = self.guiLblFont)
		self.heroStrngthEntr3 = tk.Entry(self.heroFrame, background = self.entrBgrndClr, font = self.guiLblFont)
		#************ PACKING WIDGETS *****************************************#
		self.heroFrame.grid(row = 2, column = 0)
		self.heroNmLbl.grid(row = 0, column = 0, columnspan = 2)
		self.heroNmEntr.grid(row = 1, column = 0, columnspan = 2, padx = self.entrPadX, pady = self.entrPadY)
		self.heroGenderLbl.grid(row = 2, column = 0, columnspan = 2)
		self.heroStrngthLb.grid(row = 0, column = 2, columnspan = 2)
		self.heroGenderMRBttn.grid(row = 3, column = 0)
		self.heroGenderFRBttn.grid(row = 3, column = 1)
		self.heroStrngthEntr1.grid(row = 1, column = 2, padx = self.entrPadX, pady = self.entrPadY)
		self.heroStrngthEntr2.grid(row = 2, column = 2, padx = self.entrPadX, pady = self.entrPadY)
		self.heroStrngthEntr3.grid(row = 3, column = 2, padx = self.entrPadX, pady = self.entrPadY)

		#Mentor's Characteristics Frame
		self.mntrFrame = tk.LabelFrame(self.root, text = "Mentor's Characteristics", background = self.frameBckgrndClr, font = self.guiFrameFont, padx = self.framePadX, pady = self.framePadY)
		self.mntrNmLbl = tk.Label(self.mntrFrame, text = "Mentor's Name", background = self.lblBgrndClr, font = self.guiLblFont)
		self.mntrNmEntr = tk.Entry(self.mntrFrame, background = self.entrBgrndClr, font = self.guiLblFont)
		self.mntrGftLbl = tk.Label(self.mntrFrame, text ="Mentor's Gift", background = self.lblBgrndClr, font = self.guiLblFont)
		self.mntrGftEntr = tk.Entry(self.mntrFrame, background = self.entrBgrndClr, font = self.guiLblFont)
		#************ PACKING WIDGETS *****************************************#
		self.mntrFrame.grid(row = 3, column = 0)
		self.mntrNmLbl.grid(row = 0, column = 0)
		self.mntrNmEntr.grid(row = 1, column = 0, padx = self.entrPadX, pady = self.entrPadY)
		self.mntrGftLbl.grid(row = 0, column = 1)
		self.mntrGftEntr.grid(row = 1, column = 1, padx = self.entrPadX, pady = self.entrPadY)

		#Trials Information
		self.trialFrame = tk.LabelFrame(self.root, text = "Trials Information", background = self.frameBckgrndClr, font = self.guiFrameFont, padx = self.framePadX, pady = self.framePadY)	
		self.trialCntLbl = tk.Label(self.trialFrame, text = "Number of Trials", background = self.lblBgrndClr, font = self.guiLblFont)
		self.trialCntSpBx = tk.Spinbox(self.trialFrame, from_ = self.minTrials, to = self.maxTrials, background = self.entrBgrndClr, font = self.guiLblFont)
		self.trialLocLbl = tk.Label(self.trialFrame, text = "Location of Trial", background = self.lblBgrndClr, font = self.guiLblFont)
		self.trialLocEntr = tk.Entry(self.trialFrame, background = self.entrBgrndClr, font = self.guiLblFont)
		self.trialNmLbl = tk.Label(self.trialFrame, text = "Trial", background = self.lblBgrndClr, font = self.guiLblFont)
		self.trialNmEntr = tk.Entry(self.trialFrame, background = self.entrBgrndClr, font = self.guiLblFont)
		#************ PACKING WIDGETS *****************************************#
		self.trialFrame.grid(row = 4, column = 0, padx = self.entrPadX, pady = self.entrPadY)
		self.trialCntLbl.grid(row = 0, column = 1, columnspan = 2)
		self.trialCntSpBx.grid(row = 1, column = 1, columnspan = 2, padx = self.entrPadX, pady = self.entrPadY)
		self.trialLocLbl.grid(row = 2, column = 0, columnspan = 2)
		self.trialLocEntr.grid(row = 3, column = 0, columnspan = 2, padx = self.entrPadX, pady = self.entrPadY)
		self.trialNmLbl.grid(row = 2, column = 2, columnspan = 2)
		self.trialNmEntr.grid(row =3, column = 2, columnspan = 3, padx = self.entrPadX, pady = self.entrPadY)

		#Final Challenge Information
		self.fChllngeFrame = tk.LabelFrame(self.root, text = "Final Challenge Information", background = self.frameBckgrndClr, font = self.guiFrameFont, padx = self.framePadX, pady = self.framePadY)
		self.fChllngeLocLbl = tk.Label(self.fChllngeFrame, text = "Location of Final Challenge", background = self.lblBgrndClr, font = self.guiLblFont)
		self.fChllngeLocEntr = tk.Entry(self.fChllngeFrame, background = self.entrBgrndClr, font = self.guiLblFont)
		self.fChllngeNmLbl = tk.Label(self.fChllngeFrame, text = "Final Challenge", background = self.lblBgrndClr, font = self.guiLblFont)
		self.fChllngeNmEntr = tk.Entry(self.fChllngeFrame, background = self.entrBgrndClr, font = self.guiLblFont)
		#************ PACKING WIDGETS *****************************************#
		self.fChllngeFrame.grid(row = 5, column = 0)
		self.fChllngeLocLbl.grid(row = 0, column = 0)
		self.fChllngeLocEntr.grid(row = 1, column = 0)
		self.fChllngeNmLbl.grid(row = 0, column = 1)
		self.fChllngeNmEntr.grid(row = 1, column = 1)

		#End Stage Information
		self.endFrame = tk.LabelFrame(self.root, text = "End Story", background = self.frameBckgrndClr, font = self.guiFrameFont, padx = self.framePadX, pady = self.framePadY)
		self.trnsprtHmLbl = tk.Label(self.endFrame, text = "Method of Getting Home", background = self.lblBgrndClr, font = self.guiLblFont)
		self.trnsprtHmEntr = tk.Entry(self.endFrame, background = self.entrBgrndClr, font = self.guiLblFont)
		self.rsltLbl = tk.Label(self.endFrame, text = "Result of Story", background = self.lblBgrndClr, font = self.guiLblFont)
		self.rsltEntr = tk.Entry(self.endFrame, background = self.entrBgrndClr, font = self.guiLblFont)
		#************ PACKING WIDGETS *****************************************#
		self.endFrame.grid(row = 6, column = 0)
		self.trnsprtHmLbl.grid(row = 0, column = 0)
		self.trnsprtHmEntr.grid(row = 1, column = 0)
		self.rsltLbl.grid(row = 0, column = 1)
		self.rsltEntr.grid(row = 1, column = 1)

		#Accessibility Frame
		self.accFrame = tk.LabelFrame(self.root, text = "Accessibility", background = self.frameBckgrndClr, font = self.guiFrameFont, padx = self.framePadX, pady = self.framePadY)
		self.hCLbl = tk.Label(self.accFrame, text = "High Contrast", background = self.lblBgrndClr, font = self.guiLblFont)
		self.hCCBox = tk.Checkbutton(self.accFrame, text = "ON/OFF", variable = self.enableHighContrast, background = self.lblBgrndClr, font = self.guiLblFont)
		self.fntSizeLbl = tk.Label(self.accFrame, text = "Font Size", background = self.lblBgrndClr, font = self.guiLblFont)
		self.fntSizeSpBx = tk.Spinbox(self.accFrame, from_ = self.minFontSize, to = self.maxFontSize, background = self.entrBgrndClr, font = self.guiLblFont)
		self.playTxtToSpchBttn = tk.Button(self.accFrame, text = "Play Text to Speech", command = self.bttnClicked, background = self.entrBgrndClr, font = self.guiLblFont)
		#************ PACKING WIDGETS *****************************************#
		self.accFrame.grid(row = 1, column = 2)
		self.hCLbl.grid(row = 0, column = 0)
		self.hCCBox.grid(row = 1, column = 0)
		self.fntSizeLbl.grid(row = 0, column = 1)
		self.fntSizeSpBx.grid(row = 1, column = 1)
		self.playTxtToSpchBttn.grid(row = 2, column = 0, columnspan = 2)

		#Buttons and Output Text Frame
		self.outFrame = tk.LabelFrame(self.root, text = "", background = self.frameBckgrndClr, font = self.guiFrameFont, padx = self.framePadX, pady = self.framePadY )
		self.genStoryBttn = tk.Button(self.outFrame, text = "Generate Story", command = self.bttnClicked)
		self.outTxt = tk.Text(self.outFrame, height = self.outTxtH, width = self.outTxtW, background = self.entrBgrndClr, bd = 5)
		self.saveBttn = tk.Button(self.outFrame, text = "Save", command = self.bttnClicked)
		#************ PACKING WIDGETS *****************************************#
		self.outFrame.grid(row = 2, column = 1, rowspan = 4)
		self.genStoryBttn.grid(row = 0, column = 0)
		self.outTxt.grid(row = 1, column = 0)
		self.saveBttn.grid(row = 2, column = 0)









		#Step 3: Initialize window
		self.root.mainloop()


	def bttnClicked(self):#Check function to ensure buttons work
		print("Clicked")

d = Display()