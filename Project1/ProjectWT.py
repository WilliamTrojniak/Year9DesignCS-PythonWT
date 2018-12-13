import tkinter as tk
import tkinter.font as tkFont
import random



class Display:
	def __init__(self):

#**** Variables ******************************************************************************************************************************************

		self.root = tk.Tk()

		#GUI Layout Config
		self.titleFont = tkFont.Font(family = "Times", size = 22, weight = "bold", underline = 0)
		self.guiLblFont = tkFont.Font(family = "Helvitica", size = 13, weight = "normal")
		self.guiFrameFont = tkFont.Font(family = "Helvitica", size = 13, weight = "bold")
		self.guiOutTxtFont = tkFont.Font(family = "Helvitica", size = 13, weight = "normal")
		self.bttnFont = tkFont.Font(family = "Helvitica", size = 17, weight = "bold")
		
		self.title = "STORY GENERATOR"

		self.lightBlue = "#B1E5EA"
		self.lightestBlue = "#CAF0F4"
		self.darkBlue = "#7DC6CD"
		self.darkestBlue = "#415EAE"
		self.beige = "#FFEBC0"
		self.lightBiege = "#FFF4DD" 
		self.black = "black"

		self.frameBgrndClr = self.darkBlue
		self.lblBgrndClr = self.darkBlue
		self.entrBgrndClr = self.lightestBlue
		self.windowBgrndClr = self.lightBiege
		self.titleBgrndClr = self.beige
		self.titleFntClr = self.darkestBlue

		self.framePadY = 1
		self.framePadX = 5
		self.entrPadX = 1
		self.entrPadY = 1
		self.frameExtPadX = 10
		self.frameExtPadY = 5
		self.bttnPadX = 10
		self.bttnPadY = 5
		self.titlePadY = 10

		self.outTxtH = 25
		self.outTxtW = 70

		self.fontSpBxWidth = 3
		self.trialCntSpBxWidth = 5

		self.root.configure(background=self.windowBgrndClr, height = 800, width = 1400)

		#Widget Variables
		self.enableHighContrast = tk.IntVar()
		self.maxFontSize = 16
		self.minFontSize = 13
		self.genre = tk.StringVar()
		self.genre.set("Select Option")
		self.genreOptions = ["Action", "Fantasy"]
		self.heroGender = tk.StringVar()
		self.maxTrials = 3
		self.minTrials = 1
		self.dynamicTrialEntries = [[]]
		self.currentNumOfTrials = 1
		self.newNumOfTrials = 0
		self.numOfTrials = 1

		#String Storage
		#General
		self.mntrTrialIntroSntnce = ["\"The road ahead will be dangerous, no doubt,\" said ", "\" You will face many dangers before this though,\" said "]
		self.mntrFirstTrialDescriptionSntnce = ["\"You will first have to go to ", "\"The first place to which you must journey is to "]
		self.mntr23TrialDescriptionSntnce = ["\"You must then journey to ", "\"The next place that you must journey to is to "]
		self.heroDestinySntnce = [" where you must ", " where you will ", " where it is destined that you "]
		self.heroReluctanceSntnce = ["\"I accept the tasks that you have laid before me, even if it is with some reluctance.\" responded, ", "\"Though I do not like to think of the troubles ahead, I accept your tasks,\" replied "]
		self.mntrFChllngeIntroSntnce = ["\"Only then, after you have proven worth, will you travel to ", "\"With this, you are to travel to "]
		self.mntrGiftGivingSntnce = ["\"It is as I had hoped. Then I give to you ", "\"Very well, then I give to you "]
		self.mntrGiftAidSntnce = [". May it serve you well on your journey.\" ", ". It will come in use yet.\" "]
		self.heroDepartSntnce = ["So our hero left ", "And so our hero departed from "]

		#Fantasy
		self.fntsyStrtSntnce = ["Once upon a time, in a place known as", "Some time ago, in"]
		self.fntsyHeroIntroSntnce = ["there was an elf by the name of", "there was a dwarf by the name of", "there was a knight by the name of"]
		self.fntsyMentorIntroSntnce = ["On a peculiar night, when the stars aligned just so,", "On a certain morn"]
		#Action
		self.actnStrtSntnce = ["In a galaxy far far away, in a place known as", "Once, in the land known as"]
		self.actnHeroIntroSntnce = ["there was a warrior by the name of", "there was an adventurer by the name of", "there was a spy by the name of"]
		self.actnMentorIntroSntnce = ["One morning, ", "Walking in the streets, one day,"]



		

