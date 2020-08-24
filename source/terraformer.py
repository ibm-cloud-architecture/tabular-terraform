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
import shutil
import numpy as np
import pandas as pd

# Constants

# Following static string is included in binary - update version here.
COPYRIGHT = 'Terraformer 1.11.0.0 - Copyright IBM Corporation 2020'

genheader = '# Terraformer generated file'

terraformheader = 'terraform { required_version = ">= 0.12.0" }'

outputheader = 'output "%s" {'
providerheader = 'provider "%s" {'
resourceheader = 'resource "%s" "%s" {'
variableheader = 'variable "%s" {'

endoutput = '}'
endprovider = '}'
endresource = '}'
endvariable = '}'

# Messages

terraformermessage = 'Terraformer for IBM Virtual Private Cloud\n'
starttfmessage = 'Generating Resources with input from %s\n'
startprovidermessage = 'Generating Resource for provider\n'
donetfmessage = '\nCompleted Resources for %s with output to folder %s\n'
backupdirectorymessage = 'Backed up existing output directory %s to %s\n'
invalidinputdirectorymessage = '(Error) Invalid input directory: %s'
invalidinputfilemessage = '(Error) Invalid input file: %s'
invalidprotocolmessage = '(Error) Invalid protocol: %s'
invalidgatewayspecmessage = '(Error) Invalid gateway specification: %s'
invalidnicmessage = '(Error) Invalid nic: %s'
invalidsecondarynicmessage = '(Error) Invalid secondary nic: %s'
missinginputmessage = '(Error) No input files found: %s'
missingimagemessage = '(Error) Image %s not found'
missingregionmessage = '(Error) Region %s not found'
missingzonemessage = '(Error) Zone %s not found'
missingsubnetmessage = '(Error) Subnet for %s not found'
missingimageprofilemessage = '(Error) Image profile %s not found'
missingvolumeprofilemessage = '(Error) Volume profile %s not found'
missingvaluemessage = '(Error) Required value missing on column %s, row %s'
processingsheetmessage = 'Processing %s'

# User options

options = {
'generation': '2',
'datapath': 'data',
'datatype': 'xlsx',
'genpath': 'resources',
'propext': 'xlsx',
'propfile': '',
'propname': '*',
'region': 'us-south'
}

# Resource names

resources = {
'resourcegroups': 'ibm_resource_group',
'vpcs': 'ibm_is_vpc',
'vpcaddresses': 'ibm_is_vpc_address_prefix',
'vpcroutes': 'ibm_is_vpc_route',
'subnets': 'ibm_is_subnet',
'instances': 'ibm_is_instance',
'networkinterfaces': 'ibm_is_instance_nic',
'volumes': 'ibm_is_volume',
'floatingips': 'ibm_is_floating_ip',
'publicgateways': 'ibm_is_public_gateway',
'vpngateways': 'ibm_is_vpn_gateway',
'vpnconnections': 'ibm_is_vpn_gateway_connection',
'ikepolicies': 'ibm_is_ike_policy',
'ipsecpolicies': 'ibm_is_ipsec_policy',
'images': 'ibm_is_image',
'sshkeys': 'ibm_is_ssh_key',
'loadbalancers': 'ibm_is_lb',
'lbpools': 'ibm_is_lb_pool',
'lbmembers': 'ibm_is_lb_pool_member',
'lblisteners': 'ibm_is_lb_listener',
'lbpolicies': 'ibm_is_lb_listener_policy',
'lbrules': 'ibm_is_lb_listener_policy_rule',
'aclheaders': 'ibm_is_network_acl',
'aclrules': 'ibm_is_network_acl',
'sgheaders': 'ibm_is_security_group',
'sgrules': 'ibm_is_security_group_rule',
'sgnics': 'ibm_is_security_group_network_interface_attachment',
'cisinstances': 'ibm_cis',
'cisdomains': 'ibm_cis_domain',
'cishealthchecks': 'ibm_cis_healthcheck',
'cisoriginpools': 'ibm_cis_origin_pool',
'cisglbs': 'ibm_cis_global_load_balancer'
}

# Utility functions

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
   if type(value) == str:
      value = value.replace(' ', '')
      if value == '':
         return True
   if isinstance(value, str):
      value = value.replace(' ', '')
      if value == '':
         return True
      else:
         return False
   else:
      return False

def loadfile(useroptions):
   propext = useroptions['propext']
   propfile = useroptions['propfile']

   if (propext.lower() == 'xls' or propext.lower() == 'xlsx'):
      sheets = pd.read_excel(propfile, sheet_name=None, dtype=object, header=0)
   else:
      print(invalidinputfilemessage % propfile)
      sheets = None

   return sheets

