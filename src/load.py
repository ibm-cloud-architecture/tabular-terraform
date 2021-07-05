# @file load.py
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
#import shutil
import numpy as np
import pandas as pd

from util import *

def loadfile(userdata):
   propext = userdata['propext']
   propfile = userdata['propfile']

   if (propext.lower() == 'xls' or propext.lower() == 'xlsx'):
      sheets = pd.read_excel(propfile, sheet_name=None, dtype=object, header=0)
   else:
      print(invalidinputfilemessage % propfile)
      sheets = None

   return sheets

def loadframe(userdata, pd, sheet):
   propext = userdata['propext']
   propfile = userdata['propfile']

   df = pd.DataFrame(sheet)

   if (propext.lower() == 'xls' or propext.lower() == 'xlsx'):
      # Remove leading asterisk from column names
      df.rename(columns=lambda x: x[1:] if x[0]=='*' else x, inplace=True)
   else:
      print(invalidinputfilemessage % propfile)
      sheets = None

   return df
