# @file gentf.py
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

import os
import sys
#import argparse
#import json
#import yaml
import shutil
import numpy as np
import pandas as pd

from util import *
from load import *

# Generate functions

def genproviders(userdata, name, sheet, df):
   outputdirectory = userdata['outputdirectory']

   print(processingsheetmessage % name)

   name = name.replace(' ', '')
   pos = name.find('-')
   if pos >= 0:
      sheettype = name[0:pos]
      sheetgroup = name[pos+1:]
   else:
      sheettype = name
      sheetgroup = ''

   columns = df.columns

   # Loop thru rows.
   for rowindex, row in df.iterrows():
      tfname = row['file']
      # Skip empty rows.
      empty = novalue(tfname)
      if empty:
         continue
      else:
         tfname = tfname.replace(' ', '')

      #resource = row['resource']
      #empty = novalue(resource)
      #if empty:
      #   print(missingvaluemessage % ('resource', rowindex))
      #   continue

      module = row['module']
      empty = novalue(module)
      if empty:
         module = '.'
      else:
         module = module.replace(' ', '')
 
      tfname = os.path.join(module, tfname)

      comments = row['comments']
      empty = novalue(comments)
      if not empty:
        printline(userdata, tfname, '# ' + comments)

      #printline(userdata, tfname, providerheader % name)
      printline(userdata, tfname, providerheader % 'ibm')

      savegroup = None

      # Loop through columns skipping first column (file) and last 2 columns (modules and comments).
      for columnindex in range(columns.size-2):
         if columnindex < 1:
            continue

         column = columns[columnindex]
         value = row[column]
         empty = novalue(value)
         if empty:
            continue

         if isinstance(value, int):
            value = str(value)

         column = column.replace(' ', '')

         dotpos = column.find('.')
         if dotpos >= 0:
            subgroup = column[0:dotpos]
            subcolumn = column[dotpos+1:]
            column = subcolumn
            if savegroup == None:
               # No group yet so start group.
               savegroup = subgroup
               # Remove trailing digits from duplicated columns of arrays.
               subgroup = subgroup.rstrip('0123456789')
               printline(userdata, tfname, subgroup + ' {')
            elif savegroup != subgroup:
               # Adjacent groups so close previous group and start next group.
               savegroup = subgroup
               # Remove trailing digits from duplicated columns of arrays.
               subgroup = subgroup.rstrip('0123456789')
               printline(userdata, tfname, '}')
               printline(userdata, tfname, subgroup + ' {')
         elif savegroup != None:
            # End of group so close group.
            savegroup = None
            printline(userdata, tfname, '}')

         if column != 'name':
            printline(userdata, tfname, column + ' = ' + value)

      if savegroup != None:
         # End of row so close group.
         savegroup = None
         printline(userdata, tfname, '}')

      printline(userdata, tfname, endprovider)

   return

