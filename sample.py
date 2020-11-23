# -*- coding: utf-8 -*-
"""
Created on Mon Oct 19 11:11:56 2020

@author: sayakdibyo
"""

import shutil
import random
import os

address = 'C:\\Users\\sayakdibyo\\Desktop\\nlp_assignment\\data'
new_address = 'C:\\Users\\sayakdibyo\\Desktop\\nlp_assignment\\red_data'

filenames = random.sample(os.listdir(address), 30000)
for fname in filenames:
    srcpath = os.path.join(address, fname)
    destpath =  os.path.join(new_address,fname)
    shutil.copyfile(srcpath, destpath)