#**** Widgets ******************************************************************************************************************************************


		#Title
		self.titleLabel = tk.Label(self.root, text = self.title, font = self.titleFont, background = self.titleBgrndClr, foreground = self.titleFntClr, pady = 0)
		self.titleLabel.grid(row = 0, column = 0, columnspan = 3, sticky = "NESW", pady = self.titlePadY)

		#Story Settings Frame
		self.storyFrame = tk.LabelFrame(self.root, text = "Story Settings", background = self.frameBgrndClr, font = self.guiFrameFont, pady = self.framePadY, padx = self.framePadX)
		self.genreLbl = tk.Label(self.storyFrame, text = "Select Genre", background = self.lblBgrndClr, font = self.guiLblFont)
		self.strtPlaceLbl = tk.Label(self.storyFrame, text = "Starting Place", background = self.lblBgrndClr, font = self.guiLblFont)
		self.genreOMenu = tk.OptionMenu(self.storyFrame, self.genre, self.genreOptions[0], self.genreOptions[1])
		self.strtPlaceEntr = tk.Entry(self.storyFrame, background = self.entrBgrndClr, font = self.guiLblFont)
		#************ PACKING WIDGETS *****************************************#
		self.storyFrame.grid(row = 1, column = 0, padx = self.frameExtPadX, pady = self.frameExtPadY, sticky = "NSEW")
		self.genreLbl.grid(row = 0, column = 0)
		self.strtPlaceLbl.grid(row = 0, column = 1)
		self.genreOMenu.grid(row = 1, column = 0, padx = self.entrPadX, pady = self.entrPadY)
		self.strtPlaceEntr.grid(row = 1, column = 1, padx = self.entrPadX, pady = self.entrPadY)

		#Hero's Characteristics Frame
		self.heroFrame = tk.LabelFrame(self.root, text = "Hero's Characteristics", background = self.frameBgrndClr, font = self.guiFrameFont, padx = self.framePadX, pady = self.framePadY)
		self.heroNmLbl = tk.Label(self.heroFrame, text = "Hero's Name", background = self.lblBgrndClr, font = self.guiLblFont)
		self.heroNmEntr = tk.Entry(self.heroFrame, background = self.entrBgrndClr, font = self.guiLblFont)
		self.heroGenderLbl = tk.Label(self.heroFrame, text = "Hero's Gender", background = self.lblBgrndClr, font = self.guiLblFont)
		self.heroStrngthLb  = tk.Label(self.heroFrame, text = "Hero's Strengths", background = self.lblBgrndClr, font = self.guiLblFont)
		self.heroGenderMRBttn = tk.Radiobutton(self.heroFrame, text = "Male", variable = self.heroGender, value = "male", background = self.lblBgrndClr, font = self.guiLblFont)
		self.heroGenderFRBttn = tk.Radiobutton(self.heroFrame, text = "Female", variable = self.heroGender, value = "female", background = self.lblBgrndClr, font = self.guiLblFont)
		self.heroStrngthEntr1 = tk.Entry(self.heroFrame, background = self.entrBgrndClr, font = self.guiLblFont)
		self.heroStrngthEntr2 = tk.Entry(self.heroFrame, background = self.entrBgrndClr, font = self.guiLblFont)
		self.heroStrngthEntr3 = tk.Entry(self.heroFrame, background = self.entrBgrndClr, font = self.guiLblFont)
		#************ PACKING WIDGETS *****************************************#
		self.heroFrame.grid(row = 2, column = 0, padx = self.frameExtPadX, pady = self.frameExtPadY)
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
		self.mntrFrame = tk.LabelFrame(self.root, text = "Mentor's Characteristics", background = self.frameBgrndClr, font = self.guiFrameFont, padx = self.framePadX, pady = self.framePadY)
		self.mntrNmLbl = tk.Label(self.mntrFrame, text = "Mentor's Name", background = self.lblBgrndClr, font = self.guiLblFont)
		self.mntrNmEntr = tk.Entry(self.mntrFrame, background = self.entrBgrndClr, font = self.guiLblFont)
		self.mntrGftLbl = tk.Label(self.mntrFrame, text ="Mentor's Gift", background = self.lblBgrndClr, font = self.guiLblFont)
		self.mntrGftEntr = tk.Entry(self.mntrFrame, background = self.entrBgrndClr, font = self.guiLblFont)
		#************ PACKING WIDGETS *****************************************#
		self.mntrFrame.grid(row = 3, column = 0, padx = self.frameExtPadX, pady = self.frameExtPadY)
		self.mntrNmLbl.grid(row = 0, column = 0)
		self.mntrNmEntr.grid(row = 1, column = 0, padx = self.entrPadX, pady = self.entrPadY)
		self.mntrGftLbl.grid(row = 0, column = 1)
		self.mntrGftEntr.grid(row = 1, column = 1, padx = self.entrPadX, pady = self.entrPadY)

		#Trials Information
		self.trialFrame = tk.LabelFrame(self.root, text = "Trials Information", background = self.frameBgrndClr, font = self.guiFrameFont, padx = self.framePadX, pady = self.framePadY, height = 160)	
		self.trialCntLbl = tk.Label(self.trialFrame, text = "Number of Trials", background = self.lblBgrndClr, font = self.guiLblFont)
		self.trialCntSpBx = tk.Spinbox(self.trialFrame, width = self.trialCntSpBxWidth, justify = tk.RIGHT, state = "readonly", command = self.trialsUpdated, from_ = self.minTrials, to = self.maxTrials, background = self.entrBgrndClr, font = self.guiLblFont)
		self.trialLocLbl = tk.Label(self.trialFrame, text = "Location of Trial", background = self.lblBgrndClr, font = self.guiLblFont)
		self.trialLocEntr = tk.Entry(self.trialFrame, background = self.entrBgrndClr, font = self.guiLblFont)
		self.trialNmLbl = tk.Label(self.trialFrame, text = "Trial", background = self.lblBgrndClr, font = self.guiLblFont)
		self.trialNmEntr = tk.Entry(self.trialFrame, background = self.entrBgrndClr, font = self.guiLblFont)
		self.dynamicTrialEntries[0].append(self.trialLocEntr)
		self.dynamicTrialEntries[0].append(self.trialNmEntr)
		#************ PACKING WIDGETS *****************************************#
		self.trialFrame.grid(row = 4, column = 0, padx = self.frameExtPadX, pady = self.frameExtPadY)
		self.trialCntLbl.grid(row = 0, column = 1, columnspan = 2)
		self.trialCntSpBx.grid(row = 1, column = 1, columnspan = 2, padx = self.entrPadX, pady = self.entrPadY)
		self.trialLocLbl.grid(row = 2, column = 0, columnspan = 2)
		self.trialLocEntr.grid(row = 3, column = 0, columnspan = 2, padx = self.entrPadX, pady = self.entrPadY)
		self.trialNmLbl.grid(row = 2, column = 2, columnspan = 2)
		self.trialNmEntr.grid(row =3, column = 2, columnspan = 3, padx = self.entrPadX, pady = self.entrPadY)

		#Final Challenge Information
		self.fChllngeFrame = tk.LabelFrame(self.root, text = "Final Challenge Information", background = self.frameBgrndClr, font = self.guiFrameFont, padx = self.framePadX, pady = self.framePadY)
		self.fChllngeLocLbl = tk.Label(self.fChllngeFrame, text = "Location of Final Challenge", background = self.lblBgrndClr, font = self.guiLblFont)
		self.fChllngeLocEntr = tk.Entry(self.fChllngeFrame, background = self.entrBgrndClr, font = self.guiLblFont)
		self.fChllngeNmLbl = tk.Label(self.fChllngeFrame, text = "Final Challenge", background = self.lblBgrndClr, font = self.guiLblFont)
		self.fChllngeNmEntr = tk.Entry(self.fChllngeFrame, background = self.entrBgrndClr, font = self.guiLblFont)
		#************ PACKING WIDGETS *****************************************#
		self.fChllngeFrame.grid(row = 5, column = 0, padx = self.frameExtPadX, pady = self.frameExtPadY)
		self.fChllngeLocLbl.grid(row = 0, column = 0)
		self.fChllngeLocEntr.grid(row = 1, column = 0, padx = self.entrPadX, pady = self.entrPadY)
		self.fChllngeNmLbl.grid(row = 0, column = 1)
		self.fChllngeNmEntr.grid(row = 1, column = 1, padx = self.entrPadX, pady = self.entrPadY)

		#End Stage Information
		self.endFrame = tk.LabelFrame(self.root, text = "End Story", background = self.frameBgrndClr, font = self.guiFrameFont, padx = self.framePadX, pady = self.framePadY)
		self.trnsprtHmLbl = tk.Label(self.endFrame, text = "Method of Getting Home", background = self.lblBgrndClr, font = self.guiLblFont)
		self.trnsprtHmEntr = tk.Entry(self.endFrame, background = self.entrBgrndClr, font = self.guiLblFont)
		self.rsltLbl = tk.Label(self.endFrame, text = "Result of Story", background = self.lblBgrndClr, font = self.guiLblFont)
		self.rsltEntr = tk.Entry(self.endFrame, background = self.entrBgrndClr, font = self.guiLblFont)
		#************ PACKING WIDGETS *****************************************#
		self.endFrame.grid(row = 6, column = 0, padx = self.frameExtPadX, pady = self.frameExtPadY)
		self.trnsprtHmLbl.grid(row = 0, column = 0)
		self.trnsprtHmEntr.grid(row = 1, column = 0, padx = self.entrPadX, pady = self.entrPadY)
		self.rsltLbl.grid(row = 0, column = 1)
		self.rsltEntr.grid(row = 1, column = 1, padx = self.entrPadX, pady = self.entrPadY)

		#Accessibility Frame
		self.accFrame = tk.LabelFrame(self.root, text = "Accessibility", background = self.frameBgrndClr, font = self.guiFrameFont, padx = self.framePadX, pady = self.framePadY)
		self.hCLbl = tk.Label(self.accFrame, text = "High Contrast", background = self.lblBgrndClr, font = self.guiLblFont)
		self.hCCBox = tk.Checkbutton(self.accFrame, text = "ON/OFF", variable = self.enableHighContrast, background = self.lblBgrndClr, font = self.guiLblFont, command = self.changeHighContrast)
		self.fntSizeLbl = tk.Label(self.accFrame, text = "Font Size", background = self.lblBgrndClr, font = self.guiLblFont)
		self.fntSizeSpBx = tk.Spinbox(self.accFrame, state = "readonly", command = self.fontSizeUpdated, from_ = self.minFontSize, to = self.maxFontSize, background = self.entrBgrndClr, font = self.guiLblFont, width = self.fontSpBxWidth)
		self.playTxtToSpchBttn = tk.Button(self.accFrame, text = "Play Text to Speech", background = self.entrBgrndClr, font = self.guiLblFont)
		#************ PACKING WIDGETS *****************************************#
		self.accFrame.grid(row = 1, column = 2, padx = self.frameExtPadX, pady = self.frameExtPadY, sticky = "E")
		self.hCLbl.grid(row = 0, column = 0)
		self.hCCBox.grid(row = 1, column = 0)
		self.fntSizeLbl.grid(row = 0, column = 1)
		self.fntSizeSpBx.grid(row = 1, column = 1)
		self.playTxtToSpchBttn.grid(row = 2, column = 0, columnspan = 2)

		#Buttons and Output Text Frame
		self.outFrame = tk.LabelFrame(self.root, text = "", background = self.frameBgrndClr, font = self.guiFrameFont, padx = self.framePadX, pady = self.framePadY)
		self.genStoryBttn = tk.Button(self.outFrame, text = "Generate Story", command = self.genStory, font = self.bttnFont)
		self.outTxt = tk.Text(self.outFrame, height = self.outTxtH, width = self.outTxtW, background = self.entrBgrndClr, bd = 5)
		self.saveBttn = tk.Button(self.outFrame, text = "Save", font = self.bttnFont)
		#************ PACKING WIDGETS *****************************************#
		self.outFrame.grid(row = 2, column = 1, rowspan = 4, columnspan = 2, padx = self.frameExtPadX, pady = self.frameExtPadY)
		self.genStoryBttn.grid(row = 0, column = 0, padx = self.bttnPadX, pady = self.bttnPadY)
		self.outTxt.grid(row = 1, column = 0)
		self.saveBttn.grid(row = 2, column = 0, padx = self.bttnPadX, pady = self.bttnPadY)











		#Step 3: Initialize window
		self.root.mainloop()

