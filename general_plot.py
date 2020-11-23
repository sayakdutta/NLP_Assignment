# -*- coding: utf-8 -*-
"""
Created on Fri Nov  6 19:42:57 2020

@author: sayakdibyo
"""

import numpy as np
import matplotlib.pyplot as plt
from os import listdir, chdir

chdir('C:\\Users\\sayakdibyo\\Desktop\\nlp_assignment\\NewMonths')
names = [d for d in listdir(".") if "." not in d]

arr1=[]
arr2=[]
arr3=[]
arr4=[]

for name in sorted(names):
	#print(name+'\n')
	chdir('C:\\Users\\sayakdibyo\\Desktop\\nlp_assignment\\NewMonths\\%s' %name)
	f=open('info.txt','r')
	arr1.append(float(f.readline()))
	arr2.append(float(f.readline()))
	arr3.append(float(f.readline()))
	arr4.append(float(f.readline()))
	f.close()

chdir('C:\\Users\\sayakdibyo\\Desktop\\nlp_assignment')

l1=[]
l2=[]
l3=[]
l4=[]
for i in range(5):
        for j in range(12):
            l1.append(arr1[i+j*5])
            l2.append(arr2[i+j*5])
            l3.append(arr3[i+j*5])
            l4.append(arr4[i+j*5])
            
arr1=np.array(l1)
arr2=np.array(l2)
arr3=np.array(l3)
arr4=np.array(l4)

plt.plot(arr1)
plt.title('Noise-1')
plt.savefig('fig1.png',bbox_inches='tight')
plt.gcf().clear()

plt.plot(arr2)
plt.title('"meeting" versus time')
plt.xlabel('time(in months)')
plt.ylabel('frequency')
plt.savefig('fig2.png',bbox_inches='tight')
plt.gcf().clear()
	
plt.plot(arr3,color='red')
plt.title('"business" versus time')
plt.xlabel('time(in months)')
plt.ylabel('frequency')
plt.savefig('fig3.png',bbox_inches='tight')
plt.gcf().clear()
	
plt.plot(arr4)
plt.title('Noise-2')
plt.savefig('fig4.png',bbox_inches='tight')
plt.gcf().clear()