# -*- coding: utf-8 -*-
"""
Created on Sat Oct 17 11:47:21 2020

@author: sayakdibyo
"""

docs = []
from os import listdir, chdir
import os
import re

   
# Here's my attempt at coming up with regular expressions to filter out
# parts of the enron emails that I deem as useless.

email_pat = re.compile(".+@.+")
to_pat = re.compile("To:.+\n")
cc_pat = re.compile("cc:.+\n")
subject_pat = re.compile("Subject:.+\n")
from_pat = re.compile("From:.+\n")
sent_pat = re.compile("Sent:.+\n")
received_pat = re.compile("Received:.+\n")
ctype_pat = re.compile("Content-Type:.+\n")
reply_pat = re.compile("Reply- Organization:.+\n")
date_pat = re.compile("Date:.+\n")
xmail_pat = re.compile("X-Mailer:.+\n")
mimver_pat = re.compile("MIME-Version:.+\n")
dash_pat = re.compile("--+.+--+", re.DOTALL)
star_pat = re.compile('\*\*+.+\*\*+', re.DOTALL)
uscore_pat = re.compile(" __+.+__+", re.DOTALL)
equals_pat = re.compile("==+.+==+", re.DOTALL)
contentinfo_pat = re.compile("----------------------------------------.+----------------------------------------")
forwardedby_pat = re.compile("----------------------.+----------------------")
caution_pat = re.compile('''\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*.+\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*''')
privacy_pat = re.compile(" _______________________________________________________________.+ _______________________________________________________________")

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
    sent_dirs_words = [subfolders[i] for i in sent_dirs]
    for d in sent_dirs_words:
        chdir('C:\\Users\\sayakdibyo\\Desktop\\maildir\\%s\\%s' % (name,d))
        file_list = listdir('.')
        #print(file_list)
        docs.append([" ".join(open(f, 'r').readlines()) for f in file_list if(os.path.isfile(f))])
        
# Here i go into each email from each employee, try to filter out all the useless stuff,
# then paste the email into one long flat list.  This is probably inefficient, but oh well - python
# is pretty fast anyway!
#print(docs)
docs_final = []
for subfolder in docs:
    for email in subfolder:
        if ".nsf" in email:
            etype = ".nsf"
        elif ".pst" in email:
            etype = ".pst"
        email_new = email[email.find(etype)+4:]
        email_new = to_pat.sub('', email_new)
        email_new = cc_pat.sub('', email_new)
        email_new = subject_pat.sub('', email_new)
        email_new = from_pat.sub('', email_new)
        email_new = sent_pat.sub('', email_new)
        email_new = email_pat.sub('', email_new)
        if "-----Original Message-----" in email_new:
            email_new = email_new.replace("-----Original Message-----","")
        email_new = ctype_pat.sub('', email_new)
        email_new = reply_pat.sub('', email_new)
        email_new = date_pat.sub('', email_new)
        email_new = xmail_pat.sub('', email_new)
        email_new = mimver_pat.sub('', email_new)
        email_new = contentinfo_pat.sub('', email_new)
        email_new = forwardedby_pat.sub('', email_new)
        email_new = caution_pat.sub('', email_new)
        email_new = privacy_pat.sub('', email_new)
        docs_final.append(email_new)

# Here I proceed to dump each and every email into about 126 thousand separate 
# txt files in a newly created 'data' directory.  This gets it ready for entry into a Corpus using the tm (textmining)
# package from R.

for n, doc in enumerate(docs_final):
    outfile = open("C:\\Users\\sayakdibyo\\Desktop\\nlp_assignment\\data\\%s.txt" % n,'w')
    outfile.write(doc)
    outfile.close()