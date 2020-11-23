# -*- coding: utf-8 -*-
"""
Created on Thu Oct 22 19:32:19 2020

@author: sayakdibyo
"""

import numpy as np
import matplotlib.pyplot as plt
from os import listdir, chdir
import sys
chdir('C:\\Users\\sayakdibyo\\Desktop\\nlp_assignment\\NewUsers')
names = [d for d in listdir(".") if "." not in d]


for name in names:
    chdir('C:\\Users\\sayakdibyo\\Desktop\\nlp_assignment\\NewUsers\\%s' % name)
    arr1=[]
    arr2=[]
    arr3=[]
    arr4=[]
    
    newnames=[d for d in listdir(".") if "." not in d]
    for newname in sorted(newnames):
        chdir('C:\\Users\\sayakdibyo\\Desktop\\nlp_assignment\\NewUsers\\%s\\%s' % (name,newname))
        
        f=open('info.txt','r')
        arr1.append(int(f.readline()))
        arr2.append(int(f.readline()))
        arr3.append(int(f.readline()))
        arr4.append(int(f.readline()))
        f.close()
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
    chdir('C:\\Users\\sayakdibyo\\Desktop\\nlp_assignment\\NewUsers\\%s' % name)
    arr1=np.array(l1)
    arr2=np.array(l2)
    arr3=np.array(l3)
    arr4=np.array(l4)

    plt.plot(arr1)
    plt.title('Noise-1')
    plt.savefig('%s_fig1.png' %(name),bbox_inches='tight')
    plt.gcf().clear()

    plt.plot(arr2)
    plt.title('"meeting" versus time')
    plt.xlabel('time(in months)')
    plt.ylabel('frequency')
    plt.savefig('%s_fig2.png' %(name),bbox_inches='tight')
    plt.gcf().clear()
	
    plt.plot(arr3,color='red')
    plt.title('"business" versus time')
    plt.xlabel('time(in months)')
    plt.ylabel('frequency')
    plt.savefig('%s_fig3.png' %(name),bbox_inches='tight')
    plt.gcf().clear()
	
    plt.plot(arr4)
    plt.title('Noise-2')
    plt.savefig('%s_fig4.png' %(name),bbox_inches='tight')
    plt.gcf().clear()