def genversions(userdata, name, sheet, df):

   #printline(userdata, tfname, 'terraform {')
   #printline(userdata, tfname, 'required_version = ">= ' + terraformversion + '"')
   #printline(userdata, tfname, 'required_providers {')
   #printline(userdata, tfname, 'ibm = {')
   #printline(userdata, tfname, 'source = "ibm-cloud/ibm"')
   #printline(userdata, tfname, 'version = "' + providerversion + '"')
   #printline(userdata, tfname, '}')
   #printline(userdata, tfname, '}')
   #printline(userdata, tfname, '}')

   outputdirectory = userdata['outputdirectory']

   print(processingsheetmessage % name)

   name = name.replace(' ', '')
   pos = name.find('-')
   if pos >= 0:
      sheettype = name[0:pos]
      sheetgroup = name[pos+1:]
   else:
      sheettype = name
      sheetgroup = ''

   columns = df.columns

   # Loop thru rows.
   for rowindex, row in df.iterrows():
      tfname = row['file']
      # Skip empty rows.
      empty = novalue(tfname)
      if empty:
         continue
      else:
         tfname = tfname.replace(' ', '')

      #resource = row['resource']
      #empty = novalue(resource)
      #if empty:
      #   print(missingvaluemessage % ('resource', rowindex))
      #   continue

      module = row['module']
      empty = novalue(module)
      if empty:
         module = '.'
      else:
         module = module.replace(' ', '')
 
      tfname = os.path.join(module, tfname)

      comments = row['comments']
      empty = novalue(comments)
      if not empty:
        printline(userdata, tfname, '# ' + comments)

      printline(userdata, tfname, terraformheader)

      savegroup = None

      # Loop through columns skipping first column (file) and last 2 columns (modules and comments).
      for columnindex in range(columns.size-2):
         if columnindex < 1:
            continue

         column = columns[columnindex]
         value = row[column]
         empty = novalue(value)
         if empty:
            continue

         if isinstance(value, int):
            value = str(value)

         column = column.replace(' ', '')

         dotpos = column.rfind('.')
         if dotpos >= 0:
            subgroup = column[0:dotpos]
            subcolumn = column[dotpos+1:]
            column = subcolumn
            if savegroup == None:
               # No group yet so start group.
               savegroup = subgroup
               # Remove trailing digits from duplicated columns of arrays.
               subgroup = subgroup.rstrip('0123456789')
               if subgroup == 'required_providers.ibm':
                  printline(userdata, tfname, 'required_providers {')
                  printline(userdata, tfname, 'ibm = {')
               else:
                  printline(userdata, tfname, subgroup + ' {')
            elif savegroup != subgroup:
               # Adjacent groups so close previous group and start next group.
               savegroup = subgroup
               # Remove trailing digits from duplicated columns of arrays.
               subgroup = subgroup.rstrip('0123456789')
               printline(userdata, tfname, '}')
               if subgroup == 'required_providers.ibm':
                  printline(userdata, tfname, 'required_providers {')
                  printline(userdata, tfname, 'ibm = {')

               else:
                  printline(userdata, tfname, subgroup + ' {')
         elif savegroup != None:
            # End of group so close group.
            savegroup = None
            printline(userdata, tfname, '}')
            if subgroup == 'required_providers.ibm':
               printline(userdata, tfname, '}')

         if column != 'name':
            printline(userdata, tfname, column + ' = ' + value)

      if savegroup != None:
         # End of row so close group.
         savegroup = None
         printline(userdata, tfname, '}')
         if subgroup == 'required_providers.ibm':
            printline(userdata, tfname, '}')

      printline(userdata, tfname, endterraform)

   return

def genoutputs(userdata, name, sheet, df):
   outputdirectory = userdata['outputdirectory']
   
   print(processingsheetmessage % name)

   columns = df.columns

   # Loop thru rows.
   for rowindex, row in df.iterrows():
      tfname = row['file']
      # Skip empty rows.
      empty = novalue(tfname)
      if empty:
         continue
      else:
         tfname = tfname.replace(' ', '')

      name = row['name']
      empty = novalue(name)
      if empty:
         print(missingvaluemessage % ('name', rowindex))
         continue
      
      value = row['value']
      empty = novalue(value)
      if empty:
         print(missingvaluemessage % ('value', rowindex))
         continue

      module = row['module']
      empty = novalue(module)
      if empty:
         module = '.'
      else:
         module = module.replace(' ', '')

      tfname = os.path.join(module, tfname)

      comments = row['comments']
      empty = novalue(comments)
      if not empty:
        printline(userdata, tfname, '# ' + comments)

      printline(userdata, tfname, outputheader % name)
      printline(userdata, tfname, 'value = ' + str(value))
      printline(userdata, tfname, endoutput)

   return

def gencloudinits(userdata, name, sheet, df):
   outputdirectory = userdata['outputdirectory']
   
   print(processingsheetmessage % name)

   columns = df.columns

   # Loop thru rows.
   for rowindex, row in df.iterrows():
      tfname = row['file']
      # Skip empty rows.
      empty = novalue(tfname)
      if empty:
         continue
      else:
         tfname = tfname.replace(' ', '')

      resource = row['resource']
      empty = novalue(resource)
      if empty:
         print(missingvaluemessage % ('resource', rowindex))
         continue
      
      module = row['module']
      empty = novalue(module)
      if empty:
         module = '.'
      else:
         module = module.replace(' ', '')

      inputdirectory = userdata['inputdirectory']
      initspath = os.path.join(inputdirectory, 'cloudinits')
      tfname = os.path.join(initspath, tfname)

      if os.path.isdir(initspath) and os.path.isfile(tfname):
         filepath = os.path.join(outputdirectory, module)
         # Check for existing module directory.
         if not os.path.exists(filepath):
            # Create new module directory.
            os.makedirs(filepath)
         shutil.copy(tfname, filepath)

   return