def loadframe(pd, sheet, useroptions):
   propext = useroptions['propext']
   propfile = useroptions['propfile']

   df = pd.DataFrame(sheet)

   if (propext.lower() == 'xls' or propext.lower() == 'xlsx'):
      # Remove leading asterisk from column names
      df.rename(columns=lambda x: x[1:] if x[0]=='*' else x, inplace=True)
   else:
      print(invalidinputfilemessage % propfile)
      sheets = None

   return df

def printline(options, tfname, line):
   genpath = options['genpath']

   pathname = os.path.join(genpath, tfname)

   if not os.path.exists(pathname):
      tf = open(pathname, 'w')
      tf.write(genheader)
      tf.write('\n')
      tf.close()

   tf = open(pathname, 'a')
   tf.write(line)
   tf.write('\n')
   tf.close()

   return

# Generate functions

def genprovider(options):
   generation = options['generation']
   genpath = options['genpath']
   region = options['region']

   tfname = "provider-ibm.tf"

   printline(options, tfname, terraformheader)
   printline(options, tfname, providerheader % "ibm")
   printline(options, tfname, 'region = "' + region + '"')
   printline(options, tfname, 'generation = "' + generation + '"')
   printline(options, tfname, endprovider)

   return

def genoutputs(options, name, sheet, df):
   genpath = options['genpath']
   
   print(processingsheetmessage % name)

   columns = df.columns

   # Loop thru rows.
   for rowindex, row in df.iterrows():
      tfname = row['file']
      # Skip empty rows.
      empty = novalue(tfname)
      if empty:
         continue

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

      comments = row['comments']
      empty = novalue(comments)
      if not empty:
        printline(options, tfname, '# ' + comments)

      printline(options, tfname, outputheader % name)
      printline(options, tfname, 'value = ' + str(value))
      printline(options, tfname, endoutput)

   return

def genvariables(options, name, sheet, df):
   genpath = options['genpath']
   
   print(processingsheetmessage % name)

   columns = df.columns

   # Loop thru rows.
   for rowindex, row in df.iterrows():
      tfname = row['file']
      # Skip empty rows.
      empty = novalue(tfname)
      if empty:
         continue

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

      comments = row['comments']
      empty = novalue(comments)
      if not empty:
        printline(options, tfname, '# ' + comments)

      printline(options, tfname, variableheader % name)
      printline(options, tfname, 'default = ' + str(value))
      printline(options, tfname, endvariable)

   return

def genaclresources(options, name, sheet, df):
   genpath = options['genpath']
   
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

   # Loop thru rows.
   for rowindex, row in df.iterrows():
      if header:
         tfname = row['file']
         # Skip empty rows.
         empty = novalue(tfname)
         if empty:
            continue

         resource = row['resource']
         empty = novalue(resource)
         if empty:
            print(missingvaluemessage % ('resource', rowindex))
            continue

         header = False

         comments = row['comments']
         empty = novalue(comments)
         if not empty:
           printline(options, tfname, '# ' + comments)

         printline(options, tfname, resourceheader % (resources[sheettype], resource))

         # Loop through columns skipping first 2 columns (file and resource) and last column (comments).
         for columnindex in range(columns.size-1):
            if columnindex < 2:
               continue

            column = columns[columnindex]
            value = row[column]
            empty = novalue(value)
            if empty:
               continue

            if isinstance(value, int):
               value = str(value)

            printline(options, tfname, column + ' = ' + value)
      else:
         name = row['name']
         # End of rule group when name is empty.
         empty = novalue(name)
         if empty:
            printline(options, tfname, '}')
            header = True
            continue

         printline(options, tfname, 'rules {')

         savegroup = None

         for columnindex in range(columns.size):
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
                  printline(options, tfname, subgroup + ' {')
               elif savegroup != subgroup:
                  # Adjacent groups so close previous group and start next group.
                  savegroup = subgroup
                  # Remove trailing digits from duplicated columns of arrays.
                  subgroup = subgroup.rstrip('0123456789')
                  printline(options, tfname, '}')
                  printline(options, tfname, subgroup + ' {')
            elif savegroup != None:
               # End of group so close group.
               savegroup = None
               printline(options, tfname, '}')

            printline(options, tfname, column + ' = ' + value)

         if savegroup != None:
            # End of row so close group.
            savegroup = None
            printline(options, tfname, '}')

         printline(options, tfname, '}')

   printline(options, tfname, endresource)

   return

