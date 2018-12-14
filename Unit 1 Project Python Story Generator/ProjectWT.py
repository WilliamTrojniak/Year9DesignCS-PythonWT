import tkinter as tk
import tkinter.font as tkFont
import random
import threading
from threading import Thread
import os



class myThread (threading.Thread):
	def __init__(self, stringToRead):
		threading.Thread.__init__(self)
		self.stringToRead = stringToRead.replace("'", "")
		self.stringToRead = self.stringToRead.replace("\"", "")
		self.stringToRead = self.stringToRead.replace("-", "")
		self.stringToRead = self.stringToRead.replace("\n", " ")
	def run(self):
		string = "say " + self.stringToRead
		os.system(string)
		print("Exiting Thread")


class Display:
	def __init__(self):

#**** Variables ******************************************************************************************************************************************
		self.root = tk.Tk()

		

		#Colour Storage
		self.LIGHT_BLUE = "#CAF0F4"
		self.BLUE = "#7DC6CD"
		self.DARK_BLUE = "#415EAE"
		self.BEIGE = "#FFEBC0"
		self.LIGHT_BEIGE = "#FFF4DD" 
		self.BLACK = "#08090A"
		self.LIGHT_GRAY = "#44444A"
		self.GRAY = "#383838"
		self.DARK_GRAY = "#212121"
		self.PURPLE = "#86229E"
		self.DARK_PURPLE = "#3C0F47"
		self.ORANGE = "#D66D10"
		self.DARK_ORANGE = "#613107"

		#GUI Visual Settings and Layout Config
		self.titleFont = tkFont.Font(family = "Times", size = 22, weight = "bold", underline = 0)
		self.guiLblFont = tkFont.Font(family = "Helvitica", size = 13, weight = "normal")
		self.guiFrameFont = tkFont.Font(family = "Helvitica", size = 13, weight = "bold")
		self.guiOutTxtFont = tkFont.Font(family = "Helvitica", size = 13, weight = "normal")
		self.bttnFont = tkFont.Font(family = "Helvitica", size = 17, weight = "bold")
		
		#Program Information
		self.title = "STORY GENERATOR"
		self.version = "1.0"
		self.DEVELOPER = "William Trojniak"
		self.YEAR = "2018"
		self.windowTitle = self.title + " V."+ self.version + " ~" + self.DEVELOPER + " " + self.YEAR

		#Initial Colour Scheme
		self.frameBgrndClr = self.BLUE
		self.lblBgrndClr = self.BLUE
		self.entrBgrndClr = self.LIGHT_BLUE
		self.windowBgrndClr = self.LIGHT_BEIGE
		self.titleBgrndClr = self.BEIGE
		self.titleFntClr = self.DARK_BLUE
		self.lblFntClr = self.BLACK
		self.entrFntClr = self.BLACK
		self.entrTempFntClr = self.LIGHT_GRAY

		#Widget Padding
		self.framePadY = 1
		self.framePadX = 5
		self.entrPadX = 1
		self.entrPadY = 1
		self.frameExtPadX = 10
		self.frameExtPadY = 5
		self.bttnPadX = 10
		self.bttnPadY = 5
		self.titlePadY = 10
		self.oMenuPadX = 1
		self.oMenuPadY = 1

		#Output textbox dimensions
		self.outTxtH = 25
		self.outTxtW = 70

		#Spin box sizes
		self.fontSpBxWidth = 3
		self.trialCntSpBxWidth = 5

		#OMenuSize
		self.oMenuWidth = 20


		#Widget Storage Variables
		self.frameLs = []
		self.entryLs = []
		self.labelLs = []
		self.spBxLs = []
		self.oMenuLs = []
		self.cBttnLs = []
		self.rBttnLs = []
		self.bttnLs = []
		self.txtLs = []
		self.dynamicTrialEntries = [[]]

		#Widget Value Variables
		self.enableHighContrast = tk.IntVar()
		self.maxFontSize = 16
		self.minFontSize = 13
		self.genre = tk.StringVar()
		self.genre.set("Select Option")
		self.genreOptions = ["Action", "Fantasy"]
		self.heroGender = tk.StringVar()
		self.maxTrials = 3
		self.minTrials = 1

		#Saved stories
		self.SAVEDSTORIESDOC = "savedStories.txt"
		f = open(self.SAVEDSTORIESDOC, "a+")
		f.close()
		f = open(self.SAVEDSTORIESDOC, "r")
		self.savedStories = f.read().splitlines()
		f.close()
		#print(self.savedStories)
		self.savedStoryCntr = len(self.savedStories)
		
		

		#Text to speech
		self.txtToSpeechRead = 1 #1 = Labels, -1 = Generated Story
		self.txtToSpeechSntnce = "Welcome to Story Generator. This program was developed by William Trojniak. The text to speech button switches between reading the labels and the generated story. Story Generator. Story Settings. Select Genre. Starting Place. Hero's Characteristics. Hero's Name. Hero's gender. Hero's strengths. Mentor's Characteristics. Mentor's Name. Mentor's gift. Trials Information. Number of trials. Trial Location. Trial. Final Challenge Information. Final Challenge Location. Final Challenge. End Story. Method of getting home. Result of story. Generate Story. Save"

		#***String Storage For Story Generation*******************************************************************************************************************
		#General
		self.mntrTrialIntroSntnce = ["\"The road ahead will be dangerous, no doubt,\" said ", "\" You will face many dangers before this though,\" said "]
		self.mntrFirstTrialDescriptionSntnce = ["\"You will first have to go to ", "\"The first place to which you must journey is to "]
		self.mntr23TrialDescriptionSntnce = ["\"You must then journey to ", "\"The next place that you must journey to is to "]
		self.heroDestinySntnce = [" where you must ", " where you will ", " where it is destined that you "]
		self.heroReluctanceSntnce = ["\"I accept the tasks that you have laid before me, even if it is with some reluctance,\" responded, ", "\"Though I do not like to think of the troubles ahead, I accept your tasks,\" replied "]
		self.mntrFChllngeIntroSntnce = ["\"Only then, after you have proven worth, will you travel to ", "\"With this, you are to travel to "]
		self.mntrGiftGivingSntnce = ["\"It is as I had hoped. Then I give to you ", "\"Very well, then I give to you "]
		self.mntrGiftAidSntnce = [". May it serve you well on your journey.\" ", ". It will come in use yet.\" "]
		self.heroDepartSntnce = ["So our hero left ", "And so our hero departed from "]

		#Fantasy
		self.fntsyStrtSntnce = ["Once upon a time, in a place known as", "Some time ago, in"]
		self.fntsyHeroIntroSntnce = ["there was an elf by the name of", "there was a dwarf by the name of", "there was a knight by the name of"]
		self.fntsyMentorIntroSntnce = ["On a peculiar night, when the stars aligned just so,", "On a certain morn"]
		#Action
		self.actnStrtSntnce = [" There once was a place known as", "Once, in the land known as"]
		self.actnHeroIntroSntnce = ["there was a warrior by the name of", "there was an adventurer by the name of", "there was a spy by the name of"]
		self.actnMentorIntroSntnce = ["One morning, ", "Walking in the streets one day,"]

		