def genvariables(userdata, name, sheet, df):
   outputdirectory = userdata['outputdirectory']
   
   print(processingsheetmessage % name)

   columns = df.columns

   # Loop thru rows.
   for rowindex, row in df.iterrows():
      tfname = row['file']
      # Skip empty rows.
      empty = novalue(tfname)
      if empty:
         continue
      else:
         tfname = tfname.replace(' ', '')

      name = row['name']
      empty = novalue(name)
      if empty:
         print(missingvaluemessage % ('name', rowindex))
         continue
      
      emptyvalue = False
      value = row['value']
      empty = novalue(value)
      if empty:
         emptyvalue = True
         #print(missingvaluemessage % ('value', rowindex))
         #continue

      module = row['module']
      empty = novalue(module)
      if empty:
         module = '.'
      else:
         module = module.replace(' ', '')

      tfname = os.path.join(module, tfname)

      printline(userdata, tfname, variableheader % name)

      comments = row['comments']
      empty = novalue(comments)
      if not empty:
         #printline(userdata, tfname, '# ' + comments)
         printline(userdata, tfname, 'description = "' + comments + '"')

      if not emptyvalue:
         printline(userdata, tfname, 'default = ' + str(value))

      printline(userdata, tfname, endvariable)

   return

def genmodules(userdata, name, sheet, df):
   outputdirectory = userdata['outputdirectory']
   
   print(processingsheetmessage % name)

   tfname = 'modules.tf'
   module = name.split('-')[1]

   printline(userdata, tfname, moduleheader % module)

   columns = df.columns

   # Loop thru rows.
   for rowindex, row in df.iterrows():
      tfnameignore = row['file']
      # Skip empty rows.
      empty = novalue(tfnameignore)
      if empty:
         continue

      name = row['name']
      empty = novalue(name)
      if empty:
         print(missingvaluemessage % ('name', rowindex))
         continue
      
      emptyvalue = False
      value = row['value']
      empty = novalue(value)
      if empty:
         emptyvalue = True
         #print(missingvaluemessage % ('value', rowindex))
         #continue

      module = row['module']
      empty = novalue(module)
      if empty:
         module = '.'
      else:
         module = module.replace(' ', '')

      #tfname = os.path.join(module, tfname)

      #printline(userdata, tfname, moduleheader % name)

      comments = row['comments']
      empty = novalue(comments)
      if not empty:
         printline(userdata, tfname, '# ' + comments)
         #printline(userdata, tfname, 'description = "' + comments + '"')

      if not emptyvalue:
         #printline(userdata, tfname, 'default = ' + str(value))
         printline(userdata, tfname, name + ' = ' + value)

      #printline(userdata, tfname, endvariable)

   printline(userdata, tfname, endmodule)

   return

