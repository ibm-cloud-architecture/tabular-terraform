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

# Generate functions

def provider(genpath, region, generation):
   file = os.path.join(genpath, providerfile%'ibm')
   tf = open(file, 'w')
   tf.write(genheader)
   tf.write('terraform { required_version = ">= 0.12.0" }\n')
   tf.write('provider "ibm" {\n')
   #tf.write('bluemix_api_key = "${var.bluemixkey}"\n')
   element = region
   if generation == '2':
      if element in gen2regionsdictionary.keys():
         reference = gen2regionsdictionary[element]
      else:
         print(missingregionmessage % element)
         tf.close()
         return
   else:
      if element in gen1regionsdictionary.keys():
         reference = gen1regionsdictionary[element]
      else:
         print(missingregionmessage % element)
         tf.close()
         return
   tf.write('region = "' + reference + '"\n')
   tf.write('generation = "' + generation + '"\n')
   tf.write('}\n')
   tf.close()
   return

def generatevariables(sheetname, name, sheet, df, details, useroptions):
   genpath = useroptions['genpath']
   prepend = useroptions['prepend']
   
   print(processingsheetmessage % name)

   resourcetype = details['resource']
   filetype = details['file']
   fieldstype = details['fields']
   structurestype = details['structures']
   parenttype = details['parent']
   parentfiletype = details['parentfile']

   file = os.path.join(genpath, filetype)
   tf = open(file, 'w')
   tf.write(genheader)

   columns = df.columns
   for index, row in df.iterrows():
      # Skip rows with no name.
      name = row['name']
      empty = novalue(name)
      if empty:
         continue

      details = getdetails('name', fieldstype)
      originalname = name
      if doprepend(details):
         name = prepend + name

      value = row['value']
      empty = novalue(value)
      if isrequired(details) and empty:
         print(missingvaluemessage % ('value', str(2)))
         continue

      type = row['type']

      description = row['description']

      column = columns[1]
      field = column

      newvalue = getvalue(field, column, row, fieldstype)
      if newvalue != '':
         tf.write(varsyntax2 % (name, newvalue))

   tf.close()
   return

def generatesheet(sheetname, name, sheet, df, details, useroptions):
   datavars = useroptions['datavars']
   generation = useroptions['generation']
   genpath = useroptions['genpath']
   individual = useroptions['individual']
   prepend = useroptions['prepend']
   propname = useroptions['propname']

   timeoutsave = ''
   protocolsave = ''
   protocolvaluesave = ''

   print(processingsheetmessage % name)

   resourcetype = details['resource']
   filetype = details['file']
   fieldstype = details['fields']
   structurestype = details['structures']
   parenttype = details['parent']
   parentfiletype = details['parentfile']

   aclseparator = False

   saveparentname = None

   if datavars:
      varsfile = os.path.join(genpath, varsfilename % propname)
      varstf = open(varsfile, 'a')
   else:
      varstf = None

   df = loadframe(pd, sheet, useroptions)

   columns = df.columns
   for index, row in df.iterrows():
      # Skip rows with no name.
      name = row['name']
      empty = novalue(name)
      if empty:
         continue

      details = getdetails('name', fieldstype)
      originalname = name
      if doprepend(details):
         name = prepend + name

      # Force individual for json due to random order which also required checking for aclrules here so acl rules are not individual files.
      # @revisit doing this for json.
      if (individual or parenttype == '') and not sheetname == 'aclrules': 
         file = os.path.join(genpath, filetype % name)
         tf = open(file, 'w')
         tf.write(genheader)
      else:
         parentname = getparent(originalname, row, parenttype, details, useroptions)
         if parentname == '':
            return
         saveparentname = parentname
         parentname = saveparentname
         file = os.path.join(genpath, parentfiletype % parentname)
         tf = open(file, 'a')

      if sheetname == 'aclrules':
         tf.write('rules {\n')
      elif sheetname == 'sgrules':
         resourcetype = sgruleresource
         tf.write(resourceheader % (resourcetype, name))
         tf.write(' {\n')
      else:
         if sheetname == 'provider':
            tf.write('provider ' + '"' + name + '" {\n')
         else:
            tf.write(resourceheader % (resourcetype, name))
            tf.write(' {\n')
      if gen(details):
         if isvariable(name):
            tf.write('name = ' + name + '\n')
         elif datavars:
            varstf.write(varsyntax % (name, 'name', name))
            tf.write('name = ' + (refsyntax % (name, 'name')) + '\n')
         else:
            tf.write('name = "' + name + '"\n')
      newtype = ''
      lasttype = ''
      timeoutused = False
      for pos in range(columns.size):
         column = columns[pos]
         details = getdetails(column, fieldstype)
         value = row[column]
         empty = novalue(value)
         field = column
         if not gen(details):
            continue
         if isrequired(details):
            required = True
         else:
            required = False
         if isgen2required(details):
            gen2required = True
         else:
            gen2required = False
         if isoptional(details):
            optional = True
         else:
            optional = False
         if required and empty:
            print(missingvaluemessage % (column, str(pos)))
            continue
         if gen2required and generation == '1':
            # Skip generating vpc for acl in gen1, optional in gen1, required in gen2, but received an error in gen1 if this field is specified.
            continue
         # @revisit following case only happens on vpc address prefixes after first row.
         if not empty:     
            # @revisit whehter value = row[column] set above be used here.
            value = getvalue(field, column, row, fieldstype, prepend, generation)
            if value != '':
               # @revisit timeout
               if (istimeout(details)):
                  field = getfield(details)
                  if datavars:
                     varstf.write(varsyntax % (name, field, value))
                     timeoutsave = timeoutsave + field + ' = ' + (refsyntax % (name, field)) + '\n'
                  else:
                     timeoutsave = timeoutsave + field + ' = "' + value + '"\n'
                  continue
               # @revisit protocol 
               if (isprotocol(details)):
                  protocolsave = value
                  continue
               if (isprotocolvalue(details)):
                  # JSON loads protocol values as floats so convert to ints.  
                  # @Revist whether this can be changed on the JSON load.
                  floatvalue = float(value)
                  value = int(floatvalue)
                  field = getfield(details)
                  if datavars:
                     varstf.write(varsyntax % (name, field, value))
                     protocolvaluesave = protocolvaluesave + field + ' = ' + (refsyntax % (name, field)) + '\n'
                  else:
                     protocolvaluesave = protocolvaluesave + field + ' = ' + str(value) + '\n'
                  continue
               if sheetname == 'instances':
                  if 'primary_nic' in field:
                     if not structurestarted:
                        structurestarted = True
                        tf.write('primary_network_interface = {\n')
               if sheetname == 'pubgateways' and field == 'floating_ip_id':
                  tf.write('floating_ip = {\n')
                  # @revisit
                  closepubfip = True
               else:
                  closepubfip = False
               if isprimarynic(details):
                  primarynic(varstf, tf, value, details, useroptions)
               elif isnetworkinterfaces(details):
                  networkinterfaces(tf, value, details, useroptions)
               elif not sheetname == 'aclrules' or field != 'acl':
                  if field != 'name':
                     field = getfield(details)
                     if isstring(details) and not isarray(details):
                        if isresource(details) or isfile(details): 
                           tf.write(field + ' = ' + value + '\n')
                        else:
                           if isvariable(value):
                              tf.write(field + ' = ' + value + '\n')
                           elif datavars:
                              varstf.write(varsyntax % (name, field, value))
                              tf.write(field + ' = ' + (refsyntax % (name, field)) + '\n')
                           else:
                              tf.write(field + ' = "' + value + '"\n')
                     elif isint(details):
                        tf.write(field + ' = ' + str(value) + '\n')
                     else:
                        # Arrays
                        tf.write(field + ' = ' + value + '\n')
               if closepubfip == True:
                  # @revisit better way
                  tf.write('}\n')
      
      if (timeoutsave != ''):
         tf.write('timeouts {\n')
         tf.write(timeoutsave)
         tf.write('}\n')
         timeoutsave = ''

      if (protocolsave != ''):
         if (protocolvaluesave != ''):
            tf.write(protocolsave + ' {\n')
            tf.write(protocolvaluesave)
            tf.write('}\n')
         protocolsave = ''
         protocolvaluesave = ''

      if not sheetname == 'aclheaders':
         tf.write('}\n')
      if sheetname == 'aclrules':
         aclseparator = True
     
      tf.close()
   if sheetname == 'aclrules':
      file = os.path.join(genpath, parentfiletype % saveparentname)
      tf = open(file, 'a')
      tf.write('}\n')
      tf.close()

   if datavars:
      varstf.close()

   return