def genresources(options, name, sheet, df):
   genpath = options['genpath']
   
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

      resource = row['resource']
      empty = novalue(resource)
      if empty:
         print(missingvaluemessage % ('resource', rowindex))
         continue

      comments = row['comments']
      empty = novalue(comments)
      if not empty:
        printline(options, tfname, '# ' + comments)

      printline(options, tfname, resourceheader % (resources[sheettype], resource))

      savegroup = None

      # Loop through columns skipping first 2 columns (file and resource) and last column (comments).
      for columnindex in range(columns.size-1):
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
               printline(options, tfname, subgroup + ' {')
            elif savegroup != subgroup:
               # Adjacent groups so close previous group and start next group.
               savegroup = subgroup
               # Remove trailing digits from duplicated columns of arrays.
               subgroup = subgroup.rstrip('0123456789')
               printline(options, tfname, '}')
               printline(options, tfname, subgroup + ' {')
         elif savegroup != None:
            # End of group so close group.
            savegroup = None
            printline(options, tfname, '}')

         printline(options, tfname, column + ' = ' + value)

      if savegroup != None:
         # End of row so close group.
         savegroup = None
         printline(options, tfname, '}')

      printline(options, tfname, endresource)

   return

def gentf(options):
   genpath = options['genpath']
   propfile = options['propfile']
   propname = options['propname']

   print(starttfmessage % propfile)

   sheets = loadfile(options)
   for name, sheet in sheets.items():
      name = name.replace(' ', '')

      df = loadframe(pd, sheet, options)

      if name.find('variables', 0, 9) >= 0:
         genvariables(options, name, sheet, df)
      elif name.find('outputs', 0, 7) >= 0:
         genoutputs(options, name, sheet, df)
      elif name.find('aclrules', 0, 8) >= 0:
         genaclresources(options, name, sheet, df)
      else:
         genresources(options, name, sheet, df)

   print(donetfmessage % (propname, genpath))

   return

def main():
   print(terraformermessage)

   parser = argparse.ArgumentParser(description='Generates Terraform for IBM Virtual Private Cloud')

   parser.add_argument('inputvalue', nargs='?', default=options['datapath'], help='input folder (default: ' + options['datapath'] + ')')

   parser.add_argument('-o', action='store', dest='outputfolder', default=options['genpath'], help='output folder (default: ' + options['genpath'] + ')')

   parser.add_argument('-r', dest='region', default=options['region'], help='region for VPC (default: ' + options['region'] + ')')

   parser.add_argument('-t', dest='datatype', default=options['datatype'], help='type of input files (default: ' + options['datatype'] + ')')

   parser.add_argument('--version', action='version', version='%(prog)s ' + COPYRIGHT.split(' ')[1])

   results = parser.parse_args()

   options['datapath'] = results.inputvalue
   options['datatype'] = results.datatype
   options['genpath'] = results.outputfolder
   options['region'] = results.region

   datapath = options['datapath']
   datatype = options['datatype']
   genpath = options['genpath']
  
   # Check for existing input directory and exit if not valid.
   if not os.path.isdir(os.path.join(datapath, datatype)):
      print(invalidinputdirectorymessage % os.path.join(datapath, datatype))
      return

   genbackup = None
   # Check for existing output directory and backup if exists.
   if os.path.exists(genpath):
      backup = 1
      found = False
      genbackup = None
      # Find a new backup directory.
      while not found:
         genbackup = genpath + '.backup' + str(backup)
         if os.path.exists(genbackup):
            backup += 1
         else:
            found = True
      # Move existing output directory to backup directory.
      shutil.move(genpath, genbackup)
      print(backupdirectorymessage % (genpath, genbackup))

   # Create new empty output directory.
   os.makedirs(genpath)

   # Copy existing terraform.tfstate to output directory.
   if genbackup != None and os.path.isfile(os.path.join(genbackup, 'terraform.tfstate')):
      shutil.copy(os.path.join(genbackup, 'terraform.tfstate'), os.path.join(genpath, 'terraform.tfstate'))

   datapath = options['datapath']
   datatype = options['datatype']

   # Copy terraform to output directory.
   filelist = os.listdir(os.path.join(datapath, datatype))
   terraformfiles = os.listdir(os.path.join(datapath, 'terraform'))
   for terraformfile in terraformfiles:
      shutil.copy(os.path.join(datapath, 'terraform', terraformfile), genpath)         

   # Copy ansible to output directory.
   shutil.copytree(os.path.join(datapath, 'ansible'), os.path.join(genpath, 'ansible'))         

   # Generate provider.
   print(startprovidermessage)
   genprovider(options)

   # Process all files in specified directory.
   found = False
   for afile in filelist:
      propfile = os.path.join(datapath, datatype, afile)
      propfilenopath = os.path.basename(propfile)
      propname = os.path.splitext(propfilenopath)[0]
      propext = os.path.splitext(propfilenopath)[1][1:]
      if (os.path.isfile(propfile)):
         found = True
         options['propfile'] = propfile
         options['propname'] = propname
         options['propext'] = propext
         gentf(options)
   if (not found):
      print(missinginputmessage % results.inputvalue)

   return
      
main()