#**** Window 1 time Configuration ******************************************************************************************************************************************
		
		self.root.title(self.windowTitle)

#**** Widgets ******************************************************************************************************************************************


		#Title
		self.titleLabel = tk.Label(self.root)
		self.titleLabel.grid(row = 0, column = 0, columnspan = 3, sticky = "NESW", pady = self.titlePadY)

		#Story Settings Frame
		self.storyFrame = tk.LabelFrame(self.root, text = "Story Settings")
		self.genreLbl = tk.Label(self.storyFrame, text = "Select Genre")
		self.strtPlaceLbl = tk.Label(self.storyFrame, text = "Starting Place")
		self.genreOMenu = tk.OptionMenu(self.storyFrame, self.genre, self.genreOptions[0], self.genreOptions[1])
		self.strtPlaceEntr = tk.Entry(self.storyFrame)
		#************ PACKING WIDGETS *****************************************#
		self.storyFrame.grid(row = 1, column = 0, padx = self.frameExtPadX, pady = self.frameExtPadY)
		self.genreLbl.grid(row = 0, column = 0)
		self.strtPlaceLbl.grid(row = 0, column = 1)
		self.genreOMenu.grid(row = 1, column = 0, padx = self.oMenuPadX, pady = self.oMenuPadY)
		self.strtPlaceEntr.grid(row = 1, column = 1, padx = self.entrPadX, pady = self.entrPadY)

		#Hero's Characteristics Frame
		self.heroFrame = tk.LabelFrame(self.root, text = "Hero's Characteristics")
		self.heroNmLbl = tk.Label(self.heroFrame, text = "Hero's Name")
		self.heroNmEntr = tk.Entry(self.heroFrame)
		self.heroGenderLbl = tk.Label(self.heroFrame, text = "Hero's Gender")
		self.heroStrngthLbl  = tk.Label(self.heroFrame, text = "Hero's Strengths")
		self.heroGenderMRBttn = tk.Radiobutton(self.heroFrame, text = "Male", variable = self.heroGender, value = "male")
		self.heroGenderFRBttn = tk.Radiobutton(self.heroFrame, text = "Female", variable = self.heroGender, value = "female")
		self.heroStrngthEntr1 = tk.Entry(self.heroFrame)
		self.heroStrngthEntr2 = tk.Entry(self.heroFrame)
		self.heroStrngthEntr3 = tk.Entry(self.heroFrame)
		#************ PACKING WIDGETS *****************************************#
		self.heroFrame.grid(row = 2, column = 0, padx = self.frameExtPadX, pady = self.frameExtPadY)
		self.heroNmLbl.grid(row = 0, column = 0, columnspan = 2)
		self.heroNmEntr.grid(row = 1, column = 0, columnspan = 2, padx = self.entrPadX, pady = self.entrPadY)
		self.heroGenderLbl.grid(row = 2, column = 0, columnspan = 2)
		self.heroStrngthLbl.grid(row = 0, column = 2, columnspan = 2)
		self.heroGenderMRBttn.grid(row = 3, column = 0)
		self.heroGenderFRBttn.grid(row = 3, column = 1)
		self.heroStrngthEntr1.grid(row = 1, column = 2, padx = self.entrPadX, pady = self.entrPadY)
		self.heroStrngthEntr2.grid(row = 2, column = 2, padx = self.entrPadX, pady = self.entrPadY)
		self.heroStrngthEntr3.grid(row = 3, column = 2, padx = self.entrPadX, pady = self.entrPadY)

		#Mentor's Characteristics Frame
		self.mntrFrame = tk.LabelFrame(self.root, text = "Mentor's Characteristics")
		self.mntrNmLbl = tk.Label(self.mntrFrame, text = "Mentor's Name")
		self.mntrNmEntr = tk.Entry(self.mntrFrame)
		self.mntrGftLbl = tk.Label(self.mntrFrame, text ="Mentor's Gift")
		self.mntrGftEntr = tk.Entry(self.mntrFrame)
		#************ PACKING WIDGETS *****************************************#
		self.mntrFrame.grid(row = 3, column = 0, padx = self.frameExtPadX, pady = self.frameExtPadY)
		self.mntrNmLbl.grid(row = 0, column = 0)
		self.mntrNmEntr.grid(row = 1, column = 0, padx = self.entrPadX, pady = self.entrPadY)
		self.mntrGftLbl.grid(row = 0, column = 1)
		self.mntrGftEntr.grid(row = 1, column = 1, padx = self.entrPadX, pady = self.entrPadY)

		#Trials Information
		self.trialFrame = tk.LabelFrame(self.root, text = "Trials Information")	
		self.trialCntLbl = tk.Label(self.trialFrame, text = "Number of Trials")
		self.trialCntSpBx = tk.Spinbox(self.trialFrame, width = self.trialCntSpBxWidth, command = self.trialsUpdated, from_ = self.minTrials, to = self.maxTrials)
		self.trialLocLbl = tk.Label(self.trialFrame, text = "Location of Trial")
		self.trialLocEntr = tk.Entry(self.trialFrame)
		self.trialNmLbl = tk.Label(self.trialFrame, text = "Trial")
		self.trialNmEntr = tk.Entry(self.trialFrame)
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
		self.fChllngeFrame = tk.LabelFrame(self.root, text = "Final Challenge Information")
		self.fChllngeLocLbl = tk.Label(self.fChllngeFrame, text = "Location of Final Challenge")
		self.fChllngeLocEntr = tk.Entry(self.fChllngeFrame)
		self.fChllngeNmLbl = tk.Label(self.fChllngeFrame, text = "Final Challenge")
		self.fChllngeNmEntr = tk.Entry(self.fChllngeFrame)
		#************ PACKING WIDGETS *****************************************#
		self.fChllngeFrame.grid(row = 5, column = 0, padx = self.frameExtPadX, pady = self.frameExtPadY)
		self.fChllngeLocLbl.grid(row = 0, column = 0)
		self.fChllngeLocEntr.grid(row = 1, column = 0, padx = self.entrPadX, pady = self.entrPadY)
		self.fChllngeNmLbl.grid(row = 0, column = 1)
		self.fChllngeNmEntr.grid(row = 1, column = 1, padx = self.entrPadX, pady = self.entrPadY)

		#End Stage Information
		self.endFrame = tk.LabelFrame(self.root, text = "End Story")
		self.trnsprtHmLbl = tk.Label(self.endFrame, text = "Method of Getting Home")
		self.trnsprtHmEntr = tk.Entry(self.endFrame)
		self.rsltLbl = tk.Label(self.endFrame, text = "Result of Story")
		self.rsltEntr = tk.Entry(self.endFrame)
		#************ PACKING WIDGETS *****************************************#
		self.endFrame.grid(row = 6, column = 0, padx = self.frameExtPadX, pady = self.frameExtPadY)
		self.trnsprtHmLbl.grid(row = 0, column = 0)
		self.trnsprtHmEntr.grid(row = 1, column = 0, padx = self.entrPadX, pady = self.entrPadY)
		self.rsltLbl.grid(row = 0, column = 1)
		self.rsltEntr.grid(row = 1, column = 1, padx = self.entrPadX, pady = self.entrPadY)

		#Accessibility Frame
		self.accFrame = tk.LabelFrame(self.root, text = "Accessibility")
		self.hCLbl = tk.Label(self.accFrame, text = "High Contrast")
		self.hCCBox = tk.Checkbutton(self.accFrame, text = "ON/OFF", variable = self.enableHighContrast, command = self.changeHighContrast)
		self.fntSizeLbl = tk.Label(self.accFrame, text = "Font Size")
		self.fntSizeSpBx = tk.Spinbox(self.accFrame, command = self.fontSizeUpdated, from_ = self.minFontSize, to = self.maxFontSize, width = self.fontSpBxWidth)
		self.playTxtToSpchBttn = tk.Button(self.accFrame, text = "Play Text to Speech", font = self.guiLblFont, command = self.handleTextToSpeech)
		#************ PACKING WIDGETS *****************************************#
		self.accFrame.grid(row = 1, column = 2, padx = self.frameExtPadX, pady = self.frameExtPadY, sticky = "E")
		self.hCLbl.grid(row = 0, column = 0)
		self.hCCBox.grid(row = 1, column = 0)
		self.fntSizeLbl.grid(row = 0, column = 1)
		self.fntSizeSpBx.grid(row = 1, column = 1)
		self.playTxtToSpchBttn.grid(row = 2, column = 0, columnspan = 2)

		#Buttons and Output Text Frame
		self.outFrame = tk.LabelFrame(self.root)
		self.genStoryBttn = tk.Button(self.outFrame, text = "Generate Story", command = self.genStory)
		self.txtScroll = tk.Scrollbar(self.outFrame)
		self.outTxt = tk.Text(self.outFrame, height = self.outTxtH, width = self.outTxtW, yscrollcommand=self.txtScroll.set)
		self.saveBttn = tk.Button(self.outFrame, text = "Save", command = self.saveStory)
		self.txtScroll.config(command = self.outTxt.yview)
		self.savedStoryScroll = tk.Scrollbar(self.outFrame)
		self.savedStoryLsBox = tk.Listbox(self.outFrame, height = 3, yscrollcommand = self.savedStoryScroll.set)
		self.savedStoryScroll.config(command = self.savedStoryLsBox.yview)
		self.savedStoryLsBox.bind("<Double-Button-1>", self.loadStory)
		#************ PACKING WIDGETS *****************************************#
		self.outFrame.grid(row = 2, column = 1, rowspan = 5, columnspan = 2, padx = self.frameExtPadX, pady = self.frameExtPadY)
		self.genStoryBttn.grid(row = 0, column = 0, columnspan = 3, padx = self.bttnPadX, pady = self.bttnPadY)
		self.outTxt.grid(row = 1, column = 0, columnspan = 3)
		self.saveBttn.grid(row = 2, column = 0,  padx = self.bttnPadX, pady = self.bttnPadY)
		self.txtScroll.grid(row = 1, column = 3, sticky = "NS")
		self.savedStoryLsBox.grid(row = 2, column = 1, pady = 5, padx = self.entrPadX, sticky = "NES")
		self.savedStoryScroll.grid(row = 2, column = 2, sticky ="NWS", pady = 5)

		for i in range(len(self.savedStories)): #Inserts previously saved stories into the listbox upon launch
			self.savedStoryLsBox.insert(tk.END, self.savedStories[i])

		#Storing Widgets by Types in Lists for Configuration
		self.frameLs.extend([self.storyFrame, self.heroFrame, self.mntrFrame, self.trialFrame, self.fChllngeFrame, self.endFrame, self.outFrame, self.accFrame])
		self.labelLs.extend([self.genreLbl, self.strtPlaceLbl, self.heroNmLbl, self.heroStrngthLbl, self.heroGenderLbl, self.mntrNmLbl, self.mntrGftLbl, self.trialCntLbl, self.trialLocLbl, self.trialNmLbl, self.fChllngeLocLbl, self.fChllngeNmLbl, self.trnsprtHmLbl, self.rsltLbl, self.hCLbl, self.fntSizeLbl])
		self.entryLs.extend([self.strtPlaceEntr, self.heroNmEntr, self.heroStrngthEntr1, self.heroStrngthEntr2, self.heroStrngthEntr3, self.mntrNmEntr, self.mntrGftEntr, self.fChllngeLocEntr, self.fChllngeNmEntr, self.trnsprtHmEntr, self.rsltEntr])
		self.oMenuLs.extend([self.genreOMenu])
		self.cBttnLs.extend([self.hCCBox])
		self.rBttnLs.extend([self.heroGenderMRBttn, self.heroGenderFRBttn])
		self.spBxLs.extend([self.trialCntSpBx, self.fntSizeSpBx])
		self.bttnLs.extend([self.genStoryBttn, self.saveBttn]) #Excluded txt to speach button as doesn't use the same font
		self.txtLs.extend([self.outTxt])

		#Calls configWidgets to apply default configurations
		self.configWidgets()

		#Step 3: Initialize window
		self.root.mainloop()

