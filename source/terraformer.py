# Terraformer for IBM Virtual Private Cloud
#
# Copyright IBM Corporation 2020
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

import os
import sys
import argparse
import json
import yaml
import numpy as np
import pandas as pd

from copyright import *
from messages import *
from structures import *
from genpuml import *
from gentf import *

def main():
   print(terraformermessage)

   parser = argparse.ArgumentParser(description='Generates Terraform and PUML for IBM Virtual Private Cloud')

   datapath = useroptions['datapath']
   parser.add_argument('inputvalue', nargs='?', default=datapath, help='input folder or input filename (default: ' + datapath + ')')

   generation = useroptions['generation']
   parser.add_argument('-g', dest='generation', default=generation, help='1 for VPC Gen1, 2 for VPC Gen2 (default: ' + generation + ')')

   genpath = useroptions['genpath']
   parser.add_argument('-o', action='store', dest='outputfolder', default=genpath, help='folder for generated Terraform files (default: ' + genpath + ')')

   prepend = useroptions['prepend']
   parser.add_argument('-p', dest='prepend', default=prepend, help='prepend string to resource names (default: ' + prepend + ')')

   region = useroptions['region']
   parser.add_argument('-r', dest='region', default=region, help='region for VPC (default: ' + region + ')')

   puml = useroptions['puml']
   parser.add_argument('-d', action='store_true', dest='puml', default=puml, help='generate diagram (default: ' + ('True' if puml else 'False') + ')')

   datavars = useroptions['datavars']
   parser.add_argument('-v', action='store_true', dest='datavars', default=datavars, help='generate variables (default: ' + ('True' if datavars else 'False') + ')')

   parser.add_argument('--version', action='version', version='%(prog)s ' + COPYRIGHT.split(' ')[1])

   results = parser.parse_args()

   useroptions['datapath'] = results.inputvalue
   useroptions['datavars'] = results.datavars
   useroptions['generation'] = results.generation
   useroptions['genpath'] = results.outputfolder
   useroptions['prepend'] = results.prepend
   useroptions['puml'] = results.puml
   useroptions['region'] = results.region

   inputvalue = results.inputvalue
   if (os.path.isdir(inputvalue)):
      # If inputvalue is a dir that is found then process all files.
      datapath = inputvalue
      filelist = os.listdir(datapath)
      found = False
      for afile in filelist:
         propfile = os.path.join(datapath, afile)
         propfilenopath = os.path.basename(propfile)
         propname = os.path.splitext(propfilenopath)[0]
         propext = os.path.splitext(propfilenopath)[1][1:]
         if (os.path.isfile(propfile)):
            found = True
            useroptions['propfile'] = propfile
            useroptions['propname'] = propname
            useroptions['propext'] = propext
            gentf(useroptions)
            if (useroptions['puml'] and propname == 'vpc'):
               genpuml(useroptions)
      if (not found):
         print(missinginputmessage % results.inputvalue)
   elif (os.path.isfile(inputvalue)):
      # If inputvalue is a file that is found then process file.
      propfile = inputvalue
      propfilenopath = os.path.basename(propfile)
      propname = os.path.splitext(propfilenopath)[0]
      propext = os.path.splitext(propfilenopath)[1][1:]
      useroptions['propfile'] = propfile
      useroptions['propname'] = propname
      useroptions['propext'] = propext
      gentf(useroptions)
      if (useroptions['puml'] and propname == 'vpc'):
         genpuml(useroptions)
   elif (os.path.isfile(os.path.join(datapath, inputvalue))):
      # Add path to inputvalue and if found then process the file. 
      propfile = os.path.join(datapath, inputvalue)
      propfilenopath = os.path.basename(propfile)
      propname = os.path.splitext(propfilenopath)[0]
      propext = os.path.splitext(propfilenopath)[1][1:]
      useroptions['propfile'] = propfile
      useroptions['propname'] = propname
      useroptions['propext'] = propext
      gentf(useroptions)
      if (useroptions['puml'] and propname == 'vpc'):
         genpuml(useroptions)
   else:
      print(invalidinputmessage % results.inputvalue)

   return
      
main()
