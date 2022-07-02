import os
from tkinter import *
from tkinter import ttk
from tkinter import filedialog
import pandas as pd
import numpy as np

userProfile = os.path.expanduser("~").split("\\")[-1]
class XLXFile:
    def __init__(self, path):
        self.path = path
        self.name = path.split("/")[-1].split(".")[0]
        self.ext = path.split(".")[1]

def browseFile(fileType):
    selectedFile = filedialog.askopenfilename(title = "Select {}".format(fileType), filetypes = (("xlsx","*.xlsx*"),("All Files","*.*")))
    if selectedFile != "":
        if fileType == "A":
            global fileA
            fileA = XLXFile(selectedFile)
            fileALabel.config(text = fileA.name + fileA.ext)
        elif fileType == "B":
            global fileB
            fileB = XLXFile(selectedFile)
            fileBLabel.config(text = fileB.name + fileB.ext)
        elif fileType == "C":
            global fileC
            fileC = XLXFile(selectedFile)
            fileCLabel.config(text = fileC.name + fileC.ext)
            



mainRoot = Tk()
mainRoot.geometry("685x300")
mainRoot.title("Transaction Company")
mainFrame = Frame(mainRoot)
mainFrame.pack(fill = BOTH, expand = 1, padx = 10, pady = 20)

Label(mainFrame, text = "Data Manager", font = ("JUST DO GOOD",15)).grid(column = 1, row = 0,columnspan = 4)
ttk.Separator(mainFrame, orient=HORIZONTAL).grid(sticky = E+W,row=1,column=0,columnspan=6, pady = 10)

Button(mainFrame, text ="Select File Input", command = lambda:[browseFile("A")],height=2, relief = "ridge").grid(sticky = "ew",row=2,column=0,columnspan=2)
Button(mainFrame, text ="Select File Data", command = lambda:[browseFile("B")],height=2, relief = "ridge").grid(sticky = "ew",row=2,column=2,columnspan=2)
Button(mainFrame, text ="Select File Output", command = lambda:[browseFile("C")],height=2, relief = "ridge").grid(sticky = "ew",row=2,column=4,columnspan=2)

fileALabel = Label(mainFrame, text="No file Selected",width = 30,height=2)
fileBLabel = Label(mainFrame, text="No file Selected",width = 30,height=2)
fileCLabel = Label(mainFrame, text="No file Selected",width = 30,height=2)
fileALabel.grid(row=3,column=0,columnspan=2)
fileBLabel.grid(row=3,column=2,columnspan=2)
fileCLabel.grid(row=3,column=4,columnspan=2)

ttk.Separator(mainFrame, orient=HORIZONTAL).grid(sticky = E+W,row=4,column=0,columnspan=6, ipadx=100)

Label(mainFrame,text = "Alternatif Name To Be Saved :", relief = "groove",height = 2).grid(sticky = "ew",column = 0,row = 5, columnspan = 2,pady = 10)
alterName = Entry(mainFrame,width = 21,font=("Times New Roman",15),justify = "center")
alterName.grid(row = 5, column = 3,padx=(15,0))

ttk.Separator(mainFrame, orient=HORIZONTAL).grid(sticky = E+W,row=7,column=0,columnspan=6, ipadx=100)
Button(mainFrame,text = "Start",command = lambda: [mainProcess()], bg='#FF6900', fg='black', font= ("JUST DO GOOD",13)).grid(sticky = E+W, row=9,columnspan=6, pady = 10)

finalLabel = Label(mainFrame,text = "",width = 60)
finalLabel.grid(row=10,column=0,columnspan=4)

ttk.Separator(mainFrame, orient=HORIZONTAL).grid(sticky = E+W,row=10,column=0,columnspan=6, ipadx=100)
Label(mainFrame, text = "Copyright Company").grid(row = 10, column = 0, columnspan = 6)
mainRoot.mainloop()