#**** Functions ******************************************************************************************************************************************

	def genStory(self):
		#************ STORES ENTRY VALUES AS TEMPORARY VARIABLES *****************************************
		genreVar = self.genre.get()
		strtPlace = self.strtPlaceEntr.get()
		heroNm = self.heroNmEntr.get()
		heroGender = self.heroGender.get()
		heroHeShe = ""
		heroHimHer = ""
		heroHisHer = ""
		if(heroGender == ""):
			self.outPutTxtToBox(1, "Invalid Gender Selected")#Outputs error to textbox if no gender is selected
			return
		elif(heroGender == "male"): #Sets gender specific words to respective word depending on gender of hero
			heroHimHer = "him"
			heroHeShe = "He"
			heroHisHer = "his"
		elif(heroGender == "female"):
			heroHimHer = "her"
			heroHeShe = "She"
			heroHisHer = "her"
		heroStrngth1 = self.heroStrngthEntr1.get()
		heroStrngth2 = self.heroStrngthEntr2.get()
		heroStrngth3 = self.heroStrngthEntr3.get()
		mntrNm = self.mntrNmEntr.get()
		mntrGft = self.mntrGftEntr.get()
		trialNmLs = []
		trialLocLs = []
		for i in range(len(self.dynamicTrialEntries)): #Stores trial loc and name values in respective lists
			for t in range(len(self.dynamicTrialEntries[i])):
				if(t == 0):
					trialLocLs.append(self.dynamicTrialEntries[i][t].get())
				if(t == 1):
					trialNmLs.append(self.dynamicTrialEntries[i][t].get())
		fChllngeLoc = self.fChllngeLocEntr.get()
		fChllngeNm = self.fChllngeNmEntr.get()
		trnsprtHm = self.trnsprtHmEntr.get()
		rslt = self.rsltEntr.get()



		#************ CONSTRUCTS STORY OUTPUT STRING *****************************************#
		#print("Generating story...")
		storyStr = "---STAGE 1---\n-Hero is called to adventure\n-Hero is reluctant to go\n-Hero is given aid from a mentor\n-Hero leaves from starting point 'crossing a threshold'\n\n"

		#Checks what the genre of the story is, Introduction of story changes based on the genre
		if(genreVar == self.genreOptions[0]):#Genre is Action
			storyStr += self.getRandItemFromLs(self.actnStrtSntnce)
			storyStr += (" " + strtPlace+", ")
			storyStr += self.getRandItemFromLs(self.actnHeroIntroSntnce)
			storyStr += (" " + heroNm+ ". ")
			storyStr += (heroNm + " had " + heroStrngth2 + ", " + heroStrngth3 + " and " + heroStrngth1 + ". ")
			storyStr += (" "+ self.getRandItemFromLs(self.actnMentorIntroSntnce) + " " + mntrNm+" approached " + heroHimHer + ". " )
			
		elif(self.genre.get() == self.genreOptions[1]):#Genre is Fantasy
			storyStr += self.getRandItemFromLs(self.fntsyStrtSntnce)	
			storyStr += (" " + strtPlace+", ")
			storyStr += self.getRandItemFromLs(self.fntsyHeroIntroSntnce)
			storyStr += (" " + heroNm+ ". ")
			storyStr += (heroNm + " had " + heroStrngth2 + ", " + heroStrngth3 + " and " + heroStrngth1 + ".")
			storyStr += (" "+ self.getRandItemFromLs(self.fntsyMentorIntroSntnce) + " " + mntrNm+" approached " + heroHimHer + ". " )

		else:
			self.outPutTxtToBox(1, "Invalid Genre Selected") #Outputs error message to text box if no genre is selected and stops the genStory function
			return 

		#Generates the rest of the story that isnt affected by the genre	
		storyStr += (mntrNm + " told " + heroNm + " of how " + heroHeShe.lower() + " must " + fChllngeNm + " in order to " + rslt + ". ")
		storyStr += (self.getRandItemFromLs(self.mntrTrialIntroSntnce) + mntrNm + ". ")
		storyStr += (self.getRandItemFromLs(self.mntrFirstTrialDescriptionSntnce) + trialLocLs[0] + self.getRandItemFromLs(self.heroDestinySntnce) + trialNmLs[0] + ".\" ")
		if(len(trialLocLs) >= 2):
			storyStr += (self.getRandItemFromLs(self.mntr23TrialDescriptionSntnce) + trialLocLs[1] + self.getRandItemFromLs(self.heroDestinySntnce) + trialNmLs[1] + ".\" ")
		if(len(trialLocLs) >= 3):
			storyStr += (self.getRandItemFromLs(self.mntr23TrialDescriptionSntnce) + trialLocLs[2] + self.getRandItemFromLs(self.heroDestinySntnce) + trialNmLs[2] + ".\" ")
		storyStr += (self.getRandItemFromLs(self.mntrFChllngeIntroSntnce) + fChllngeLoc + self.getRandItemFromLs(self.heroDestinySntnce) + fChllngeNm + " and " + rslt + ".\" ")
		storyStr += (self.getRandItemFromLs(self.heroReluctanceSntnce)+ heroNm + ". ")
		storyStr += (self.getRandItemFromLs(self.mntrGiftGivingSntnce) + mntrGft + self.getRandItemFromLs(self.mntrGiftAidSntnce) + "\n")
		storyStr += "\n---STAGE 2---\n-Hero faces a series of trials\n-Hero learns something through the trials\n-Hero goes to 'innermost cave' where the final challenge is\n\n"
		storyStr += (self.getRandItemFromLs(self.heroDepartSntnce) + strtPlace + " and journeyed to " + trialLocLs[0] + ". ")
		storyStr += ("Here, " + heroHeShe.lower() + " " + trialNmLs[0] + " using " + heroHisHer + " " + heroStrngth1 + ". ")
		if(len(trialLocLs) >= 2):
			storyStr += (heroHeShe + " then traveled to " + trialLocLs[1] + " and using " + heroHisHer + " " +  heroStrngth2 + ", " + heroHeShe.lower() + " " + trialNmLs[1] + ". ")
		if(len(trialLocLs) >= 3):
			storyStr += ("Finally, "+ heroHeShe.lower() + "  proceeded to " + trialLocLs[2] + " and with " + heroHisHer + " " +  heroStrngth3 + ", " + heroHeShe.lower() + " " + trialNmLs[2] + ". ")
		storyStr += ("With this, our hero was prepared to " + fChllngeNm + " at " + fChllngeLoc + ", and so there " + heroHeShe.lower() + " journeyed. ")
		storyStr += ("Using all of " + heroHisHer + " skills, " + heroNm + " " + fChllngeNm + " . ")
		storyStr += "\n\n---STAGE 3---\n-Hero returns from their journey\n-Hero offers a solution to the initial problem\n-Hero has to learn to reintigrate with society\n\n"
		storyStr += ("With this, " + heroNm + " " + rslt +  " and returned to " + strtPlace + " by " + trnsprtHm + ", where " + heroHeShe.lower() + " was recieved as a true hero.")

		self.outPutTxtToBox(0, storyStr) #Passes storyStr to outputTxtToBox function to be outputted	

	def outPutTxtToBox(self, isError, outStr):#isError = 0 or 1 : false or true
		self.outTxt.config(state = "normal")
		self.outTxt.delete(1.0, tk.END)#clears output text box
		if(isError == 1):
			self.outTxt.insert(tk.END, "Error while attempting to generate story: \nError Message: "+ outStr)
		else:
			self.outTxt.insert(tk.END, outStr)
		self.outTxt.config(state = "disabled")

	def saveStory(self, *args):
		storyName = "SavedStory" + str(self.savedStoryCntr) + ".txt"
		f = open(storyName, "w+")
		f.write(self.outTxt.get(1.0, tk.END))
		f.close()
		self.savedStories.append(storyName)
		f = open(self.SAVEDSTORIESDOC, "a+")
		f.write(storyName + "\n")
		f.close()
		self.savedStoryCntr+= 1

		self.savedStoryLsBox.insert(tk.END, storyName)

	def loadStory(self, event):
		t = ""
		f = open(self.savedStories[event.widget.curselection()[0]], "r")
		t = f.read()
		f.close()
		self.outPutTxtToBox(0, t)
		
	def handleTextToSpeech(self, *args):
	
		
		string = ""
		if(self.txtToSpeechRead == 1):
			string = self.txtToSpeechSntnce
			self.txtToSpeechRead = -1
		else:
			string = self.outTxt.get(1.0, tk.END)
			self.txtToSpeechRead = 1
			print("reading story")
		print("got here")
		t = myThread(string)
		t.start()#Creates a thread to read text to speach

	def changeHighContrast(self, *args): #Handles high contrast being turned on and off 1 = on, 0 = off
		
		if(self.enableHighContrast.get() == 1):
			#High Contrast
			self.windowBgrndClr = self.GRAY
			self.frameBgrndClr = self.BLACK
			self.lblFntClr = self.PURPLE
			self.lblBgrndClr = self.BLACK
			self.titleFontClr = self.DARK_PURPLE
			self.titleBgrndClr = self.DARK_GRAY
			self.entrBgrndClr = self.LIGHT_GRAY
			self.entrFntClr  = self.ORANGE
			self.entrTempFntClr = self.DARK_ORANGE


		else:
			#Default
			self.frameBgrndClr = self.BLUE
			self.lblBgrndClr = self.BLUE
			self.entrBgrndClr = self.LIGHT_BLUE
			self.windowBgrndClr = self.LIGHT_BEIGE
			self.titleBgrndClr = self.BEIGE
			self.titleFntClr = self.DARK_BLUE
			self.lblFntClr = self.BLACK
			self.entrFntClr = self.BLACK
			self.entrTempFntClr = self.LIGHT_GRAY
		
	
		self.configWidgets()
		#Configures all FRAMES

	def configWidgets(self):#Config All Widgets Based On Type -- Used to update colour of widets
		#Configures Window
		self.root.config(background = self.windowBgrndClr)

		#Configures main title label
		self.titleLabel.config(text = self.title, font = self.titleFont, background = self.titleBgrndClr, foreground = self.titleFntClr)

		#Configures all FRAMES
		for i in range(len(self.frameLs)):
			self.frameLs[i].config(bg = self.frameBgrndClr, font = self.guiFrameFont, pady = self.framePadY, padx = self.framePadX, fg = self.lblFntClr)

		#Configures all LABELS
		for i in range(len(self.labelLs)):
			self.labelLs[i].config(bg = self.lblBgrndClr, font = self.guiLblFont, fg = self.lblFntClr)

		#Configures all ENTRIES
		for i in range(len(self.entryLs)):
			self.entryLs[i].config(bg = self.entrBgrndClr, font = self.guiLblFont, fg = self.entrFntClr)

		for i in range(len(self.dynamicTrialEntries)):
			for t in range(len(self.dynamicTrialEntries[i])):
				self.dynamicTrialEntries[i][t].config(background = self.entrBgrndClr, font = self.guiLblFont, fg = self.entrFntClr)
			
		#Configures all OPTIONMENUS
		for i in range (len(self.oMenuLs)):
			self.oMenuLs[i].config(width = self.oMenuWidth, fg = self.lblFntClr)

		#Configures all RADIOBUTTONS
		for i in range (len(self.rBttnLs)):
			self.rBttnLs[i].config(bg = self.lblBgrndClr, font = self.guiLblFont, fg = self.lblFntClr)

		#Configures all CHECKBUTTONS
		for i in range(len(self.cBttnLs)):
			self.cBttnLs[i].config(bg = self.lblBgrndClr, font = self.guiLblFont, fg = self.lblFntClr)

		#Configures all SPINBOXES
		for i in range(len(self.spBxLs)):
			self.spBxLs[i].config(state = "readonly", bg = self.entrBgrndClr, font = self.guiLblFont, justify = tk.RIGHT, fg = self.lblFntClr)

		#Configures all BUTTONS
		for i in range(len(self.bttnLs)):
			self.bttnLs[i].config(font = self.bttnFont, fg = self.lblFntClr)

		#Configures all TEXTBOXES
		for i in range(len(self.txtLs)):
			self.txtLs[i].config(background = self.entrBgrndClr, bd = 5, wrap = tk.WORD, font = self.guiOutTxtFont, state = "disabled", fg = self.entrFntClr)

	def fontSizeUpdated(self, *args): #Handles font size being changed
		newFont = self.fntSizeSpBx.get()
		self.guiLblFont.config(size = newFont)
		self.guiOutTxtFont.config(size = newFont)

	def trialsUpdated(self, *args): #Handles the trial number being changed
		numOfTrials = int(self.trialCntSpBx.get())

		#Destroys Previous Entries in Case the Number of Trials Decreased
		for i in range(0, len(self.dynamicTrialEntries), 1):
			for t in range(0, len(self.dynamicTrialEntries[i]), 1):
				self.dynamicTrialEntries[i][t].destroy()

		self.dynamicTrialEntries = [[],[],[]] #Resets the List

		#Creates New Entries in dynamicTrialEntries list
		for i in  range (0, numOfTrials, 1):
			self.dynamicTrialEntries[i].append(tk.Entry(self.trialFrame, background = self.entrBgrndClr, font = self.guiLblFont, fg = self.entrFntClr))
			self.dynamicTrialEntries[i].append(tk.Entry(self.trialFrame, background = self.entrBgrndClr, font = self.guiLblFont, fg = self.entrFntClr))
			self.dynamicTrialEntries[i][0].grid(row = 4+i, column = 0, columnspan = 2, padx = self.entrPadX, pady = self.entrPadY)
			self.dynamicTrialEntries[i][1].grid(row = 4+i, column = 2, columnspan = 2, padx = self.entrPadX, pady = self.entrPadY)

	def getRandItemFromLs(self, exList): #Returns a random element from a list
		randIndex = random.randint(0, len(exList)-1)		
		return exList[randIndex]



d = Display()


