#**** Functions ******************************************************************************************************************************************

	def genStory(self):
		#************ GETS ENTRY VALUES *****************************************#
		print("Getting variables...")
		self.genreVar = self.genre.get()
		self.strtPlace = self.strtPlaceEntr.get()
		self.heroNm = self.heroNmEntr.get()
		self.heroGenderVar = self.heroGender.get()
		print("Hero Gender:"+self.heroGenderVar)
		self.heroStrngth1 = self.heroStrngthEntr1.get()
		self.heroStrngth2 = self.heroStrngthEntr2.get()
		self.heroStrngth3 = self.heroStrngthEntr3.get()
		self.heroHeHer = ""
		self.heroHimShe = ""
		self.heroHisHer = ""
		if(self.heroGenderVar == ""):
			self.outPutTxtToBox(1, "No Gender Selected")#Outputs error to textbox if no gender is selected
			return
		elif(self.heroGenderVar == "male"):
			self.heroHimHer = "him"
			self.heroHeShe = "He"
			self.heroHisHer = "his"
		elif(self.heroGenderVar == "female"):
			self.heroHimHer = "her"
			self.heroHeShe = "She"
			self.heroHisHer = "her"



		self.mntrNm = self.mntrNmEntr.get()
		self.mntrGft = self.mntrGftEntr.get()
		self.trialNmLs = []
		self.trialLocLs = []
		for i in range(len(self.dynamicTrialEntries)):
			for t in range(len(self.dynamicTrialEntries[i])):
				if(t == 0):
					self.trialLocLs.append(self.dynamicTrialEntries[i][t].get())
				if(t == 1):
					self.trialNmLs.append(self.dynamicTrialEntries[i][t].get())

		self.fChllngeLoc = self.fChllngeLocEntr.get()
		self.fChllngeNm = self.fChllngeNmEntr.get()
		self.trnsprtHm = self.trnsprtHmEntr.get()
		self.rslt = self.rsltEntr.get()

		#************ CONSTRUCTS OUTPUT STORY STRING *****************************************#
		print("Generating story...")
		self.storyStr = ""

		#Checks what the genre of the story is, Introduction of story changes based on the genre
		if(self.genreVar == self.genreOptions[0]):#Genre is Action
			self.storyStr += self.getRandItemFromLs(self.actnStrtSntnce)
			self.storyStr += (" " + self.strtPlace+", ")
			self.storyStr += self.getRandItemFromLs(self.actnHeroIntroSntnce)
			self.storyStr += (" " + self.heroNm+ ". ")
			self.storyStr += (self.heroNm + " had " + self.heroStrngth2 + ", " + self.heroStrngth3 + " and " + self.heroStrngth1 + ". ")
			self.storyStr += (" "+ self.getRandItemFromLs(self.actnMentorIntroSntnce) + " " + self.mntrNm+" approached " + self.heroHimHer + ". " )
			

		elif(self.genre.get() == self.genreOptions[1]):#Genre is Fantasy
			self.storyStr += self.getRandItemFromLs(self.fntsyStrtSntnce)	
			self.storyStr += (" " + self.strtPlace+", ")
			self.storyStr += self.getRandItemFromLs(self.fntsyHeroIntroSntnce)
			self.storyStr += (" " + self.heroNm+ ". ")
			self.storyStr += (self.heroNm + " had " + self.heroStrngth2 + ", " + self.heroStrngth3 + " and " + self.heroStrngth1 + ".")
			self.storyStr += (" "+ self.getRandItemFromLs(self.fntsyMentorIntroSntnce) + " " + self.mntrNm+" approached " + self.heroHimHer + ". " )
		

		else:
			self.outPutTxtToBox(1, "Invalid Genre Selected") #Outputs error message to text box if no genre is selected and stops the genStory function
			return 

		#Generates the rest of the story that isnt affected by the genre	
		self.storyStr += (self.mntrNm + " told " + self.heroNm + " of how " + self.heroHeShe.lower() + " must " + self.fChllngeNm + " in order to " + self.rslt + ". ")
		self.storyStr += (self.getRandItemFromLs(self.mntrTrialIntroSntnce) + self.mntrNm + ". ")
		self.storyStr += (self.getRandItemFromLs(self.mntrFirstTrialDescriptionSntnce) + self.trialLocLs[0] + self.getRandItemFromLs(self.heroDestinySntnce) + self.trialNmLs[0] + ".\" ")
		if(len(self.trialLocLs) >= 2):
			self.storyStr += (self.getRandItemFromLs(self.mntr23TrialDescriptionSntnce) + self.trialLocLs[1] + self.getRandItemFromLs(self.heroDestinySntnce) + self.trialNmLs[1] + ".\" ")
		if(len(self.trialLocLs) >= 3):
			self.storyStr += (self.getRandItemFromLs(self.mntr23TrialDescriptionSntnce) + self.trialLocLs[2] + self.getRandItemFromLs(self.heroDestinySntnce) + self.trialNmLs[2] + ".\" ")
		self.storyStr += (self.getRandItemFromLs(self.mntrFChllngeIntroSntnce) + self.fChllngeLoc + self.getRandItemFromLs(self.heroDestinySntnce) + self.fChllngeNm + " and " + self.rslt + ".\" ")
		self.storyStr += (self.getRandItemFromLs(self.heroReluctanceSntnce)+ self.heroNm + ". ")
		self.storyStr += (self.getRandItemFromLs(self.mntrGiftGivingSntnce) + self.mntrGft + self.getRandItemFromLs(self.mntrGiftAidSntnce))
		self.storyStr += (self.getRandItemFromLs(self.heroDepartSntnce) + self.strtPlace + " and journeyed to " + self.trialLocLs[0] + ". ")
		self.storyStr += ("Here, " + self.heroHeShe.lower() + " " + self.trialNmLs[0] + " using " + self.heroHisHer + " " + self.heroStrngth1 + ". ")
		if(len(self.trialLocLs) >= 2):
			self.storyStr += (self.heroHeShe + " then traveled to " + self.trialLocLs[1] + " and using " + self.heroHisHer + " " +  self.heroStrngth2 + ", " + self.heroHeShe.lower() + " " + self.trialNmLs[1] + ". ")
		if(len(self.trialLocLs) >= 3):
			self.storyStr += ("Finally, "+ self.heroHeShe.lower() + "  proceeded to " + self.trialLocLs[2] + " and with " + self.heroHisHer + " " +  self.heroStrngth3 + ", " + self.heroHeShe.lower() + " " + self.trialNmLs[2] + ". ")
		self.storyStr += ("With this our hero was prepared to " + self.fChllngeNm + " at " + self.fChllngeLoc + ", and so there " + self.heroHeShe.lower() + " journeyed. ")
		self.storyStr += ("Using all of " + self.heroHisHer + " skills, " + self.heroNm + " " + self.fChllngeNm + " .")
		self.storyStr += ("With this, " + self.heroNm + " " + self.rslt +  " and returned to " + self.strtPlace + " by " + self.trnsprtHm + ", where " + self.heroHeShe.lower() + " was recieved as a true hero.")

		


		self.outPutTxtToBox(0, self.storyStr)

		

	def outPutTxtToBox(self, isError, outStr):#isError = 0 or 1 : false or true
		self.outTxt.delete(1.0, tk.END)#clears output text box
		if(isError == 1):
			self.outTxt.insert(tk.END, "Error while attempting to generate story: \nError Message: "+ outStr)
		else:
			self.outTxt.insert(tk.END, outStr)

	def changeHighContrast(self, *args): #Handles high contrast being turned on and off
		
		if(self.enableHighContrast.get() == 1):
			self.windowBgrndClr = self.black
		else:
			self.windowBgrndClr = self.lightBiege
		
		self.root.config(bg = self.windowBgrndClr)

	def fontSizeUpdated(self, *args): #Handles font size being changed
		
		self.guiLblFont.config(size = self.fntSizeSpBx.get())

	def trialsUpdated(self, *args): #Handles the trial number being changed
		self.numOfTrials = int(self.trialCntSpBx.get())
		self.addTrialEntries(self.numOfTrials)
	
	def addTrialEntries(self, num): #Adjusts Number of Entries to Reflect the Number of Trials Set
		#Destroys Previous Entries in Case the Number of Trials Decreased
		for i in range(0, len(self.dynamicTrialEntries), 1):
			for t in range(0, len(self.dynamicTrialEntries[i]), 1):
				self.dynamicTrialEntries[i][t].destroy()

		self.dynamicTrialEntries = [[],[], []] #Resets the List

		#Creates New Entries in dynamicTrialEntries list
		for i in  range (0, num, 1):
			self.dynamicTrialEntries[i].append(tk.Entry(self.trialFrame, background = self.entrBgrndClr, font = self.guiLblFont))
			self.dynamicTrialEntries[i].append(tk.Entry(self.trialFrame, background = self.entrBgrndClr, font = self.guiLblFont))
			self.dynamicTrialEntries[i][0].grid(row = 4+i, column = 0, columnspan = 2, padx = self.entrPadX, pady = self.entrPadY)
			self.dynamicTrialEntries[i][1].grid(row = 4+i, column = 2, columnspan = 2, padx = self.entrPadX, pady = self.entrPadY)

	def getRandItemFromLs(self, exList): #Returns a random item from a list
		randIndex = random.randint(0, len(exList)-1)		
		return exList[randIndex]


d = Display()


