def genlocalfiles(userdata, name, sheet, df):
   outputdirectory = userdata['outputdirectory']
   
   print(processingsheetmessage % name)

   name = name.replace(' ', '')
   pos = name.find('-')
   if pos >= 0:
      sheettype = name[0:pos]
      sheetgroup = name[pos+1:]
   else:
      sheettype = name
      sheetgroup = ''

   columns = df.columns

   header = True
   tfname = None

   columns = df.columns

   # Loop thru rows.
   for rowindex, row in df.iterrows():
      if header:
         tfname = row['file']
         # Skip empty rows.
         empty = novalue(tfname)
         if empty:
            continue
         else:
            tfname = tfname.replace(' ', '')

         resource = row['resource']
         empty = novalue(resource)
         if empty:
            print(missingvaluemessage % ('resource', rowindex))
            continue
         else:
            resource = resource.replace(' ', '')

         header = False

         module = row['module']
         empty = novalue(module)
         if empty:
            module = '.'
         else:
            module = module.replace(' ', '')

         tfname = os.path.join(module, tfname)

         comments = row['comments']
         empty = novalue(comments)
         if not empty:
            printline(userdata, tfname, '# ' + comments)

         printline(userdata, tfname, resourceheader % (resources[sheettype], resource))

         filename = row['filename']
         empty = novalue(filename)
         if empty:
            print(missingvaluemessage % ('filename', rowindex))
            continue
         else:
            filename = filename.replace(' ', '')

         printline(userdata, tfname, 'filename = ' + filename)

         content = row['content']
         empty = novalue(content)
         if empty:
            print(missingvaluemessage % ('content', rowindex))
            continue
         #else:
         #   content = content.replace(' ', '')

         printline(userdata, tfname, 'content = <<EOT')

         printline(userdata, tfname, content)

      else:

         tfnameignore = row['file']
         # Skip empty rows.
         empty = novalue(tfnameignore)
         if empty:
            continue

         content = row['content']
         empty = novalue(content)
         if empty:
            print(missingvaluemessage % ('content', rowindex))
            continue
         #else:
         #   content = content.replace(' ', '')

         printline(userdata, tfname, content)

   printline(userdata, tfname, 'EOT')

   printline(userdata, tfname, endmodule)

   return

def genaclresources(userdata, name, sheet, df):
   outputdirectory = userdata['outputdirectory']
   
   print(processingsheetmessage % name)

   name = name.replace(' ', '')
   pos = name.find('-')
   if pos >= 0:
      sheettype = name[0:pos]
      sheetgroup = name[pos+1:]
   else:
      sheettype = name
      sheetgroup = ''

   columns = df.columns

   header = True
   tfname = None

   # Loop thru rows.
   for rowindex, row in df.iterrows():
      if header:
         tfname = row['file']
         # Skip empty rows.
         empty = novalue(tfname)
         if empty:
            continue
         else:
            tfname = tfname.replace(' ', '')

         resource = row['resource']
         empty = novalue(resource)
         if empty:
            print(missingvaluemessage % ('resource', rowindex))
            continue
         else:
            resource = resource.replace(' ', '')

         #resource_data = False
         #resource = resource.replace(' ', '')
         #pos = resource.find('.')
         #if pos >= 0:
         #   if resource[0:pos] == 'data':
         #      resource_data = True
         #      resource = resource[pos+1:]

         header = False

         module = row['module']
         empty = novalue(module)
         if empty:
            module = '.'
         else:
            module = module.replace(' ', '')

         tfname = os.path.join(module, tfname)

         comments = row['comments']
         empty = novalue(comments)
         if not empty:
            printline(userdata, tfname, '# ' + comments)

         #if resource_data == True:
         #   printline(userdata, tfname, dataheader % (resources[sheettype], resource))
         #else:
         printline(userdata, tfname, resourceheader % (resources[sheettype], resource))

         # Loop through columns skipping first 2 columns (file and resource) and last 2 columns (module and comments).
         for columnindex in range(columns.size-2):
            if columnindex < 2:
               continue

            column = columns[columnindex]
            value = row[column]
            empty = novalue(value)
            if empty:
               continue

            if isinstance(value, int):
               value = str(value)

            printline(userdata, tfname, column + ' = ' + value)
      else:
         name = row['name']
         # End of rule group when name is empty.
         empty = novalue(name)
         if empty:
            printline(userdata, tfname, '}')
            header = True
            continue

         printline(userdata, tfname, 'rules {')

         savegroup = None

         # Loop through columns skipping first 2 columns (file and resource) and last 2 columns (module and comments).
         for columnindex in range(columns.size-2):
            if columnindex < 2:
               continue

            column = columns[columnindex]
            value = row[column]
            empty = novalue(value)
            if empty:
               continue

            if isinstance(value, int):
               value = str(value)

            column = column.replace(' ', '')
            dotpos = column.find('.')
            if dotpos >= 0:
               subgroup = column[0:dotpos]
               subcolumn = column[dotpos+1:]
               column = subcolumn
               if savegroup == None:
                  # No group yet so start group.
                  savegroup = subgroup
                  # Remove trailing digits from duplicated columns of arrays.
                  subgroup = subgroup.rstrip('0123456789')
                  printline(userdata, tfname, subgroup + ' {')
               elif savegroup != subgroup:
                  # Adjacent groups so close previous group and start next group.
                  savegroup = subgroup
                  # Remove trailing digits from duplicated columns of arrays.
                  subgroup = subgroup.rstrip('0123456789')
                  printline(userdata, tfname, '}')
                  printline(userdata, tfname, subgroup + ' {')
            elif savegroup != None:
               # End of group so close group.
               savegroup = None
               printline(userdata, tfname, '}')

            printline(userdata, tfname, column + ' = ' + value)

         if savegroup != None:
            # End of row so close group.
            savegroup = None
            printline(userdata, tfname, '}')

         printline(userdata, tfname, '}')

   if tfname != None:
      printline(userdata, tfname, endresource)

   return

