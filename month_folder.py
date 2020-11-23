# -*- coding: utf-8 -*-
"""
Created on Mon Oct 19 13:00:41 2020

@author: sayakdibyo
"""

from os import listdir, chdir
import re
import os

chdir("C:\\Users\\sayakdibyo\\Desktop\\nlp_assignment\\NewMonths")

for i in range(1,13):
	path=('C:\\Users\\sayakdibyo\\Desktop\\nlp_assignment\\NewMonths\\%s_1998' % i )
	os.makedirs(path)

for i in range(1,13):
	path=('C:\\Users\\sayakdibyo\\Desktop\\nlp_assignment\\NewMonths\\%s_1999' % i )
	os.makedirs(path)

for i in range(1,13):
	path=('C:\\Users\\sayakdibyo\\Desktop\\nlp_assignment\\NewMonths\\%s_2000' % i )
	os.makedirs(path)

for i in range(1,13):
	path=('C:\\Users\\sayakdibyo\\Desktop\\nlp_assignment\\NewMonths\\%s_2001' % i )
	os.makedirs(path)

for i in range(1,13):
	path=('C:\\Users\\sayakdibyo\\Desktop\\nlp_assignment\\NewMonths\\%s_2002' % i )
	os.makedirs(path)