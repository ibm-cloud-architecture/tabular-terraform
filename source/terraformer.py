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

from messages import *
from generators import *

def main():
   datavars = False
   individual = False
   generation = '2'
   region = 'Dallas'
   prepend = ''
   genheader = '# Terraformer generated file'
   genpath = 'resources'
   datafolder = 'data'
   datatype = 'xlsx'
   propfile = ''
   propname = '*'
   propext = 'xlsx'
   print(terraformermessage)
   parser = argparse.ArgumentParser(description='Generates Terraform for IBM Virtual Private Cloud')
   datapath = datafolder
   parser.add_argument('inputvalue', nargs='?', default=datapath, help='input folder or input filename (default: ' + datapath + ')')
   parser.add_argument('-o', action='store', dest='outputfolder', default=genpath, help='folder for generated Terraform files (default: ' + genpath + ')')
   parser.add_argument('-g', dest='generation', default='2', help='1 for VPC Gen1, 2 for VPC Gen2 (default: 2)')
   parser.add_argument('-r', dest='region', default='Dallas', help='region for VPC (default: Dallas)')
   parser.add_argument('-p', dest='prepend', default='', help='prepend string to resource names (default: \'\')')
   parser.add_argument('-d', action='store_true', dest='datavars', default=False, help='generate variables for data (default: False)')
   parser.add_argument('--version', action='version', version='%(prog)s ' + COPYRIGHT.split(' ')[1])
   results = parser.parse_args()

   genpath = results.outputfolder
   datavars = results.datavars
   region = results.region
   prepend = results.prepend
   generation = results.generation

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
            generateall(propfile, propname, propext, generation, datavars, genpath, region, individual, prepend)
      if (not found):
         print(missinginputmessage % results.inputvalue)
   elif (os.path.isfile(inputvalue)):
      # If inputvalue is a file that is found then process file.
      propfile = inputvalue
      propfilenopath = os.path.basename(propfile)
      propname = os.path.splitext(propfilenopath)[0]
      propext = os.path.splitext(propfilenopath)[1][1:]
      generateall(propfile, propname, propext, generation, datavars, genpath, region, individual, prepend)
   elif (os.path.isfile(os.path.join(datapath, inputvalue))):
      # Add path to inputvalue and if found then process the file. 
      propfile = os.path.join(datapath, inputvalue)
      propfilenopath = os.path.basename(propfile)
      propname = os.path.splitext(propfilenopath)[0]
      propext = os.path.splitext(propfilenopath)[1][1:]
      generateall(propfile, propname, propext, generation, datavars, genpath, region, individual, prepend)
   else:
      print(invalidinputmessage % results.inputvalue)

   return
      
main()