def genresources(userdata, name, sheet, df):
   outputdirectory = userdata['outputdirectory']
   
   print(processingsheetmessage % name)

   name = name.replace(' ', '')
   pos = name.find('-')
   if pos >= 0:
      sheettype = name[0:pos]
      sheetgroup = name[pos+1:]
   else:
      sheettype = name
      sheetgroup = ''

   columns = df.columns

   # Loop thru rows.
   for rowindex, row in df.iterrows():
      tfname = row['file']
      # Skip empty rows.
      empty = novalue(tfname)
      if empty:
         continue
      else:
         tfname = tfname.replace(' ', '')

      resource = row['resource']
      empty = novalue(resource)
      if empty:
         print(missingvaluemessage % ('resource', rowindex))
         continue
      else:
         resource = resource.replace(' ', '')

      resource_data = False
      resource = resource.replace(' ', '')
      pos = resource.find('.')
      if pos >= 0:
         if resource[0:pos] == 'data':
            resource_data = True
            resource = resource[pos+1:]

      module = row['module']
      empty = novalue(module)
      if empty:
         module = '.'
      else:
         module = module.replace(' ', '')
 
      tfname = os.path.join(module, tfname)

      comments = row['comments']
      empty = novalue(comments)
      if not empty:
         printline(userdata, tfname, '# ' + comments)

      if resource_data == True:
         printline(userdata, tfname, dataheader % (resources[sheettype], resource))
         value = row['name']
         empty = novalue(value)
         if empty:
            print(missingvaluemessage % ('resource', rowindex))
            continue
         printline(userdata, tfname, 'name = ' + value)
         printline(userdata, tfname, enddata)
         continue

      printline(userdata, tfname, resourceheader % (resources[sheettype], resource))

      savegroup = None

      # Loop through columns skipping first 2 columns (file and resource) and last 2 columns (module and comments).
      for columnindex in range(columns.size-2):
         if columnindex < 2:
            continue

         column = columns[columnindex]
         value = row[column]
         empty = novalue(value)
         if empty:
            continue

         if isinstance(value, int):
            value = str(value)

         column = column.replace(' ', '')

         dotpos = column.find('.')
         if dotpos >= 0:
            subgroup = column[0:dotpos]
            subcolumn = column[dotpos+1:]
            column = subcolumn
            if savegroup == None:
               # No group yet so start group.
               savegroup = subgroup
               # Remove trailing digits from duplicated columns of arrays.
               subgroup = subgroup.rstrip('0123456789')
               printline(userdata, tfname, subgroup + ' {')
            elif savegroup != subgroup:
               # Adjacent groups so close previous group and start next group.
               savegroup = subgroup
               # Remove trailing digits from duplicated columns of arrays.
               subgroup = subgroup.rstrip('0123456789')
               printline(userdata, tfname, '}')
               printline(userdata, tfname, subgroup + ' {')
         elif savegroup != None:
            # End of group so close group.
            savegroup = None
            printline(userdata, tfname, '}')

         printline(userdata, tfname, column + ' = ' + value)

      if savegroup != None:
         # End of row so close group.
         savegroup = None
         printline(userdata, tfname, '}')

      printline(userdata, tfname, endresource)

   return

