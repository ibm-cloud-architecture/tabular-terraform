# @file main.py
#
# Copyright IBM Corporation 2021
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import sys
import argparse
import configparser

import tkinter
from tkinter import filedialog
from tkinter import IntVar
from tkinter import messagebox

from util import *
from load import *
from gentf import *

class Config:
    def __init__(self,appName):
        
        # platform specific...
        if self.isWindows():
            self.filename = appName + ".ini"
        else:
            self.filename =  os.path.expanduser('~') + '/Library/Application Support/' + appName + ".ini"
        
        self.config = configparser.ConfigParser()
        if os.path.exists(self.filename):
            self.config.read(self.filename)
        if not self.config.has_section("parameters"):
            self.config.add_section("parameters")

        # platform specific...
        if not self.has("inputDirectory"):
            if self.isWindows():
                self.setInputDirectory("./" + appName)
            else:
                self.setInputDirectory(os.path.expanduser('~') + '/' + appName)

        # platform specific...
        if not self.has("outputDirectory"):
            if self.isWindows():
                self.setOutputDirectory("./" + appName)
            else:
                self.setOutputDirectory(os.path.join(os.path.expanduser('~'), 'Documents', TOOLNAME))

    def isWindows(self):
        return hasattr(sys, 'getwindowsversion')

    def get(self,propertyName):
        if propertyName in self.config["parameters"]:
            return self.config["parameters"][propertyName]
        else:
            return None
    
    def set(self,propertyName,value):
        self.config.set("parameters",propertyName,value)
        
    def has(self,propertyName):
        return self.config.has_option("parameters",propertyName)

    def write(self):
        with open(self.filename, 'w') as configfile:
            self.config.write(configfile)
            
    #def getAPIKey(self):
    #    return self.get("apiKey")
    
    #def setAPIKey(self,apiKey):
    #    self.set("apiKey",apiKey)

    def getInputDirectory(self):
        return self.get("inputDirectory")
    
    def setInputDirectory(self,inputDirectory):
        self.set("inputDirectory",inputDirectory)

    def getOutputDirectory(self):
        return self.get("outputDirectory")
    
    def setOutputDirectory(self,outputDirectory):
        self.set("outputDirectory",outputDirectory)

