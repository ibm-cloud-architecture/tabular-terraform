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

from constants import *
from structures import *
from messages import *
from helpers import *
from extractors import *

# Constants

genheader = '# Terraformer generated file\n'

# Search functions (puml)

def findrow(gettype, rowname, useroptions):
   sheets = loadfile(useroptions)

   for name, sheet in sheets.items():
      name = name.replace(' ', '')
      pos = name.find('-')
      if pos >= 0:
         sheettype = name[0:pos] 
         sheetgroup = name[pos+1]
      else:
         sheettype = name
         sheetgroup = ''

      if sheettype == gettype:
         df = loadframe(pd, sheet, useroptions)
         columns = df.columns
         for index, row in df.iterrows():
            # Skip rows with no name - values in other columns are used for arrays.
            name = row['name']
            empty = novalue(name)
            if empty:
                continue

            if row['name'] == rowname:
               return row

   return None

def getsheets(gettype, useroptions):
   sheetlist = []   
   sheets = loadfile(useroptions)

   for name, sheet in sheets.items():
      name = name.replace(' ', '')
      pos = name.find('-')
      if pos >= 0:
         sheettype = name[0:pos] 
         sheetgroup = name[pos+1]
      else:
         sheettype = name
         sheetgroup = ''

      if sheettype == gettype:
         sheetlist.append(sheet)

   return sheetlist

# Generate functions

def genpuml(useroptions):
   datavars = useroptions['datavars']
   generation = useroptions['generation']
   genpath = useroptions['genpath']
   propfile = useroptions['propfile']
   propname = useroptions['propname']
   region = useroptions['region']

   print(startpumlmessage % (generation, propfile))

   sheets = loadfile(useroptions)

   sheetlist = getsheets('networkinterfaces', useroptions)
   #for sheet in sheetlist: 
   #  print(sheet)

   nicrow = findrow('networkinterfaces', "vsi1nic0", useroptions)
   nicsubnet = nicrow['subnet']
   nicfip = nicrow['floating_ip']

   subnetrow = findrow('subnets', nicsubnet, useroptions)
   subnetzone = subnetrow['zone']
   subnetvpc = subnetrow['vpc']

   pumlfile = os.path.join(genpath, subnetvpc + "-diagram.puml")
   puml = open(pumlfile, 'w')

   puml.write('@startuml ' + subnetvpc + '-diagram\n')

   puml.write('!include ../dist/common.puml\n')
   puml.write('!include ../dist/Applications/common.puml\n')
   puml.write('!include ../dist/Applications/EnterpriseApplications.puml\n')
   puml.write('!include ../dist/Data/DataSources.puml\n')
   puml.write('!include ../dist/Data/EnterpriseData.puml\n')
   puml.write('!include ../dist/Data/EnterpriseUserDirectory.puml\n')
   puml.write('!include ../dist/Security/Firewall.puml\n')
   puml.write('!include ../dist/Users/user.puml\n')
   puml.write('!include ../dist/Users/device.puml\n')

   puml.write('!include ../dist/VPC/DataCenter.puml\n')
   puml.write('!include ../dist/VPC/DirectLink.puml\n')
   puml.write('!include ../dist/VPC/FloatingIP.puml\n')
   puml.write('!include ../dist/VPC/Instance.puml\n')
   puml.write('!include ../dist/VPC/Internet.puml\n')
   puml.write('!include ../dist/VPC/LoadBalancer.puml\n')
   puml.write('!include ../dist/VPC/PublicGateway.puml\n')
   puml.write('!include ../dist/VPC/Router.puml\n')
   puml.write('!include ../dist/VPC/VPNGateway.puml\n')
   puml.write('!include ../dist/VPC/VPNConnection.puml\n')

   puml.write('PublicNetwork(public, Public Network){\n')
   puml.write('user(user1, User)\n')
   puml.write('Internet(internet, Internet)\n')
   puml.write('}\n')

   puml.write('Cloud(cloud, IBM Cloud){\n')
   puml.write('Region(dallas, Dallas){\n')
   puml.write('VPC(vpc1, ' + subnetvpc + '){\n')
   puml.write('Zone(dallas1, ' + subnetzone + '){\n')
   puml.write('Subnet(subnet1, ' + nicsubnet + '){\n')
   puml.write('Instance(vsi1, ' + 'vsi1' + ')\n')
   puml.write('FloatingIP(fip1, ' + nicfip + ')\n')
   puml.write('}\n')
   puml.write('}\n')
   puml.write('}\n')
   puml.write('}\n')
   puml.write('}\n')

   puml.write('user1 -> internet\n')
   puml.write('internet <--> fip1\n')
   puml.write(nicfip + ' - ' + 'vsi1\n')
   puml.write('@enduml\n')

   puml.close()

   print(donepumlmessage % (propname, genpath))

   return