def gentf(userdata):
   outputdirectory = userdata['outputdirectory']
   propfile = userdata['propfile']
   propname = userdata['propname']

   #print(starttfmessage % propfile)

   sheets = loadfile(userdata)
   for name, sheet in sheets.items():
      name = name.replace(' ', '')

      df = loadframe(userdata, pd, sheet)

      if name.find('variables', 0, 9) >= 0:
         genvariables(userdata, name, sheet, df)
      elif name.find('outputs', 0, 7) >= 0:
         genoutputs(userdata, name, sheet, df)
      elif name.find('cloudinits', 0, 10) >= 0:
         gencloudinits(userdata, name, sheet, df)
      elif name.find('modules', 0, 7) >= 0:
         genmodules(userdata, name, sheet, df)
      elif name.find('providers', 0, 9) >= 0:
         genproviders(userdata, name, sheet, df)
      elif name.find('versions', 0, 8) >= 0:
         genversions(userdata, name, sheet, df)
      elif name.find('aclrules', 0, 8) >= 0:
         genaclresources(userdata, name, sheet, df)
      elif name.find('localfiles', 0, 10) >= 0:
         genlocalfiles(userdata, name, sheet, df)
      else:
         genresources(userdata, name, sheet, df)

   #print(donetfmessage % (propname, outputdirectory))

   return

def genall(userdata):
   genbackup = None
   outputdirectory = userdata['outputdirectory']
   # Check for existing output directory and backup if exists.
   if os.path.exists(outputdirectory):
      backup = 1
      found = False
      genbackup = None
      # Find a new backup directory.
      while not found:
         genbackup = outputdirectory + '.backup' + str(backup)
         if os.path.exists(genbackup):
            backup += 1
         else:
            found = True
      # Move existing output directory to backup directory.
      shutil.move(outputdirectory, genbackup)
      print(backupdirectorymessage % (outputdirectory, genbackup))

   # Create new empty output directory.
   os.makedirs(outputdirectory)

   # Copy existing terraform.tfstate to output directory.
   if genbackup != None and os.path.isfile(os.path.join(genbackup, 'terraform.tfstate')):
      shutil.copy(os.path.join(genbackup, 'terraform.tfstate'), os.path.join(outputdirectory, 'terraform.tfstate'))

   # Copy existing .terraform to output directory.
   if genbackup != None and os.path.isdir(os.path.join(genbackup, '.terraform')):
      shutil.copytree(os.path.join(genbackup, '.terraform'), os.path.join(outputdirectory, '.terraform'))

   inputdirectory = userdata['inputdirectory']
   inputtype = userdata['inputtype']
   #filelist = os.listdir(os.path.join(inputdirectory, datatype))
   filelist = os.listdir(inputdirectory)

   # Copy terraform-cloudinits if exists to output directory.
   #if os.path.isdir(os.path.join(inputdirectory, 'terraform-cloudinits')):
   #   terraformfiles = os.listdir(os.path.join(inputdirectory, 'terraform-cloudinits'))
   #   for terraformfile in terraformfiles:
   #      shutil.copy(os.path.join(inputdirectory, 'terraform-cloudinits', terraformfile), outputdirectory)

   # Copy ansible if exists to output directory.
   if os.path.isdir(os.path.join(inputdirectory, 'playbooks')):
      shutil.copytree(os.path.join(inputdirectory, 'playbooks'), os.path.join(outputdirectory, 'playbooks'))

   # Generate provider.
   #print(startprovidermessage)
   #genprovider(userdata)

   # Generate versions.
   #print(startversionsmessage)
   #genversions(userdata)

   # Process all files in specified directory.
   found = False
   for afile in filelist:
      if (not afile.endswith(inputtype)):
         continue
      #propfile = os.path.join(inputdirectory, datatype, afile)
      propfile = os.path.join(inputdirectory, afile)
      propfilenopath = os.path.basename(propfile)
      propname = os.path.splitext(propfilenopath)[0]
      propext = os.path.splitext(propfilenopath)[1][1:]
      if (os.path.isfile(propfile)):
         found = True
         userdata['propfile'] = propfile
         userdata['propname'] = propname
         userdata['propext'] = propext
         gentf(userdata)
   if (not found):
      print(missinginputmessage % inputdirectory)

   return