class generate():
   top = tkinter.Tk()
   top.title(TOOLNAME + ' ' + COPYRIGHT.split(' ')[2])
   statusText = tkinter.StringVar()

   #print(COPYRIGHT)
   #print(toolheader)

   def main(self): 

        config = Config("Tabular Terraform")  
        #self.apiKey = config.getAPIKey()
        self.inputDirectory = config.getInputDirectory()
        self.outputDirectory = config.getOutputDirectory()
      
        parser = argparse.ArgumentParser(description='Tabular Terraform')

        parser.add_argument('-i', dest='inputdirectory',  default=userdata['inputdirectory'], help='input directory')
        parser.add_argument('-o', dest='outputdirectory', default=os.path.join(self.outputDirectory, userdata['outputdirectory']), help='output folder')
        parser.add_argument('-t', dest='inputtype', default=userdata['inputtype'], help='input type')

        parser.add_argument('-nogui', dest='nogui', action='store_true', help="No gui (batch mode)")
        parser.add_argument('--version', action='version', version='Tabular Terraform ' + COPYRIGHT.split(' ')[1])
        
        args = parser.parse_args()

        inputdirectory = args.inputdirectory.replace(' ', '')
        outputdirectory = args.outputdirectory.replace(' ', '')
        inputtype = args.inputtype.replace(' ', '').lower()

        userdata['inputdirectory'] = inputdirectory
        userdata['outputdirectory'] = outputdirectory
        userdata['inputtype'] = inputtype

        self.minInfo = False

        done = False

        if args.nogui:
            #try: 
                print(COPYRIGHT)
                #print(toolheader)

                # Check for existing input file and exit if not valid.
                #if not os.path.isfile(self.inputFile):
                #    print(invalidinputfilemessage % inputfile)
                #    return

                inputdirectory = userdata['inputdirectory']
                outputdirectory = userdata['outputdirectory']

                #backupdirectory(userdata)

                #if apikey != KEY_PLACEHOLDER and apikey != None and apikey != '':
                #    userdata['inputtype'] = 'rias'
                #    inputbase = apikey
                #    outputfile = inputbase + '.' + outputtype
                #    userdata['outputfile'] = outputfile
                #    print(starttoolmessage % 'RIAS')
                #if inputfolder != INPUT_PLACEHOLDER and inputfolder != None and inputfolder != '':
                if inputdirectory != None and inputdirectory != '':
                    userdata['inputtype'] = 'xslt'
                    #basename = os.path.basename(inputfolder)
                    #inputbase = os.path.splitext(basename)[0]
                    #inputtype = os.path.splitext(basename)[1][1:]
                    #outputfolder = inputbase + '.' + outputtype
                    #userdata['genpath'] = outputfolder
                    print(starttoolmessage % inputdirectory)
                else:
                    return

                # Generate Terraform
                gentf(userdata)

                print(donetoolmessage % outputdirectory)

                done = True
        else:
        
            frame = tkinter.Frame(self.top)
            frame.pack(fill=tkinter.X, side=tkinter.TOP)
            frame.grid_columnconfigure(1, weight=1)            
            row = 1
    
            genbutton = tkinter.Frame(frame)
            eGenerate = tkinter.Button(genbutton, text="Generate Terraform", state='normal', command=lambda: onClickGenerate())
            genbutton.grid(row=row, columnspan=2, sticky=tkinter.E)
            eGenerate.pack(side=tkinter.LEFT)
            row = row + 1
            
            #lAPIKey = tkinter.Entry(frame, bd=5)
            #lAPIKey.insert(0, apikey)
            #lAPIKey.grid(row=row, column=1, sticky=tkinter.W + tkinter.E)
            #config.set("apiKey",apikey)
            #config.write()
            #row = row + 1

            #tkinter.Label(frame, text="Yaml").grid(row=row)
            #lInputFile = tkinter.Label(frame, text=inputfile)
            lInputDirectory = tkinter.Entry(frame, bd=5)
            #lInputDirectory.insert(0, inputdirectory)
            lInputDirectory.grid(row=row, column=1, sticky=tkinter.W + tkinter.E)
            row = row + 1

            #if apikey != KEY_PLACEHOLDER and apikey != None and apikey != '':
            #    lInputFile.delete(0, 'end')
            #    self.inputFile = ''
            #    config.set("inputFile", self.inputFile)
            #    config.write()

            def onClickSelectInputDirectory():
                folder_selected = filedialog.askdirectory(initialdir = self.inputDirectory,title = "Select Input Directory")
                if folder_selected != None and len(folder_selected) > 0:
                    self.inputDirectory = folder_selected
                    #lAPIKey.delete(0, 'end')
                    lInputDirectory.delete(0, 'end')
                    lInputDirectory.insert(0, self.inputDirectory)
                    lInputDirectory.configure(text=self.inputDirectory)
                    #lAPIKey.delete(0, 'end')
                    #self.apiKey = ''
                    #config.set("apiKey", self.apiKey)
                    #config.write()
                    config.set("inputDirectory", self.inputDirectory)
                    config.write()
                    
            inputbutton = tkinter.Frame(frame)
            eSelectInputDirectory = tkinter.Button(inputbutton, text="Select Input Directory", command=lambda: onClickSelectInputDirectory())
            inputbutton.grid(row=row, columnspan=2, sticky=tkinter.E)
            eSelectInputDirectory.pack(side=tkinter.RIGHT)
            row = row + 1

            #inputfile = userdata['inputfile']
            #basename = os.path.basename(inputfile)
            #inputbase = os.path.splitext(basename)[0]
            #inputtype = os.path.splitext(basename)[1][1:]
            #outputfile = inputbase + '.' + outputtype
            #userdata['outputfile'] = outputfile

            #tkinter.Label(frame, text="Output").grid(row=row)
            #lOutputDirectory = tkinter.Label(frame, text=outputfolder)
            lOutputDirectory = tkinter.Entry(frame, bd=5)
            lOutputDirectory.insert(0, outputdirectory)
            #lOutputDirectory.grid(row=row,column=1)
            lOutputDirectory.grid(row=row, column=1, sticky=tkinter.W + tkinter.E)
            row = row + 1

            def onClickSelectOutputDirectory():
                folder_selected = filedialog.askdirectory(initialdir = self.outputDirectory,title = "Select Output Directory")
                if folder_selected != None and len(folder_selected) > 0:
                    self.outputDirectory = folder_selected
                    lOutputDirectory.delete(0, 'end')
                    lOutputDirectory.insert(0, self.outputDirectory)
                    lOutputDirectory.configure(text=self.outputDirectory)
                    config.set("outputDirectory",self.outputDirectory)
                    config.write()
                    userdata['outputdirectory'] = self.outputDirectory
                    
            outputbutton = tkinter.Frame(frame)
            eSelectOutputDirectory = tkinter.Button(outputbutton, text="Select Output Directory", command=lambda: onClickSelectOutputDirectory())
            outputbutton.grid(row=row, columnspan=2, sticky=tkinter.E)
            eSelectOutputDirectory.pack(side=tkinter.RIGHT)
            row = row + 2

            #layoutoptions = [
            #    "Circular Layout", 
            #    "Distributed Recursive Layout", 
            #    "Fruchtermain-Reingold Layout",
            #    "Fruchtermain-Reingold 3D Layout",
            #    "Fruchtermain-Reingold Grid Layout",
            #    "Kamada-Kawai Layout",
            #    "Kamada-Kawai 3D Layout",
            #    "Large Graph Layout",
            #    "Random Layout",
            #    "Random 3D Layout",
            #    "Reingold-Tilford Tree Layout",
            #    "Reingold-Tilford Tree Polar Layout",
            #    "Spherical Layout"]
            #eOutputLayout = tkinter.StringVar(self.top)
            #eOutputLayout.set("Reingold-Tilford Tree Layout")
            #layoutmenu = tkinter.OptionMenu(self.top, eOutputLayout, *layoutoptions)
            #layoutmenu.pack()

            #typeoptions = [
            #    "Generate Drawio", 
            #    "Generate PlantUML"]
            #eOutputType = tkinter.StringVar(self.top)
            #eOutputType.set("Generate Drawio")
            #typemenu = tkinter.OptionMenu(self.top, eOutputType, *typeoptions)
            #typemenu.pack()

            #splitoptions = [
            #    "Generate Single File", 
            #    "Generate Files by Region", 
            #    "Generate Files by VPC"]
            #eOutputSplit = tkinter.StringVar(self.top)
            #eOutputSplit.set("Generate Single File")
            #splitmenu = tkinter.OptionMenu(self.top, eOutputSplit, *splitoptions)
            #splitmenu.pack()

            def onClickGenerate():
                try:
                    self.statusText.set("Starting")
                    frame.after_idle(onClickGenerate)                   

                    #outputlayout = str(eOutputLayout.get())
                    #if outputlayout == "Circular Layout": 
                    #    outputlayout = "circle"
                    #elif outputlayout == "Distributed Recursive Layout": 
                    #    outputlayout = "drl"
                    #elif outputlayout == "Fruchtermain-Reingold Layout":
                    #    outputlayout = "fr"
                    #elif outputlayout == "Fruchtermain-Reingold 3D Layout":
                    #    outputlayout = "fr3d"
                    #elif outputlayout == "Fruchtermain-Reingold Grid Layout":
                    #    outputlayout = "grid_fr"
                    #elif outputlayout == "Kamada-Kawai Layout":
                    #    outputlayout = "kk"
                    #elif outputlayout == "Kamada-Kawai 3D Layout":
                    #    outputlayout = "kk3d"
                    #elif outputlayout == "Large Graph Layout":
                    #    outputlayout = "large"
                    #elif outputlayout == "Random Layout":
                    #    outputlayout = "random"
                    #elif outputlayout == "Random 3D Layout":
                    #    outputlayout = "random_3d"
                    #elif outputlayout == "Reingold-Tilford Tree Layout":
                    #    outputlayout = "rt"
                    #elif outputlayout == "Reingold-Tilford Tree Polar Layout":
                    #    outputlayout = "rt_circular"
                    #elif outputlayout == "Spherical Layout":
                    #    outputlayout = "sphere"
                    #userdata['outputlayout'] = outputlayout

                    #outputtype = str(eOutputType.get())
                    #if outputtype == "Generate Drawio": 
                    #    outputtype = "drawio"
                    #elif outputtype == "Generate PlantUML":
                    #    outputtype = "puml"
                    #userdata['outputtype'] = outputtype

                    #outputsplit = str(eOutputSplit.get())
                    #if outputsplit == "Generate Single File":
                    #    outputsplit = "all"
                    #elif outputsplit == "Generate Files by Region":
                    #    outputsplit = "region"
                    #elif outputsplit == "Generate Files by VPC":
                    #    outputsplit = "vpc"
                    #userdata['outputsplit'] = outputsplit

                    #apikey = self.apiKey
                    #apikey = str(lAPIKey.get())
                    #userdata['apikey'] = apikey 

                    #inputfile = self.inputFile
                    inputdirectory = str(lInputDirectory.get())
                    userdata['inputdirectory'] = inputdirectory
                    basename = os.path.basename(inputdirectory)

                    outputdirectory = str(lOutputDirectory.get())
                    userdata['outputdirectory'] = os.path.join(outputdirectory, basename + '.resources')

                    self.statusText.set("Starting")
                    #print(starttoolmessage % self.inputFile)

                    #if apikey != KEY_PLACEHOLDER and apikey != None and apikey != '':
                    #    userdata['inputtype'] = 'rias'
                    #    inputbase = apikey
                    #    outputfile = str(inputbase) + '.' + outputtype
                    #    userdata['outputfile'] = outputfile
                    #    print(starttoolmessage % 'RIAS')
                    #if inputdirectory != INPUT_PLACEHOLDER and inputdirector != None and inputdirectory != '':
                    #if inputdirectory != None and inputdirectory != '':
                    #    userdata['inputtype'] = 'xslt'
                    #    #basename = os.path.basename(self.inputFile)
                    #    #inputbase = os.path.splitext(basename)[0]
                    #    #inputtype = os.path.splitext(basename)[1][1:]
                    #    #outputfile = inputbase + '.' + outputtype
                    #    #userdata['outputfile'] = outputfile
                    #    print(starttoolmessage % inputdirectory)
                    #else:
                    #    sys.exit()

                    # Generate Terraform
                    genall(userdata)

                    #inputdata = load(userdata)
                    #if inputdata != None:
                    #    userdata['inputdata'] = inputdata

                    #    setupdata = analyze(userdata)
                    #    userdata['setupdata'] = setupdata

                    #    if outputtype == 'puml':
                    #        genpuml(userdata)
                    #    elif outputtype == 'drawio':
                    #        genxml(userdata)
                    #    else:
                    #        print(invalidoutputtypemessage % outputtype)

                    print(donetoolmessage % userdata['outputdirectory'])
                    self.statusText.set("Completed")

                    sys.exit()

                except Exception as error:
                    self.statusText.set("Generate failed")
                    messagebox.showinfo("Generate failed", str(error))
                    #traceback.print_exc()
                    #traceback.print_last()

            eGenerate.pack(side=tkinter.RIGHT)

            self.statusText.set("Ready")    
    
            statusLabel = tkinter.Label(self.top, textvariable=self.statusText)
            statusLabel.pack(side=tkinter.RIGHT)
    
            self.top.mainloop()

#main()

if __name__ == "__main__":
   main = generate()
   main.main()
