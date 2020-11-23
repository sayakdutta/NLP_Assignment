# -*- coding: utf-8 -*-
"""
Created on Thu Oct 22 12:17:05 2020

@author: sayakdibyo
"""

# -*- coding: utf-8 -*-
"""
Created on Sat Oct 17 11:47:21 2020

@author: sayakdibyo
"""

docs = []
col=['Msg-ID','Date','X-From','X-To','From','To','Subject','Mime-ver','content-type','content-encoding','X-cc','X-bcc','X-Folder','X-origin','X-file']
from os import listdir, chdir
from pandas import DataFrame
import os
import re
import networkx as nx

g=nx.Graph()
   
# Here's my attempt at coming up with regular expressions to filter out
# parts of the enron emails that I deem as useless.

msg_id=re.compile("Message-ID:.+\n")
date=re.compile("Date:.+\n")
From=re.compile("From:.+\n")
to=re.compile("To:.+\n")
sub=re.compile("Subject:.+\n")
mime=re.compile("Mime-Version:.+\n")
content_type=re.compile("Content-Type:.+\n")
content_enc=re.compile("Content-Transfer-Encoding:.+\n")
x_from=re.compile("X-From:.+\n")
x_to=re.compile("X-To:.+\n")
x_cc=re.compile("X-cc:.+\n")
x_bcc=re.compile("X-bcc:.+\n")
x_folder=re.compile("X-Folder:.+\n")
x_origin=re.compile("X-Origin:.+\n")
x_filename=re.compile("X-FileName:.+\n")

# The enron emails are in 151 directories representing each each senior management
# employee whose email account was entered into the dataset.
# The task here is to go into each folder, and enter each 
# email text file into one long nested list.
# I've used readlines() to read in the emails because read() 
# didn't seem to work with these email files.

chdir("C:\\Users\\sayakdibyo\\Desktop\\maildir")
names = [d for d in listdir(".") if "." not in d]
for name in names:
    chdir("C:\\Users\\sayakdibyo\\Desktop\\maildir\\%s" % name)
    subfolders = listdir('.')
    sent_dirs = [n for n, sf in enumerate(subfolders) if "sent" in sf]
    sent_dirs_words = [subfolders[i] for i in sent_dirs ]
    for d in sent_dirs_words:
        chdir('C:\\Users\\sayakdibyo\\Desktop\\maildir\\%s\\%s' % (name,d))
        file_list = listdir('.')
        #print(file_list)
        docs.append([" ".join(open(f, 'r').readlines()) for f in file_list if(os.path.isfile(f))])
        break
    break
        
# Here i go into each email from each employee, try to filter out all the useless stuff,
# then paste the email into one long flat list.  This is probably inefficient, but oh well - python
# is pretty fast anyway!
#print(docs)
d=[]
dict={}
for subfolder in docs:
    
    for email in subfolder:
        l=[]
        p=msg_id.findall(email)
        if(len(p)>1):
            l.append(p[0])
        else:
            l+=p
        p=date.findall(email)
        if(len(p)>1):
            l.append(p[0])
        else:
            l+=p
        p=x_from.findall(email)
        if(len(p)>1):
            l.append(p[0])
        else:
            l+=p
        p=x_to.findall(email)
        if(len(p)>1):
            l.append(p[0])
        else:
            l+=p
        email=x_from.sub('',email)
        email=x_to.sub('',email)
        p=From.findall(email)
        if(len(p)>1):
            l.append(p[0])
        else:
            l+=p
        
        p=to.findall(email)
        if(len(p)>1):
            l.append(p[0])
        else:
            l+=p
        #print(to.findall(email))
        p=sub.findall(email)
        if(len(p)>1):
            l.append(p[0])
        else:
            l+=p
        #print(l)
        p=mime.findall(email)
        if(len(p)>1):
            l.append(p[0])
        else:
            l+=p
        p=content_type.findall(email)
        if(len(p)>1):
            l.append(p[0])
        else:
            l+=p
        p=content_enc.findall(email)
        if(len(p)>1):
            l.append(p[0])
        else:
            l+=p
        p=x_cc.findall(email)
        if(len(p)>1):
            l.append(p[0])
        else:
            l+=p
        p=x_bcc.findall(email)
        if(len(p)>1):
            l.append(p[0])
        else:
            l+=p
        p=x_folder.findall(email)
        if(len(p)>1):
            l.append(p[0])
        else:
            l+=p
        p=x_origin.findall(email)
        if(len(p)>1):
            l.append(p[0])
        else:
            l+=p
        p=x_filename.findall(email)
        if(len(p)>1):
            l.append(p[0])
        else:
            l+=p
        sender=(l[4].split(' '))[1]
        receiver= (l[5].split(' '))[1]
        for i in receiver.split(','):
            
            if(sender=="" or i==""):
                continue
            if(sender[-1]=='\n'):
                sender=sender[:-1]
            if(i[-1]=='\n'):
                i=i[:-1]
            if((sender,i) in dict.keys() ):
                dict[(sender,i)]+=1
            else:
                dict[(sender,i)]=1
            if((i,sender) in dict.keys() ):
                dict[(i,sender)]+=1
            else:
                dict[(i,sender)]=1
    break
for key in dict:
    if(dict[key]>=10):
        g.add_edge(key[0],key[1])
for k in (nx.find_cliques(g)):
    print(len(k))

        
        

