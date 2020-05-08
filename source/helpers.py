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

# Helper functions

# isna returns True for NA values such as None or numpy.NaN.
# isna returns False for empty strings or numpy.inf unless  
# set pandas.options.mode.use_inf_as_na = True
# Note: 
# Empty spreadsheet values start out as NaN but if a value is
# added and later deleted then the value can be an empty string.
# Checking pd.isna here doesn't work as value is 'nan'.
def novalue(value):
   empty = pd.isna(value)
   if empty:
      return True
   if isinstance(value, str):
      value = value.replace(' ', '')
      if value == '':
         return True
      else:
         return False
   else:
      return False

def getdetails(field, fieldstype):
   details = fieldstype[field]
   return details

def getfield(details):
   return details[0]

def isstring(details):
   return details[1] == 'string' or details[1] == 'string array'

def isint(details):
   return details[1] == 'int' or details[1] == 'int array'

def isarray(details):
   return details[1] == 'string array' or details[1] == 'int array'

def isrequired(details):
   return (details[2] == 'required') or (details[2] == 'gen2required')

def isgen2required(details):
   return (details[2] == 'gen2required')

def isoptional(details):
   return details[2] == 'optional'

def isreuse(details):
   return details[2] == 'reuse'

def isvariable(value):
   return value.find('var.') != -1

def getaction(details):
   return details[3]

def gen(details):
   return details[3] != 'nogen' 

def nogen(details):
   return details[3] == 'nogen'

def istimeout(details):
   return details[3] == 'timeout'

def isvalue(details):
   return details[3] == 'value'

def isprimarynic(details):
   return details[3] == 'primarynic'

def isnetworkinterfaces(details):
   return details[3] == 'networkinterfaces'

def isprotocol(details):
   return details[3] == 'protocol'

def isprotocolvalue(details):
   return details[3] == 'protocolvalue'

def isfile(details):
   return details[3] == 'file'

def isimage(details):
   return details[3] == 'image'

def isregion(details):
   return details[3] == 'region'

def iszone(details):
   return details[3] == 'zone'

def isimageprofile(details):
   return details[3] == 'imageprofile'

def isvolumeprofile(details):
   return details[3] == 'volumeprofile'

def isvalue(details):
   return details[3] == 'value'

def isresource(details):
   return details[4] != ''

def getresource(details):
   return details[4]

def doprepend(details):
   return details[5]

def loadfile(useroptions):
   propext = useroptions['propext']
   propfile = useroptions['propfile']

   if (propext.lower() == 'json'):
      # Unable to use pd.read_json as it returns error that all arrays must all be same length which is already the case. 
      sheets_raw = yaml.dump(json.load(open(propfile)))
      sheets_raw
      sheets = yaml.load(sheets_raw, Loader=yaml.FullLoader)
      # Combining related resources doesn't work since json to yaml puts resources in random order, so set json to individual for now.
      individual = True
   elif (propext.lower() == 'ods'):
      sheets = pd.read_excel(propfile, sheet_name=None, dtype=object, header=0, engine="odf")
   elif (propext.lower() == 'xls' or propext.lower() == 'xlsx'):
      sheets = pd.read_excel(propfile, sheet_name=None, dtype=object, header=0)
   elif (propext.lower() == 'yml' or propext.lower() == 'yaml'):
      stream = open(propfile, 'r')
      sheets = yaml.load(stream, Loader=yaml.FullLoader)
   else:
      print(invalidinputmessage % propfile)
      sheets = None

   return sheets

def loadframe(pd, sheet, useroptions):
   propext = useroptions['propext']
   propfile = useroptions['propfile']

   df = pd.DataFrame(sheet)

   if (propext.lower() == 'json'):
      # Remove trailing asterisk from column names
      df.rename(columns=lambda x: x[0:-1] if x[-1]=='*' else x, inplace=True)
   elif (propext.lower() == 'ods'):
      df.rename(columns=lambda x: x[1:] if x[0]=='*' else x, inplace=True)
   elif (propext.lower() == 'xls' or propext.lower() == 'xlsx'):
      # Remove leading asterisk from column names
      df.rename(columns=lambda x: x[1:] if x[0]=='*' else x, inplace=True)
   elif (propext.lower() == 'yml' or propext.lower() == 'yaml'):
      # Remove trailing asterisk from column names
      df.rename(columns=lambda x: x[0:-1] if x[-1]=='*' else x, inplace=True)
   else:
      print(invalidinputmessage % propfile)
      sheets = None

   return df