def gentf(useroptions):
   datavars = useroptions['datavars']
   generation = useroptions['generation']
   genpath = useroptions['genpath']
   propfile = useroptions['propfile']
   propname = useroptions['propname']
   region = useroptions['region']

   print(starttfmessage % (generation, propfile))

   os.makedirs(genpath, exist_ok=True)
   provider(genpath, region, generation)

   if datavars:
      print(processingsheetmessage % ("systemvariables-" + propname))
      varsfile = os.path.join(genpath, varsfilename % propname)
      varstf = open(varsfile, 'w')
      varstf.write(genheader)
      varstf.close()

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
      if sheettype in ['floatingips', 'publicgateways', 'lbpolicies', 'lbrules', 'uservariables', 'systemvariables']:
         continue

      df = loadframe(pd, sheet, useroptions)

      if sheettype == 'volumes':
         volumetable = extractvolumetable(sheet, df)
         if not volumetable.empty:
            generatesheet(sheettype, name, volumetable, volumetable, alldetails[sheettype], useroptions)
      elif sheettype == 'networkinterfaces':
         fiptable = extractinstancefiptable(sheet, df)
         if not fiptable.empty:
            generatesheet('fips', name+'-fips', fiptable, fiptable, alldetails['fips'], useroptions)
      elif sheettype == 'subnets':
         generatesheet(sheettype, name, sheet, df, alldetails[sheettype], useroptions)
         fiptable = extractsubnetfiptable(sheet, df)
         if not fiptable.empty:
            generatesheet('fips', name+'-fips', fiptable, fiptable, alldetails['fips'], useroptions)
         publicgatewaytable = extractsubnetgatewaytable(sheet, df)
         if not publicgatewaytable.empty:
            generatesheet('publicgateways', name+'-publicgateways', publicgatewaytable, publicgatewaytable, alldetails['publicgateways'], useroptions)
      elif sheettype == 'variables':
         generatevariables(sheettype, name, sheet, df, alldetails[sheettype], useroptions)
      else: 
         generatesheet(sheettype, name, sheet, df, alldetails[sheettype], useroptions)

   print(donetfmessage % (propname, genpath))
   return
