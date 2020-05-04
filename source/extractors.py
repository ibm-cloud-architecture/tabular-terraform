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

from structures import *
from messages import *
from helpers import *

# Extraction functions

def extractvpctable(sheet, df):
   vpctable = df.filter(items=['name', 'default_network_acl', 'classic_access', 'resource_group', 'tags'])
   return vpctable

def extractprefixtable(sheet, df):
   prefixtable = df.filter(items=['prefix_name', 'name', 'zone', 'cidr'])
   prefixtable.rename(columns=lambda x: 'vpc' if 'name' == x else x, inplace=True)
   prefixtable.rename(columns=lambda x: 'name' if 'prefix_name' == x else x, inplace=True)
   return prefixtable

def extractvolumetable(sheet, df):
   df.drop(df[df.attachment_type == 'boot'].index, inplace=True)  
   return df

def extractvpngatewaytable(sheet, df):
   vpngatewaytable = df.filter(items=['gateway_name', 'subnet', 'resource_group'])
   vpngatewaytable.rename(columns=lambda x: 'name' if x=='gateway_name' else x, inplace=True)
   return vpngatewaytable

def extractvpnconnectiontable(sheet, df):
   vpnconnectiontable = df.filter(items=['name', 'peer_address', 'preshared_key', 'local_cidrs', 'peer_cidrs', 'admin_state_up', 'dead_peer_action', 'dead_peer_interval', 'dead_peer_timeout', 'ike_policy', 'ipsec_policy', 'timeouts', 'gateway_name', 'subnet'])
   return vpnconnectiontable

def extractaclruletable(sheet, df):
   aclruletable = df.filter(items=['name', 'action', 'source', 'destination', 'direction', 'protocol', 'acl_name'])
   return aclruletable

def extractsgruletable(sheet, df):
   df.rename(columns=lambda x: x[1:] if x[0]=='*' else x, inplace=True)
   sgruletable = df.filter(items=['name', 'direction', 'remote', 'ip_version', 'protocol', 'group_name'])
   return sgruletable

def extractsubnetgatewaytable(sheet, df):
   gatewaylist = []
   columns = df.columns
   for index, row in df.iterrows():
      # Skip rows with no name - values in other columns are used for arrays.
      name = row['name']
      empty = novalue(name)
      if empty:
         continue
      
      # After first table skip header rows (*name, *sg_name, etc)

      header = name
      header = header[1:] if header[0] == '*' else header
      headerpos = header.rfind(':')
      header = header[headerpos+1:] if headerpos != -1 else header
      if header == 'name':
         continue

      gateway = row['public_gateway']
      empty = novalue(gateway)
      if empty:
         continue

      values = gateway.split(':')
      count = len(values)
      if count == 1 or count == 2:
         gatewayname = values[0]
         if count == 2:
            fipname = values[1]
         else:
            fipname = np.nan
      else:
         print(invalidgatewayspecmessage % gateway)
         return None

      subnetname = name

      vpcname = row['vpc']
      empty = novalue(vpcname)
      if empty:
         vpcname = None

      zone = row['zone']
      empty = novalue(zone)
      if empty:
         zone = None

      gatewaylist.append([gatewayname, vpcname, subnetname, zone, fipname])

   if gatewaylist != []:
      sheet = pd.DataFrame(gatewaylist, columns = ['name', 'vpc', 'subnet', 'zone', 'floating_ip_id'])
   else:
      sheet = pd.DataFrame()

   return sheet

def extractsubnetfiptable(sheet, df):
   fiplist = []
   columns = df.columns
   for index, row in df.iterrows():
      # Skip rows with no name.
      name = row['name']
      empty = novalue(name)
      if empty:
         continue

      # Skip rows with no public_gateway.
      gateway = row['public_gateway']
      empty = novalue(gateway)
      if empty:
         continue

      values = gateway.split(':')
      count = len(values)
      if count == 1:
         continue
      elif count == 2:
         fipname = values[1]
      else:
         print(invalidgatewayspecmessage % gateway)
         return pd.DataFrame()

      zone = row['zone']
      empty = novalue(zone)
      if empty:
         zone = None

      fiplist.append([fipname, name, zone])

   if fiplist != []:
      sheet = pd.DataFrame(fiplist, columns = ['name', 'subnet', 'zone'])
   else:
      sheet = pd.DataFrame()

   return sheet

def extractinstancefiptable(sheet, df):
   fiplist = []
   columns = df.columns
   for index, row in df.iterrows():
      # Skip rows with no name - values in other columns are used for arrays.
      name = row['name']
      empty = novalue(name)
      if empty:
         continue

      # @revisit making instance column mandatory or go thru instances to networkinterfaces to get fip so the instance name is already known.
      instance = row['instance']
      empty = novalue(instance)
      if empty:
         continue

      fipname = row['floating_ip']
      empty = novalue(fipname)
      if empty:
         continue

      subnetname = row['subnet']
      empty = novalue(subnetname)
      if empty:
         # @revisit error since subnet is required.
         subnetname = None

      sgnames = row['security_groups']
      empty = novalue(sgnames)
      if empty:
         sgnames = None

      fiplist.append([fipname, subnetname, instance])

   if fiplist != []:
      sheet = pd.DataFrame(fiplist, columns = ['name', 'subnet', 'target'])
   else:
      sheet = pd.DataFrame()

   return sheet