def getnic(nicname, details, useroptions):
   sheets = loadfile(useroptions)
   for sheetname, sheet in sheets.items():
      sheetname = sheetname.replace(' ', '')
      pos = sheetname.find('-')
      if pos >= 0:
         basename = sheetname[0:pos] 
         groupname = sheetname[pos+1]
      else:
         basename = sheetname
         groupname = ''
      if basename != 'networkinterfaces':
         continue

      df = loadframe(pd, sheet, useroptions)

      details = alldetails[basename]
      resourcetype = details['resource']
      filetype = details['file']
      fieldstype = details['fields']
      structurestype = details['structures']
      parenttype = details['parent']
      parentfiletype = details['parentfile']

      columns = df.columns
      for index, row in df.iterrows():
         # Skip rows with no name.
         rowname = row['name']
         empty = novalue(rowname)
         if empty:
            continue
         if rowname != nicname:
            continue
         return row
  
   return None

def getparent(rowname, parentrow, parenttype, details, useroptions):
   prepend = useroptions['prepend']  

   parentname = ''
   if parenttype.find(':') == -1:
      columnname = parenttype
      parentname = parentrow[columnname]
      empty = novalue(parentname)
      if not empty:
         if doprepend(details):
            parentname = prepend + parentname
   else:
      parentarray = parenttype.split(':')
      parentcolumn = parentarray[0]
      sheettype = parentarray[1]
      columnname = parentarray[2]

      if isrequired(details):
         required = True
      else:
         required = False

      if isgen2required(details):
         gen2required = True
      else:
         gen2required = False

      parentname = parentrow[parentcolumn]
      empty = novalue(parentcolumn)
      if required and empty:
        print(missingvaluemessage % (parentcolumn, rowname))
        return ''

      parentvalue = parentrow[parentcolumn]

      sheets = loadfile(useroptions)
      for name, sheet in sheets.items():
         name = name.replace(' ', '')
         pos = name.find('-')
         if pos >= 0:
            type = name[0:pos] 
            group = name[pos+1]
         else:
            type = name
            group = ''
         if type != sheettype:
            continue

         df = loadframe(pd, sheet, useroptions)

         details = alldetails[type]
         resourcetype = details['resource']
         filetype = details['file']
         fieldstype = details['fields']
         structurestype = details['structures']
         parenttype = details['parent']
         parentfiletype = details['parentfile']

         columns = df.columns
         for index, row in df.iterrows():
            # Skip rows with no name.
            name = row['name']
            empty = novalue(name)
            if empty:
               continue
            if name != parentvalue:
               continue
            subnet = row[columnname]
            parentname = subnet
            details = getdetails('name',fieldstype)
            if doprepend(details):
               parentname = prepend + parentname
   return parentname

def getreference(field, element, fieldstype, prepend, generation):
   details = getdetails(field,fieldstype)
   # @revisit timeout and protocol
   if isvalue(details) or istimeout(details) or isprotocol(details) or isprotocolvalue(details):
      reference = element
      if doprepend(details):
         reference = prepend + element
      else:
         reference = element
   elif nogen(details):
      reference = 'nogen'
   elif isfile(details):
      reference = 'file("' + element + '")'
   elif isimage(details):
      element = element.replace(" ", "")
      if generation == '2':
         if element in gen2imagedictionary.keys():
            reference = gen2imagedictionary[element]
         else:
            print(missingimagemessage % element)
            reference = element
      else:
         if element in gen1imagedictionary.keys():
            reference = gen1imagedictionary[element]
         else:
            print(missingimagemessage % element)
            reference = element
   elif isregion(details):
      element = element.replace(" ", "")
      if generation == '2':
         if element in gen2regionsdictionary.keys():
            reference = gen2regionsdictionary[element]
         else:
            print(missingregionmessage % element)
            reference = element
      else:
         if element in gen1regionsdictionary.keys():
            reference = gen1regionsdictionary[element]
         else:
            print(missingregionmessage % element)
            reference = element
   elif iszone(details):
      element = element.replace(" ", "")
      if generation == '2':
         if element in gen2zonesdictionary.keys():
            reference = gen2zonesdictionary[element]
         else:
            print(missingzonemessage % element)
            reference = element
      else:
         if element in gen1zonesdictionary.keys():
            reference = gen1zonesdictionary[element]
         else:
            print(missingzonemessage % element)
            reference = element
   elif isimageprofile(details):
      element = element.replace(" ", "")
      if generation == '2':
         if element in gen2imageprofilesdictionary.keys():
            reference = gen2imageprofilesdictionary[element]
         else:
            print(missingimageprofilemessage % element)
            reference = element
      else:
         if element in gen1imageprofilesdictionary.keys():
            reference = gen1imageprofilesdictionary[element]
         else:
            print(missingimageprofilemessage % element)
            reference = element
   elif isvolumeprofile(details):
      element = element.replace(" ", "")
      if generation == '2':
         if element in gen2volumeprofilesdictionary.keys():
            reference = gen2volumeprofilesdictionary[element]
         else:
            print(missingvolumeprofilemessage % element)
            reference = element
      else:
         if element in gen1volumeprofilesdictionary.keys():
            reference = gen1volumeprofilesdictionary[element]
         else:
            print(missingvolumeprofilemessage % element)
            reference = element
   elif isprimarynic(details):
       reference = element
   elif isnetworkinterfaces(details):
       reference = element

   else:  
      if field == 'public_gateway':
         values = element.split(':')
         count = len(values)
         if count == 2:
            element = values[0]
      elif field == 'protocol':
          return element
      elif 'network_acl' in field and generation == '2':
         return '$network_acl'
      if doprepend(details):
         element = prepend + element
      resource = getresource(details)
      action = getaction(details) 
      reference = resource + '.' + element + '.' + action
   return reference

