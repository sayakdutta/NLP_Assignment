# -*- coding: utf-8 -*-
"""
Created on Mon Oct 19 11:46:46 2020

@author: sayakdibyo
"""

from os import listdir, chdir
import re
import os


chdir("C:\\Users\\sayakdibyo\\Desktop\\maildir")
names = [d for d in listdir(".") if "." not in d]
chdir("C:\\Users\\sayakdibyo\\Desktop\\nlp_assignment\\NewUsers")
for name in names:
	os.makedirs('C:\\Users\\sayakdibyo\\Desktop\\nlp_assignment\\NewUsers\\%s' % name)
	for i in range(1,13):
	    path=('C:\\Users\\sayakdibyo\\Desktop\\nlp_assignment\\NewUsers\\%s\\%s_1998' % (name,i) )
	    os.makedirs(path)

	for i in range(1,13):
	    path=('C:\\Users\\sayakdibyo\\Desktop\\nlp_assignment\\NewUsers\\%s\\%s_1999' % (name,i) )
	    os.makedirs(path)

	for i in range(1,13):
	    path=('C:\\Users\\sayakdibyo\\Desktop\\nlp_assignment\\NewUsers\\%s\\%s_2000' % (name,i) )
	    os.makedirs(path)

	for i in range(1,13):
	    path=('C:\\Users\\sayakdibyo\\Desktop\\nlp_assignment\\NewUsers\\%s\\%s_2001' % (name,i) )
	    os.makedirs(path)

	for i in range(1,13):
	    path=('C:\\Users\\sayakdibyo\\Desktop\\nlp_assignment\\NewUsers\\%s\\%s_2002' % (name,i) )
	    os.makedirs(path)