def getvalue(field, column, row, fieldstype, prepend, generation):
   details = getdetails(field, fieldstype)
   if isint(details):
      cell = row[field]
      return cell
   cell = str(row[field])
   cell = cell.strip()
   cell = cell.replace(" ", "")
   if isvariable(cell):
      return cell
   if isarray(details):
      list = cell.split(',')
      value = ''
      for element in list:
         delimiter = '' if value == '' else ','
         reference = getreference(field, element, fieldstype, prepend, generation)
         if reference != '':
            if isresource(details): 
               value = value + delimiter + reference
            else:
               value = value + delimiter + '"' + reference + '"'
         else:
            value = value + delimiter + '"' + element + '"'
      value = '[' + value + ']'
   else:
      reference = getreference(field, cell, fieldstype, prepend, generation)
      # @revisit when acls are in Gen2.
      if reference == '$network_acl': 
         return ''
      if nogen(details):
        return ''
      value = reference if reference != '' else cell
   return value

def primarynic(varstf, tf, nicname, details, useroptions):
   datavars = useroptions['datavars']
   prepend = useroptions['prepend']

   row = getnic(nicname, details, useroptions)

   if row.empty:
      print(invalidnicmessage % nicname)
      return 

   # @revisit check doprepend.
   nicname = prepend + nicname

   subnetname = row['subnet']
   subnetname = prepend + subnetname 

   sglist = ''
   fipname = ''
  
   sglist = row['security_groups']
   empty = novalue(sglist)

   # FIP is already handled.
   fipname = row['floating_ip']
   empty = novalue(fipname)
   if not empty:
      fipname = prepend + fipname

   tf.write(primarynicstructure + ' {\n')
   if isvariable(nicname):
      tf.write('name = ' + nicname + '\n')
   elif datavars:
      varstf.write(varsyntax % (nicname, 'name', nicname))
      tf.write('name = ' + (refsyntax % (nicname, 'name')) + '\n')
   else:
      tf.write('name = "' + nicname + '"\n')
   tf.write('subnet = ' + subnetresource + '.' + subnetname + '.id' + '\n')

   if sglist != '':
      sgarray = sglist.split(',')
      resource = 'ibm_is_security_group'
      action = 'id'

      tf.write('security_groups = [\n')

      sgcount = 0

      for sgname in sgarray: 
         if sgcount > 0:
            # @revisit to remove unnecessary trailing comma.
            tf.write(',\n') 
         sgcount = sgcount + 1
         sgname = prepend + sgname
         tf.write(resource + '.' + sgname + '.' + action)
      tf.write(']\n')

   tf.write('}\n')
      
   return

def networkinterfaces(tf, niclist, details, useroptions):
   prepend = useroptions['prepend']

   nicarray = niclist.split(',')

   for nicname in nicarray: 
      row = getnic(nicname, details, useroptions)

      if row.empty:
         print(invalidnicmessage % nicname)
         return 

      # @revisit check doprepend.
      nicname = prepend + nicname

      subnetname = row['subnet']
      subnetname = prepend + subnetname 

      sglist = ''
      fipname = ''
  
      sglist = row['security_groups']
      empty = novalue(sglist)

      # FIP is already handled.
      fipname = row['floating_ip']
      empty = novalue(fipname)
      if not empty:
         fipname = prepend + fipname

      tf.write(networkinterfacesstructure + ' {\n')
      tf.write('name = "' + nicname + '"\n')
      tf.write('subnet = ' + subnetresource + '.' + subnetname + '.id' + '\n')

      if sglist != '':
         sgarray = sglist.split(',')
         resource = 'ibm_is_security_group'
         action = 'id'

         tf.write('security_groups = [\n')

         sgcount = 0

         for sgname in sgarray: 
            if sgcount > 0:
               # @revisit to remove unnecessary trailing comma.
               tf.write(',\n') 
            sgcount = sgcount + 1
            sgname = prepend + sgname
            tf.write(resource + '.' + sgname + '.' + action)
         tf.write(']\n')

      tf.write('}\n')

   return

def ruleprotocol(tf, value, acl, fieldstype):
   if value == 'icmp':
      tf.write('icmp {\n')
   elif value == 'tcp':
      tf.write('tcp {\n')
   elif value == 'udp':
      tf.write('udp {\n')
   return
